from model.park_obj_base import ParkObjBase


class Facility(ParkObjBase):

  def __init__(self, resp_dict):
    self.resp_dict = resp_dict
    self.id = resp_dict['FacilityID']

    self.long = resp_dict['FacilityLongitude']
    self.lat = resp_dict['FacilityLatitude']

  ### public methods

  def get_location(self):
    """Returns lat, long tuple
    Returns
    (float, float) - (lat, long)
    """
    return (self.lat, self.long)
