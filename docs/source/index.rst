#########################################
:mod:`ipidea_proxy` --- ipidea_proxy Python library
#########################################

.. module:: ipidea_proxy

The :mod:`ipidea_proxy` module provides
  - :mod:`ipidea_proxy.client.IpideaProxy`: A client for ipidea's HTTP API.


Installation
============

Install from PyPI::

    $ pip install ipidea-proxy --upgrade


Initialization
============

:mod:`ipidea_proxy` must be initialized with :meth:`ipidea_proxy.client.IpideaProxy`. 
A uid and an app key are required. The uid and app key can be passed explicitly 
to :meth:`ipidea_proxy.client.IpideaProxy` or defined as environment variables
``IPIDEA_UID`` and ``IPIDEA_APPKEY`` respectively.

Here's an example to initialize the client

1.Defining environment variables in advance::

    from ipidea_proxy.client import IpideaProxy
   
    ipp = IpideaProxy()

2.Use uid and appkey explicitly with the client::

    from ipidea_proxy.client import IpideaProxy

    ipp = IpideaProxy(uid='xxxx', appkey='xxxxxx')



Usage
~~~~~

Be sure to initialize the client using :meth:`ipidea_proxy.client.IpideaProxy` and then 
use :meth:`ipidea_proxy.client.IpideaProxy` for more API purposes::

    from ipidea_proxy.client import IpideaProxy
   
    ipp = IpideaProxy()

    # add whitelist ips:
    ipp.add_whitelist(white_ips)

    # list whitelist ips:
    ipp.list_whitelist()

    # delete whitelist ips:
    ipp.delete_whitelist(white_ips)

    # get account remaining quota:
    ipp.get_remaining_quota()

    # set account alarm threshold:
    ipp.set_alaram_threshold(phone, flow_upper_limit, operate, status)

    # get main account usage during a time period:
    ipp.get_main_account_usage(start_time, end_time)

    # get sub account usage during a time period:
    ipp.get_sub_account_usage(sub_id, start_time, end_time)

