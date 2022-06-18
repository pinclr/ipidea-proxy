import os
import time

from src.ipidea_proxy.client import IpideaProxy


class TestApi(object):

  def setup_class(cls):
    cls.ipp = IpideaProxy()

  def get_full_whitelisted_ips(self):
    full_ips = []
    for log in self.ipp.list_whitelist()['ret_data']['lists']:
      for k, v in log.keys():
        if k == 'mark_ip':
          full_ips.append(v)
    return full_ips

  def split_whitelist_ips(self):
    white_ips = '1.2.3.4,1.2.3.5'
    if ',' in white_ips:
      split_ips = white_ips.split(',')
    else:
      split_ips = white_ips
    return split_ips

  def test_add_whitelist_msg_equals_success(self):
    white_ips = '1.2.3.4,1.2.3.5'
    assert self.ipp.add_whitelist(white_ips)['msg'] == 'success'

  '''
  def test_whitelists_were_added(self):
    white_ips = '1.2.3.4,1.2.3.5'
    f = self.get_full_whitelisted_ips()
    s = self.split_whitelist_ips(white_ips)
    assert set(s) < set(f)
  '''

  def test_delete_whitelist_msg_equals_success(self):
    time.sleep(2)
    white_ips = '1.2.3.4,1.2.3.5'
    assert self.ipp.delete_whitelist(white_ips)['msg'] == 'success'
        
  '''
  def test_ips_are_not_whitelisted(self):
    white_ips = '1.2.3.4,1.2.3.5'
    f = self.get_full_whitelisted_ips()
    s = self.split_whitelist_ips(white_ips) 
    assert (set(s) & set(f)) == set()
  '''

  def test_list_whitelist_msg_equals_success(self):
    time.sleep(2)
    assert self.ipp.list_whitelist()['msg'] == 'success'

  def get_main_account_usage_msg_equals_success(self):
    time.sleep(2)
    start_time = '2022-06-01 00:00:00'
    end_time = '2022-06-07 23:59:59'
    assert self.ipp.get_main_account_usage(start_time, end_time)['msg'] == 'success'

  def test_get_remaining_quota_msg_equals_success(self):
    time.sleep(2)
    assert self.ipp.get_remaining_quota()['msg'] == 'success'

  def test_get_sub_account_usage_msg_equals_success(self):
    time.sleep(2)
    sub_id = '313'
    start_time = '2022-06-01 00:00:00'
    end_time = '2022-06-07 23:59:59'
    assert self.ipp.get_sub_account_usage(sub_id, start_time, end_time)['msg'] == 'success'

  def test_set_alarm_threshold_msg_equals_success(self):
    time.sleep(2)
    phone = '18888888888'
    flow_upper_limit = '101'
    operate = '1'
    status = '1'
    assert self.ipp.set_alarm_threshold(phone, flow_upper_limit, operate, status)['msg'] == 'success'
