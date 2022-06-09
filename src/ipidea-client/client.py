""" Client Library for IPIDEA Proxy Service API
"""
class IpIdeaProxy(object):

  def __init__(self) -> None:
    pass

  """API authorization
  """
  def auth(self):
    pass

  """whitelisting APIs
  """

  def add_whitelist(self):
    pass

  def list_whitelist(self):
    pass

  def delete_whitelist(self):
    pass

  
  """authentication APIs
  """

  def add_auth_account(self):
    pass

  def patch_auth_account(self):
    pass

  def delete_auth_account(self):
    pass


  """flow APIs
  """

  def get_remaining_quota(self):
    pass

  def set_alarm_threshold(self):
    pass

  def get_main_account_usage(self):
    pass

  def get_sub_account_usage(self):
    pass

  """IP APIs
  """

  def datacenter_ip(self):
    pass

  def residential_ip(self):
    pass

  def get_datacenter_ip(self):
    pass

  def get_residential_ips(self):
    pass

  def get_residential_ips(self):
    pass


  """ordering APIs
  """

  def get_dynamic_flow_orders(self):
    pass

  def get_datacenter_ip_orders(self):
    pass

  def get_residential_ip_orders(self):
    pass
