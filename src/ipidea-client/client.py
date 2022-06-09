""" Client Library for IPIDEA Proxy Service API
"""

import requests

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


  """get IP addresses
  """
  def get_ip_address_from_auth_account(self, proxy_user, proxy_pass, proxy_addr='proxy.ipidea.io:2333', proxy_region=''):

    proxies = {
      'http': proxy_addr
    }

    if proxy_region != '':
      proxy_region = '-region-'+proxy_region
    proxy_pass = f"{proxy_user}-zone-custom{proxy_region}:{proxy_pass}"

    url = 'http://ipinfo.io'

    session = requests.Session()
    session.auth = (proxy_user, proxy_pass)

    res = session.get(url, proxies=proxies)
    try:
      data = res.json()
    except Exception as e:
      raise(e)

    return data

def get_ip_addresses_from_whitlisted_ip(self, nums=100, proto='http', format='json', region=''):
  # cap on 900
  if nums > 900:
    nums = 900
  if nums < 1:
    nums = 1

  API_BASE = 'api.proxy.ipidea.io/getProxyIp'
  if nums > 500:
    url = f'http://{API_BASE}?big_num={nums}&return_type={format}&lb=1&sb=0&flow=1&regions={region}&protocol={proto}'
  else:
    url = f'http://{API_BASE}?num={nums}&return_type={format}&lb=1&sb=0&flow=1&regions={region}&protocol={proto}'

  res = requests(url)

  try:
    data = res.json()
  except Exception as e:
    raise(e)

  return data
