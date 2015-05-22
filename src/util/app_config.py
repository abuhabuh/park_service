import yaml


class AppConfig():

  CONFIG_YAML = 'conf/config.yaml'
  CONFIG = None

  @classmethod
  def get_config(cls):
    """
    Returns
    dict
    """
    cls._load_config()
    return cls.CONFIG

  @classmethod
  def _load_config(cls):
    if cls.CONFIG is None:
      stream = open(cls.CONFIG_YAML, 'r')
      cls.CONFIG = yaml.load(stream)
