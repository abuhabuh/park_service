from model.park_obj_base import ParkObjBase
from park_api.facility_api import FacilityAPI


class Campsite(ParkObjBase):

  def __init__(self, resp_dict):
    self.resp_dict = resp_dict
    self.id = resp_dict['CampsiteID']
    self.facility_id = resp_dict['FacilityID']

  ### public methods

  def get_location(self):
    facility_api = FacilityAPI()
    facility = facility_api.get_facility(self.facility_id)

    return facility.get_location()
