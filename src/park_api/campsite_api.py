from park_api.base_api import BaseAPI
from model.campsite import Campsite


class CampsiteAPI(BaseAPI):

  # todo - extract
  PATH_DICT = {
    'all_sites': '/campsites',
    'site': '/campsites/{0}'
  }

  ### public methods

  def get_site(self, site_id):
    """Get specific campsite

    Returns
    Campsite -- campsite object
    """
    request_url = CampsiteAPI._get_auth_url(
        self._get_api_path('site'), site_id)

    response_items = CampsiteAPI._send_get_request(request_url)
    if not response_items or len(response_items) == 0:
      return None

    site_dict = response_items[0]

    return Campsite(site_dict)

  def get_all_sites(self):
    request_url = CampsiteAPI._get_auth_url(
        self._get_api_path('all_sites'))

    response_items = CampsiteAPI._send_get_request(request_url)

    if not response_items or not 'RECDATA' in response_items:
      return None

    site_dicts = response_items['RECDATA']

    camp_sites = []
    for site_dict in site_dicts:
      camp_sites.append(Campsite(site_dict))

    return camp_sites

  ### private methods

  def _get_api_path(self, path_key_str):
    """See BaseAPI for spec"""
    return CampsiteAPI.PATH_DICT[path_key_str]
