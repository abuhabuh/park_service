from park_api.base_api import BaseAPI


class OrgAPI(BaseAPI):

  ### public methods

  def get_all_orgs(self):
    request_url = self._get_auth_url(self._get_api_path())

    return OrgAPI._send_get_request(request_url)

  ### private methods

  def _get_api_path(self):
    return '/organizations'
