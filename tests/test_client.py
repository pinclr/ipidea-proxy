from ipidea_proxy import client
import os

class TestApi(object):

  def __init__(self, uid='', appkey='') -> None:
    #
    # get the uid and appkey from https://www.ipidea.net/ipidea-api.html#001
    # after signed in from https://www.ipidea.net/userLogin
    #
    if uid:
      self.uid = uid
    else:
      self.uid = os.environ.get('IPIDEA_UID')

    if appkey:
      self.appkey = appkey
    else:
      self.appkey = os.environ.get('IPIDEA_APPKEY')

    ipp = client.IpideaProxy(uid, appkey)
    

    def get_full_whitelisted_ips():
        full_ips = []
        for log in ipp.list_whitelist()['ret_data']['lists']:
            for k,v in log.keys():
                if k == 'mark_ip':
                    full_ips.append(v)
        return full_ips
    
    
    def split_whitelist_ips(white_ips):
        if ',' in white_ips:
            split_ips = white_ips.split(',')
        else:
            split_ips = white_ips
        return split_ips
    
    
    def test_add_whitelist_msg_equals_success(white_ips):
        assert ipp.add_whitelist(white_ips)['msg'] == 'success'

        
    def test_whitelists_were_added(white_ips):
        f = get_full_whitelisted_ips()
        s = split_whitelist_ips(white_ips)
        assert set(s) < set(f)
    
    
    def test_delete_whitelist_msg_equals_success(white_ips):
        assert ipp.delete_whitelist(white_ips)['msg'] == 'success'
        
    
    def test_ips_are_not_whitelisted(white_ips):
        f = get_full_whitelisted_ips()
        s = split_whitelist_ips(white_ips) 
        assert (set(s) & set(f)) == set()
        
        
    def test_list_whitelist_msg_equals_success():
        assert ipp.list_whitelist()['msg'] == 'success'


    def get_main_account_usage_msg_equals_success():
        assert ipp.get_main_account_usage()['msg'] == 'success'
        
        
    def test_get_remaining_quota_msg_equals_success():
        assert ipp.get_remaining_quota()['msg'] == 'success'


    def test_get_sub_account_usage_msg_equals_success(sub_id):
        assert ipp.get_sub_account_usage(sub_id)['msg'] == 'success'
    
    
    def test_set_alarm_threshold_msg_equals_success(phone, flow_upper_limit, operate, status):
        assert ipp.set_alarm_threshold(phone, flow_upper_limit, operate, status)['msg'] == 'success'
