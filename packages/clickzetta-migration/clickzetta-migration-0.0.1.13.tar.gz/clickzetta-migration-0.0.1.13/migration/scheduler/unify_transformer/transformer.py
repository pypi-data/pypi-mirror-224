import logging

from migration.base import ProfileConfigError
from migration.connector.destination.base import Destination
from migration.connector.source import Source
from migration.scheduler.scheduler import SchedulerConfig, Scheduler
from migration.scheduler.transformer import Transformer
from migration.scheduler.data_transformer.transformer import DataTransformer
from migration.scheduler.data_validation.validation import Validation
from migration.scheduler.schema_transformer.transformer import SchemaTransformer

logger = logging.getLogger(__name__)

DOT_SPLITTER = '.'
LEFT_BRACKET = '('


class UnifyTransformer(Transformer):
    def __init__(self, source: Source, destination: Destination, project_name: str, db_list=None,
                 config_table_list=None,
                 external_table_list=None,
                 concurrency=1, quit_if_fail=False):
        super().__init__(source, destination, project_name, db_list, config_table_list, external_table_list,
                         concurrency, quit_if_fail)
        self.schema_transformer = SchemaTransformer(source=self.source, destination=self.destination,
                                                    project_name=self.project_name, db_list=self.db_list,
                                                    config_table_list=self.config_table_list,
                                                    external_table_list=self.external_table_list,
                                                    concurrency=self.transform_concurrency,
                                                    quit_if_fail=self.quit_if_fail)
        self.data_transformer = DataTransformer(source=self.source, destination=self.destination,
                                                project_name=self.project_name, db_list=self.db_list,
                                                config_table_list=self.config_table_list,
                                                external_table_list=self.external_table_list,
                                                concurrency=self.transform_concurrency, quit_if_fail=self.quit_if_fail)
        self.validate_transformer = Validation(source=self.source, destination=self.destination,
                                               project_name=self.project_name, db_list=self.db_list,
                                               config_table_list=self.config_table_list,
                                               external_table_list=self.external_table_list,
                                               concurrency=self.transform_concurrency, quit_if_fail=self.quit_if_fail)

    def schedule_migration_tasks(self):
        self.schema_transformer.transform()
        self.data_transformer.transform()
        self.validate_transformer.transform()
