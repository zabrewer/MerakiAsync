import merakiasync
from pprint import pprint

my_apikey = 'ABC123'

# initiate our class AsyncDashboard from the merakiasync library - this only needs to be done ONCE
async_session = merakiasync.AsyncDashboard(apikey=my_apikey)

# instatiate the organizations method from AsyncDashboard class in __init__.py
# this in turn automatically instatiates the Organizations class 
# repeat below for networks, devices, etc. - only one time PER each scope (class)
organization_session = async_session.organizations()

# get all organization that our apikey has access to
all_organizations = organization_session.AsyncGetOrganizations()

# prettyprint all of our organizations
pprint(all_organizations)

# for ALL of our organizations, get all networks:
all_networks = organization_session.AsyncGetOrganizationNetworks(organizations=all_organizations)

'''
Note that in the above line we DID NOT have to loop through each org and pass them in individually.  All MerakiAsync classes take a list containing one or more dictionaries. Each nested dictionary must include the requred paramaters for the given MerakiAsync Method. In most cases this is done automatically e.g. after calling AsyncGetOrganizations, MerakiAsync added OrganizationId to every nested dictionary before returning the entire list so we don't have to do anything to call AsyncGetOrganizationNetworks.

MerakiAsync also indvidually handles calling the meraki dashboard for each organization using async tasks which speeds up the entire operation.
'''
pprint(all_networks)
