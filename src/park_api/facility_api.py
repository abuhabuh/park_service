from park_api.base_api import BaseAPI
from model.facility import Facility


class FacilityAPI(BaseAPI):

  # todo - extract
  PATH_DICT = {
    'facility': '/facilities/{0}'
  }

  ### public methods

  def get_facility(self, facility_id):
    """Get specific facility

    Returns
    Facility -- facility object
    """
    request_url = FacilityAPI._get_auth_url(
        self._get_api_path('facility'), facility_id)

    facility_dict = FacilityAPI._send_get_request(request_url)

    if not facility_dict:
      return None

    return Facility(facility_dict)

  ### private methods

  def _get_api_path(self, path_key_str):
    """See BaseAPI for spec"""
    return FacilityAPI.PATH_DICT[path_key_str]
