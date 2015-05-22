from abc import ABCMeta, abstractmethod
import json
import requests

from util.app_config import AppConfig


class BaseAPI:

  __metaclass__ = ABCMeta

  ### private methods

  @abstractmethod
  def _get_api_path(self):
    """Retrieves path component for specific API endpoint
    Returns
    str -- endpoint path component (e.g. '/campsites')
    """
    return

  @classmethod
  def _get_api_key_str(cls):
    return AppConfig.get_config()['api_key']

  @classmethod
  def _get_base_url(cls):
    return AppConfig.get_config()['endpoint_base_url']

  @classmethod
  def _get_auth_url(cls, path, *args):
    print 'args: ' + str(args)
    final_path = path
    if len(args) > 0:
      final_path = path.format(*args)
    print 'final_path: ' + final_path

    path_base = '{0}{1}?apikey={2}'.format(
        cls._get_base_url(), final_path, cls._get_api_key_str())
    return path_base

  @classmethod
  def _send_get_request(cls, full_url):
    # todo: try catch
    response = requests.get(full_url)

    # todo: try catch
    resp_dict = json.loads(response.text)

    return resp_dict
