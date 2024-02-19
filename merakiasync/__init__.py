import inspect
import os

import merakiasync.api.organizationscalls as organizationscalls
import merakiasync.api.networkscalls as networkscalls
import merakiasync.api.devicescalls as devicescalls
import merakiasync.api.insightcalls as insightcalls
import merakiasync.api.wirelesscalls as wirelesscalls
import merakiasync.api.appliancecalls as appliancecalls
import merakiasync.api.switchcalls as switchcalls
import merakiasync.api.cellularGatewaycalls as cellularGatewaycalls
import merakiasync.api.administeredcalls as administeredcalls
import merakiasync.api.licensingcalls as licensingcalls

__author__ = 'Zach Brewer'
__email__ = 'zbrewer@cisco.com'
__version__ = '1.0.02'
__license__ = 'MIT'

def _create_logdir(directory_name):
    '''
    Returns the path containing the .py file calling this library

    Creates directory_name directory in the directory of the calling .py file if it does not exist
    '''
    frame = inspect.stack()[-1]
    module = inspect.getmodule(frame[0])
    calling_dir = os.path.dirname(os.path.realpath(module.__file__))
    parent_log_path = os.path.join(calling_dir, directory_name)
    path_exists = os.path.exists(parent_log_path)
    if not path_exists:
        os.makedirs(parent_log_path)

    return parent_log_path

class AsyncDashboard(object):
    '''
    **Creates an instance of merakiasync**
    - apikey (string): API key generated in dashboard; can also be set as an environment variable MERAKI_DASHBOARD_API_KEY
    - async_debug (boolean): Set to debug True/False
    - debug_dict (dict): Provide your own debug and concurrency related values as dictionary keys/values. If async_debug = True, debug_dict is ignored
    debug dict expected keys:
        - base_url (string): preceding all endpoint resources
        - wait_on_rate_limit (boolean): retry if 429 rate limit error encountered?
        - maximum_retries (integer): retry up to this many times when encountering 429s or other server-side errors
        - output_log (boolean): create an output log file?
        - log_path (string): path to output log; by default, working directory of script if not specified
        - log_file_prefix (string): log file name appended with date and timestamp
        - print_console (boolean): print logging output to console?
        - suppress_logging (boolean): disable all logging? you're on your own then!
        - caller (string): optional identifier for API usage tracking; can also be set as an environment variable MERAKI_PYTHON_SDK_CALLER
    '''
    def __init__(self, apikey, async_debug=False, debug_dict=None):
        if debug_dict:
            if not isinstance(debug_dict, dict):
                print('Debug dictionary must by of type dict')
                exit(0)
            else:
                required_keys = ['base_url', 'log_file_prefix', 'log_path', 'maximum_concurrent_requests', 'maximum_retries', 'wait_on_rate_limit', 'output_log', 'print_console', 'suppress_logging', 'caller']
                for each_key in required_keys:
                    if each_key not in debug_dict.keys():
                        print(f'Error: Key "{each_key}" not found in debug_dict keys')
                        exit(0)
        if async_debug:
            log_path = _create_logdir(directory_name='merakiasync_logs')
            debug_dict={
                        'base_url': 'https://api.meraki.com/api/v1',
                        'log_file_prefix': 'merakiasync',
                        'log_path': log_path,
                        'maximum_concurrent_requests': 10,
                        'maximum_retries': 100,
                        'wait_on_rate_limit': True,
                        'output_log': True,
                        'print_console': True,
                        'suppress_logging': False,
                        'caller': f'MerakiAsync/{__version__} ZachBrewerMeraki'
                    }
        else:
            debug_dict={
                        'base_url': 'https://api.meraki.com/api/v1',
                        'log_file_prefix': __file__[:-3],
                        'log_path': '',
                        'maximum_concurrent_requests': 10,
                        'maximum_retries': 100,
                        'wait_on_rate_limit': True,
                        'output_log': False,
                        'print_console': False,
                        'suppress_logging': True,
                        'caller': f'MerakiAsync/{__version__} ZachBrewerMeraki'
                    }

        self._debug_dict = debug_dict
        self._apikey = apikey
        self._organizations = organizationscalls.Organizations(apikey=self._apikey, debug_dict=self._debug_dict)
        self._networks = networkscalls.Networks(apikey=self._apikey, debug_dict=self._debug_dict)
        self._devices = devicescalls.Devices(apikey=self._apikey, debug_dict=self._debug_dict)
        self._insight = insightcalls.Insight(apikey=self._apikey, debug_dict=self._debug_dict)
        self._wireless = wirelesscalls.Wireless(apikey=self._apikey, debug_dict=self._debug_dict)
        self._appliance = appliancecalls.Appliance(apikey=self._apikey, debug_dict=self._debug_dict)
        self._switch = switchcalls.Switch(apikey=self._apikey, debug_dict=self._debug_dict)
        self._cellularGateway = cellularGatewaycalls.CellularGateway(apikey=self._apikey, debug_dict=self._debug_dict)
        self._administered = administeredcalls.Administered(apikey=self._apikey, debug_dict=self._debug_dict)
        self._licensing = licensingcalls.Licensing(apikey=self._apikey, debug_dict=self._debug_dict)

    def organizations(self):
        return self._organizations
    
    def networks(self):
        return self._networks
    
    def devices(self):
        return self._devices
    
    def insight(self):
        return self._insight
    
    def wireless(self):
        return self._wireless
    
    def appliance(self):
        return self._appliance
    
    def switch(self):
        return self._switch
    
    def cellularGateway(self):
        return self._cellularGateway
    
    def administered(self):
        return self._administered
    
    def licensing(self):
        return self._licensing
    


