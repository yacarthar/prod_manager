"""
Root Config Module
"""
import os

from .config import (
    DevelopmentConfig,
    LocalConfig,
    ProductionConfig,
    TestingConfig,
    config_by_name,
)


CONFIG_NAME = os.environ.get("FLASK_ENV") or "local"
app_config = config_by_name[CONFIG_NAME]


is_dev_env = issubclass(app_config, DevelopmentConfig)
is_local_env = issubclass(app_config, LocalConfig)
is_prod_env = issubclass(app_config, ProductionConfig)
is_test_env = issubclass(app_config, TestingConfig)
