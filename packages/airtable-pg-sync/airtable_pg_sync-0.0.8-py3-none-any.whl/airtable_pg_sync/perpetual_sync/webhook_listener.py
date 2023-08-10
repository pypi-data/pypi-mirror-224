import _thread
import asyncio
import functools
import json
import logging
import logging.config

from aiohttp import web

from ..core import env
from ..core.clients import airtable
from ..core.types import bridges, env_types


class WebhookListener:
    __session = None

    def __init__(self, queue: bridges.Queue):
        self.env = env.value
        self.queue = queue

    @functools.cached_property
    def logger(self) -> logging.Logger:
        return logging.getLogger('Webhook Listener')

    async def handle_event(self, request, replication: env_types.Replication) -> web.Response:
        self.logger.info('Received webhook event - adding to queue')
        res = json.loads(await request.text())
        self.queue.add(id=res['webhook']['id'], replication=replication)

        return web.Response(text="Nice Webhook")

    async def health_check(self, request) -> web.Response:
        return web.Response(text="I'm alive!")

    def remove_webhooks(self):
        self.logger.info('Removing webhooks')
        for replication in self.env.replications:
            for id in airtable.Client(replication.base_id).list_webhooks():
                airtable.Client(replication.base_id).delete_webhook(id)

    def set_up_webhooks(self):
        self.logger.info('Setting up webhooks')
        for replication in self.env.replications:
            self.logger.info(f'Setting up webhook for {replication.endpoint}')
            airtable.Client(replication.base_id).setup_webhook(replication)

    def get_endpoints(self):
        self.logger.info('Getting webhook endpoints')
        health_check_endpoint = [web.get('/', self.health_check)]
        webhook_endpoints = [
            web.post(
                f'/{replication.endpoint}',
                functools.partial(self.handle_event, replication=replication)
            )
            for replication in self.env.replications
        ]

        return health_check_endpoint + webhook_endpoints

    def start(self):
        self.logger.info('Starting webhook listener')

        try:
            # TODO: Think of a better way of doing this
            self.remove_webhooks()
            self.set_up_webhooks()

            app = web.Application()
            app.add_routes(self.get_endpoints())
            runner = web.AppRunner(app)
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(runner.setup())
            site = web.TCPSite(runner, '0.0.0.0', self.env.listener_port)
            loop.run_until_complete(site.start())
            loop.run_forever()

        except Exception as e:
            self.logger.error(e)
            self.logger.error('Webhook listener failed')
            _thread.interrupt_main()
