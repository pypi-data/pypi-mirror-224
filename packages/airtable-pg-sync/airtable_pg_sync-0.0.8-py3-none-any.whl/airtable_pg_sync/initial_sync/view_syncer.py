import functools
import logging

from ..core.clients import postgres, airtable
from ..core.types import concepts, env_types


class ViewSyncer:

    def __init__(self, replication: env_types.Replication):
        self.replication = replication

    @functools.cached_property
    def logger(self) -> logging.Logger:
        return logging.getLogger('Schema Syncer')

    @functools.cache
    def _get_airtable_schema(self) -> list[concepts.Table]:
        self.logger.debug('Getting schema from Airtable')

        return airtable.Client(self.replication.base_id).get_schema()

    def _get_pg_schema(self) -> list[concepts.Table]:
        self.logger.debug('Getting schema from Postgres')

        return postgres.Client(self.replication.schema_name).get_schema()

    def drop_views(self):
        self.logger.info('Dropping views')
        for view in postgres.Client(self.replication.schema_name).get_all_views():
            self.logger.info(f'Dropping view {view}')
            postgres.Client(self.replication.schema_name).drop_view(view_name=view)

    def create_views(self):
        self.logger.info('Creating views')
        pg_table_ids = {table.id for table in self._get_pg_schema()}

        for table in self._get_airtable_schema():

            if table.id not in pg_table_ids:
                continue

            self.logger.info(f'Creating view {table.name}')
            postgres.Client(self.replication.schema_name).create_view(table=table)

    def sync(self):
        self.logger.info('Syncing views')
        self.drop_views()
        self.create_views()
