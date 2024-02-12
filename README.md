MerakiAsync
-----------------  
- [Introduction](#Introduction)
- [Installation And Use](#installation-and-use)
- [Caveats And Differences](#caveats-and-differences)

# Introduction

MerakiAsync is a Python library built on top of the existing Meraki Python SDK Meraki library.  Its purpose is to speed up scripts and applications by strictly using the async classes in the Meraki Python SDK. MerakiAsync strives for ease of use - someone using MerakiAsync does not have to code for async tasks, functions, about async loops or worry about awaits.

Performance depends upon many factors (network, the operations being performed, API rate limiting, etc.) but in current testing we've seen around 50% reduction in the elapsed time to perform MerakiAsync operations vs. non-async API operations. 

# Installation And Use

## Installation

Note: I recommend installing MerakiAsync to a Python virtual environment.

1) Create a Python virtual environment (recommended)
2) In the virtual environment folder:
``` 
https://github.com/zabrewer/MerakiAsync.git
``` 
3) With the virtual environment activated:
``` 
pip install .
``` 

Alternatively:
1) Create a Python virtual environment (recommended)
2) With the virtual environment activated:
```
 pip install "git+https://github.com/zabrewer/MerakiAsync"
```

## Use

An example use case for MerakiAsync.  Like the Meraki Python SDK, when used in Pycharm or VSCode MerakiAsync will show hints (required and optional params) for each class method.
``` python
import merakiasync
from pprint import pprint

my_apikey = 'ABC123'

# instantiate our class AsyncDashboard from the merakiasync library - this only needs to be done ONCE
async_session = merakiasync.AsyncDashboard(apikey=my_apikey)

# instantiate the organizations METHOD from AsyncDashboard class in __init__.py
# this in turn automatically instantiates the Organizations class
# repeat below for networks, devices, etc. - only one time PER each scope (class)
organization_session = async_session.organizations()

# get all organization that our apikey has access to
all_organizations = organization_session.AsyncGetOrganizations()

# prettyprint all of our organizations
pprint(all_organizations)

# for ALL of our organizations, get all networks:
all_networks = organization_session.AsyncGetOrganizationNetworks(organizations=all_organizations)

'''
Note that in the above line we DID NOT have to loop through each org and pass them in individually.  All MerakiAsync classes take a list containing one or more dictionaries. Each nested dictionary must include the required parameters for the given MerakiAsync Method. In most cases this is done automatically e.g. after calling AsyncGetOrganizations, MerakiAsync added OrganizationId to every nested dictionary before returning the entire list so we don't have to do anything to call AsyncGetOrganizationNetworks.

MerakiAsync also individually handles calling the meraki dashboard for each organization using async tasks which speeds up the entire operation.
'''
pprint(all_networks)

# let's take a more advanced use case - let's use an org-level call to get all appliances and get the DHCP subnet per appliance
appliance_devices = orgcalls_session.AsyncGetOrganizationDevices(organizations=orgs, productTypes='appliance')

'''
Note above that we added the productTypes filter. Any optional paramaters can be passed to the class directly.
Required params must be in the nested list (e.g. each dictionary in organizations must have OrganizationId - as stated before we add this automatically when calling getOrganzations, getOrganzation and others)
'''

# if we wanted to make other calls e.g. appliances, we would have to invoke the first top-level class and then we can call any class method that belongs to it
appliance_session = async_session.appliance()
appliance_dhcpsubnets = appliance_session.AsyncGetDeviceApplianceDhcpSubnets(appliance=appliance_devices)

# obviously in between any of these steps we could perform logic on the returned data to futher filter it and only target the data we wanted in the following API call

```

If you look at the above example, we do not set up the session like you do with non-async use of the Meraki Python SDK e.g.:
``` python
api_call = meraki.DashboardAPI(
    api_key=my_apikey,
    base_url="https://api.meraki.com/api/v1/",
    output_log=False,
    print_console=False,
    suppress_logging=True,
)
```

This is due to the way that Python async works with TCP connections - we cannot re-use an async session setup like the last example.  If you want to debug or change session related settings available in the Meraki Python SDK, there are several ways:

1) When you call the session, you can set debug=True e.g.:
``` python
async_session = merakiasync.AsyncDashboard(apikey=my_apikey, debug=True)
```
This is the equivalent of the following (output_log=True, print_console=True, supress_logging=False):
``` python
'base_url': 'https://api.meraki.com/api/v1',
                        'log_file_prefix': __file__[:-3],
                        'log_path': '',
                        'maximum_concurrent_requests': 10,
                        'maximum_retries': 100,
                        'wait_on_rate_limit': True,
                        'output_log': True,
                        'print_console': True,
                        'suppress_logging': False, 
```

2) you can additionally pass in your own dictionary of session settings as debug_dict e.g.
``` python
my_debug_dict = {
                'base_url': 'https://api.meraki.com/api/v1',
                'log_file_prefix': __file__[:-3],
                'log_path': 'merakiasync/logs',
                'maximum_concurrent_requests': 10,
                'maximum_retries': 100,
                'wait_on_rate_limit': True,
                'output_log': True,
                'print_console': True,
                'suppress_logging': False,
                'caller': f'MerakiAsync/{__version__}'
                }

async_session = merakiasync.AsyncDashboard(apikey=my_apikey, debug_dict=my_debug_dict)
```

Note that if you pass a debug_dict then the settings in the dict will overwrite other session settings even if debug=True.

# Caveats And Differences

The first caveat is that MerakiAsync currently only supports API calls that use the GET http method.  Support for all other methods so that there is 1:1 coverage for all API calls is forthcoming.

The second thing to call out is that you need to have a session for each top-level class as shown in the first example above (e.g. organizations, networks, appliances, insight, etc).  

After initiating once per top-level class you can use any class method (AsyncGetOrganizations, AsyncGetOrganizationNetworks, etc.) that belongs to the respective class (organizations).

Here's an example:
``` python
import merakiasync
from pprint import pprint

my_apikey = 'ABC123'

# instantiate our class AsyncDashboard from the merakiasync library - this only needs to be done ONCE
async_session = merakiasync.AsyncDashboard(apikey=my_apikey)

# instantiate the organizations METHOD from AsyncDashboard class in __init__.py
# this in turn automatically instantiates the Organizations class from 
# repeat below for networks, devices, etc. - only one time PER each scope (class)
organization_session = async_session.organizations()
networks_session = async_session.networks()
adminstered_session = async_session.administered()
cellulargateway_session = async_sessions.cellularGateway()
devices_session = async_session.devices()
insight_session = async_session.insight()
licensing_session = async_session.licensing()
switch_session = async_session.switch()
wireless_session = async_session.wireless()
appliances_session = async_session.appliances()
```

## Differences: Parameters and Data Structures

MerakiAsync works slightly differently than the Python SDK as related to what is passed to MerakiAsync and what is returned.  First, each MerakiAsync class method *always* expects a list containing nested dictionaries.  Each dictionary must include at least the required paramaters for the given class.

Additionally, MerakiAsync *always* returns a list containing nested dictionaries. 

Let's take the example of getOrganiztion (returns a single organization).  With MerakiAsync this method is called AsyncGetOrganization and like every other method under the Organizations class (with the exception of AsyncGetOrganizations), it takes **organizationId** as a required parameter.

So we need to pass in at minimum one nested dict called **organizations** that at minimum includes organizationId as a key and a related value.

This is different from how you would normally call this class in the Python SDK which only requires organizationId passed directly to the class.

Why this difference?  For each dictionary we pass into a MerakiAsync class, we split the calls using async to speed up operations and then return all output.

This is more in-tune for how we use the Meraki Python SDK at scale.  For example, the following steps are very common starting points in the Meraki API use:

1) getOrganizations
2) do some filter to only return a subset of the organizations that we want data from
3) getNetworks (for all of those organizations in step 2)
4) (optionally) filter the networks
5) getNetworkDevices, getNetworkSSIDs, or any other operation

With MerakiAsync we simply pass the entire list containing the dictiaries to the given subsequent step.

Here's a simple example:

``` python
import merakiasync
from pprint import pprint

my_apikey = 'ABC123'

# initiate our class AsyncDashboard from the merakiasync library - this only needs to be done ONCE
async_session = merakiasync.AsyncDashboard(apikey=my_apikey)

# instantiate the organizations METHOD from AsyncDashboard class in __init__.py
# this in turn automatically instantiates the Organizations class from 
# repeat below for networks, devices, etc. - only one time PER each scope (class)
organization_session = async_session.organizations()

my_organization = [{
        "id": "123456789",
        "organizationId": "123456789",
        "organizationName": "My Org",
        "name": "My Org",
        "url": "https://somemerakiurl/overview",
        "samlConsumerUrl": "",
        "samlConsumerUrls": [],
        "api": {
            "enabled": True
        },
        "licensing": {
            "model": "co-term"
        },
        "cloud": {
            "region": {
                "name": "North America"
            }
        },
        "management": {
            "details": []
        }
    }]

single_organization = orgcalls_session.AsyncGetOrganization(organizations=my_organization)
```

The above example is not great because it would simply return the same URL since getOrganization (singular) always returns a single org but a key difference to call out here is getOrganization would normally return a dictionary whereas MerakiAsync always returns one or more dictionaries inside of a nested list.

This approach makes more sense when you start using each MerakiAsync class method together in steps such as:

AsyncGetOrganizations --> AsyncGetOrganizationNetworks --> AsyncGetNetworkDevices

Other than logic (for loops) where you filter some of the data you don't need to do anything to pass the data to the next class method and get data back as a nested list. 

**MerakiAsync handles splitting up the tasks (each dictionary in the list) for async calls and returing the results.**

Another key difference is that MerakiAsync returns a list with multiple dictionaries.  Let's look at an example where we call AsyncGetOrganizationNetworks() for all Organizations that our API key has access to...

1) call AsyncGetOrganizations()
``` python
# imports and other lines omitted for brevity
all_organizations = orgnaizationcalls_session.AsyncGetOrganizations()
```

This obviously gives us an output of all orgs that our API key has access to as a nested list containing 1 org per dictionary contained in the list.

There is no async benefit to this call because it's a single call and not many calls that are split up per org, however MerakiAsync makes one key difference here vs. the Meraki Python SDK...  **Meraki async ADDS the fields organizationName and organizationId**.  

Now in practice these are exactly the same as name and id which are returned from the API but now instead of passing the parameter 'id' for organization to any subsequent org call like *AsyncGetOrganizationNetworks*, organizationId is already there for our future use in other steps.

**For each dictionary passed into a MerakiAsync class method, MerakiAsync will always try to add the following fields to each dictionary that is returned:**
* organizationId
* organizationName
* networkId
* networkName

2) call AsyncGetOrganizationNetworks()
``` python
# imports and other lines omitted for brevity
all_organizations = orgnaizationcalls_session.AsyncGetOrganizationNetworks(organizations=all_organizations)
```

Key Point: With a non-async call, you'd have to do a for loop here and call getOrganizationNetworks once for each org.  The networks would either be returned as a single list per org that contained all of the networks (dictionaries) for that given org.

MerakiAsync returns all of the networks for *all orgs* in a single list but since the organizationName field was kept, you can easily filter on networks that belong to a given org.

Note the organizationName filed in the following example output:
``` python
[{'enrollmentString': None,
  'id': 'N_1234',
  'isBoundToConfigTemplate': False,
  'name': 'MV-Lab',
  'id': 'N_1234',
  'networkName': 'MV-Lab',
  'notes': None,
  'organizationId': '12345',
  'organizationName': 'LabOrg123',
  'productTypes': ['camera'],
  'tags': ['tag1'],
  'timeZone': 'America/Los_Angeles',
  'url': 'https://n51.meraki.com/MV-Lab/omitted/manage/usage/list'},
 {'enrollmentString': None,
  'id': 'N_54321',
  'isBoundToConfigTemplate': False,
  'name': 'Meraki-WPNTesting',
  'networkId': 'N_54321',
  'networkName': 'Meraki-WPNTesting',
  'notes': '',
  'organizationId': '678910',
  'organizationName': 'LabOrgABC',
  'productTypes': ['wireless'],
  'tags': ['tag2'],
  'timeZone': 'America/Los_Angeles',
  'url': 'https://n51.meraki.com/Meraki-WPNTestin/omitted/manage/usage/list'}]
``` 

We have a single list that contains a dictionary for every network contained in any organization that was passed to AsyncGetOrganizationNetworks().  But we can now differentiate between those networks by filtering on organizationName or organizationId.

# More Information

MerakiAsync is in active development and this documentation is a work in progress.  More details including how to report bugs, changelog, and further documentation are forthcoming.
