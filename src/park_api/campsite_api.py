from park_api.base_api import BaseAPI


class CampsiteAPI(BaseAPI):

  # todo - extract
  PATH_DICT = {
    'all_sites': '/campsites',
    'site': '/campsites/{0}'
  }

  ### public methods

  def get_site(self, site_id):
    request_url = CampsiteAPI._get_auth_url(
        self._get_api_path('site'), site_id)

    print 'request_url: ' + request_url

    return CampsiteAPI._send_get_request(request_url)

  def get_all_sites(self):
    request_url = CampsiteAPI._get_auth_url(
        self._get_api_path('all_sites'))

    return CampsiteAPI._send_get_request(request_url)

  ### private methods

  def _get_api_path(self, path_key_str):
    return CampsiteAPI.PATH_DICT[path_key_str]
