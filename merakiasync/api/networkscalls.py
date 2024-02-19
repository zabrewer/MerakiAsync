import asyncio

import merakiasync.asynctasks.networkstasks as async_tasks

class Networks:
    def __init__(self, apikey, debug_dict):
        self._apikey = apikey
        self._debug_dict = debug_dict
        self._loop = asyncio.get_event_loop()

    def AsyncGetNetwork(self, networks, **kwargs):
        """
        **Return a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network

        networks: (list) List containing one or more networks (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetwork(
                networks= networks,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkAlertsHistory(self, networks, **kwargs):
        """
        **Return the alert history for this network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-alerts-history

        networks: (list) List containing one or more networks (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        
        The following optional paramaters can be passed directly to the class as arguments:
            - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100. (optional)
            - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - total_pages (integer or string): (defaults to "all") use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages (optional)
            - direction (string): direction to paginate, either "next" (default) or "prev" page (optional)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkalertshistory(
                networks= networks,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkAlertsSettings(self, networks, **kwargs):
        """
        **Return the alert configuration for this network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-alerts-settings

        networks: (list) List containing one or more networks (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkalertssettings(
                networks= networks,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkBluetoothClients(self, networks, **kwargs):
        """
        **List the Bluetooth clients seen by APs in this network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-bluetooth-clients

        networks: (list) List containing one or more networks (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        
        The following optional paramaters can be passed directly to the class as arguments:
            - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 7 days from today. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 7 days. The default is 1 day. (optional)
            - perPage (integer): The number of entries per page returned. Acceptable range is 5 - 1000. Default is 10. (optional)
            - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - includeConnectivityHistory (boolean): Include the connectivity history for this client (optional)
            - total_pages (integer or string): (defaults to "all") use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages (optional)
            - direction (string): direction to paginate, either "next" (default) or "prev" page (optional)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkbluetoothclients(
                networks= networks,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkBluetoothClient(self, networks, **kwargs):
        """
        **Return a Bluetooth client. Bluetooth clients can be identified by their ID or their MAC.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-bluetooth-client

        networks: (list) List containing one or more networks (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
            - bluetoothClientId (string): Bluetooth client ID (required)
        
        The following optional paramaters can be passed directly to the class as arguments:
            - includeConnectivityHistory (boolean): Include the connectivity history for this client (optional)
            - connectivityHistoryTimespan (integer): The timespan, in seconds, for the connectivityHistory data. By default 1 day, 86400, will be used. (optional)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkbluetoothclient(
                networks= networks,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkClients(self, networks, **kwargs):
        """
        **List the clients that have used this network in the timespan. The data is updated at most once every five minutes.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-clients

        networks: (list) List containing one or more networks (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        
        The following optional paramaters can be passed directly to the class as arguments:
            - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day. (optional)
            - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 5000. Default is 10. (optional)
            - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - statuses (array): Filters clients based on status. Can be one of 'Online' or 'Offline'. (optional)
            - ip (string): Filters clients based on a partial or full match for the ip address field. (optional)
            - ip6 (string): Filters clients based on a partial or full match for the ip6 address field. (optional)
            - ip6Local (string): Filters clients based on a partial or full match for the ip6Local address field. (optional)
            - mac (string): Filters clients based on a partial or full match for the mac address field. (optional)
            - os (string): Filters clients based on a partial or full match for the os (operating system) field. (optional)
            - pskGroup (string): Filters clients based on partial or full match for the iPSK name field. (optional)
            - description (string): Filters clients based on a partial or full match for the description field. (optional)
            - vlan (string): Filters clients based on the full match for the VLAN field. (optional)
            - namedVlan (string): Filters clients based on the partial or full match for the named VLAN field. (optional)
            - recentDeviceConnections (array): Filters clients based on recent connection type. Can be one of 'Wired' or 'Wireless'. (optional)
            - total_pages (integer or string): (defaults to "all") use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages (optional)
            - direction (string): direction to paginate, either "next" (default) or "prev" page (optional)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkclients(
                networks= networks,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkClientsApplicationUsage(self, networks, **kwargs):
        """
        **Return the application usage data for clients. Usage data is in kilobytes. Clients can be identified by client keys or either the MACs or IPs depending on whether the network uses Track-by-IP.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-clients-application-usage

        networks: (list) List containing one or more networks (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
            - clients (string): A list of client keys, MACs or IPs separated by comma. (required)
        
        The following optional paramaters can be passed directly to the class as arguments:
            - ssidNumber (integer): An SSID number to include. If not specified, eveusage histories application usagents for all SSIDs will be returned. (optional)
            - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. (optional)
            - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today. (optional)
            - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day. (optional)
            - total_pages (integer or string): (defaults to "all") use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages (optional)
            - direction (string): direction to paginate, either "next" (default) or "prev" page (optional)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkclientsapplicationusage(
                networks= networks,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkClientsBandwidthUsageHistory(self, networks, **kwargs):
        """
        **Returns a timeseries of total traffic consumption rates for all clients on a network within a given timespan, in megabits per second.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-clients-bandwidth-usage-history

        networks: (list) List containing one or more networks (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        
        The following optional paramaters can be passed directly to the class as arguments:
            - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 30 days from today. (optional)
            - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day. (optional)
            - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. (optional)
            - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - total_pages (integer or string): (defaults to "all") use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages (optional)
            - direction (string): direction to paginate, either "next" (default) or "prev" page (optional)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkclientsbandwidthusagehistory(
                networks= networks,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkClientsOverview(self, networks, **kwargs):
        """
        **Return overview statistics for network clients**
        https://developer.cisco.com/meraki/api-v1/#!get-network-clients-overview

        networks: (list) List containing one or more networks (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        
        The following optional paramaters can be passed directly to the class as arguments:
            - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today. (optional)
            - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day. (optional)
            - resolution (integer): The time resolution in seconds for returned data. The valid resolutions are: 7200, 86400, 604800, 2592000. The default is 604800. (optional)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkclientsoverview(
                networks= networks,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkClientsUsageHistories(self, networks, **kwargs):
        """
        **Return the usage histories for clients. Usage data is in kilobytes. Clients can be identified by client keys or either the MACs or IPs depending on whether the network uses Track-by-IP.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-clients-usage-histories

        networks: (list) List containing one or more networks (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
            - clients (string): A list of client keys, MACs or IPs separated by comma. (required)
        
        The following optional paramaters can be passed directly to the class as arguments:
            - ssidNumber (integer): An SSID number to include. If not specified, events for all SSIDs will be returned. (optional)
            - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. (optional)
            - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today. (optional)
            - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day. (optional)
            - total_pages (integer or string): (defaults to "all") use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages (optional)
            - direction (string): direction to paginate, either "next" (default) or "prev" page (optional)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkclientsusagehistories(
                networks= networks,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkClient(self, networks, **kwargs):
        """
        **Return the client associated with the given identifier. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-client

        networks: (list) List containing one or more networks (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
            - clientId (string): Client ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkclient(
                networks= networks,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkClientPolicy(self, networks, **kwargs):
        """
        **Return the policy assigned to a client on the network. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-client-policy

        networks: (list) List containing one or more networks (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
            - clientId (string): Client ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkclientpolicy(
                networks= networks,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkClientSplashAuthorizationStatus(self, networks, **kwargs):
        """
        **Return the splash authorization for a client, for each SSID they've associated with through splash. Only enabled SSIDs with Click-through splash enabled will be included. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-client-splash-authorization-status

        networks: (list) List containing one or more networks (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
            - clientId (string): Client ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkclientsplashauthorizationstatus(
                networks= networks,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkClientTrafficHistory(self, networks, **kwargs):
        """
        **Return the client's network traffic data over time. Usage data is in kilobytes. This endpoint requires detailed traffic analysis to be enabled on the Network-wide > General page. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-client-traffic-history

        networks: (list) List containing one or more networks (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
            - clientId (string): Client ID (required)
        
        The following optional paramaters can be passed directly to the class as arguments:
            - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. (optional)
            - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - total_pages (integer or string): (defaults to "all") use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages (optional)
            - direction (string): direction to paginate, either "next" (default) or "prev" page (optional)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkclienttraffichistory(
                networks= networks,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkClientUsageHistory(self, networks, **kwargs):
        """
        **Return the client's daily usage history. Usage data is in kilobytes. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-client-usage-history

        networks: (list) List containing one or more networks (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
            - clientId (string): Client ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkclientusagehistory(
                networks= networks,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkDevices(self, networks, **kwargs):
        """
        **List the devices in a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-devices

        networks: (list) List containing one or more networks (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkdevices(
                networks= networks,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkEvents(self, networks, **kwargs):
        """
        **List the events for the network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-events

        networks: (list) List containing one or more networks (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        
        The following optional paramaters can be passed directly to the class as arguments:
            - productType (string): The product type to fetch events for. This parameter is required for networks with multiple device types. Valid types are wireless, appliance, switch, systemsManager, camera, and cellularGateway (optional)
            - includedEventTypes (array): A list of event types. The returned events will be filtered to only include events with these types. (optional)
            - excludedEventTypes (array): A list of event types. The returned events will be filtered to exclude events with these types. (optional)
            - deviceMac (string): The MAC address of the Meraki device which the list of events will be filtered with (optional)
            - deviceSerial (string): The serial of the Meraki device which the list of events will be filtered with (optional)
            - deviceName (string): The name of the Meraki device which the list of events will be filtered with (optional)
            - clientIp (string): The IP of the client which the list of events will be filtered with. Only supported for track-by-IP networks. (optional)
            - clientMac (string): The MAC address of the client which the list of events will be filtered with. Only supported for track-by-MAC networks. (optional)
            - clientName (string): The name, or partial name, of the client which the list of events will be filtered with (optional)
            - smDeviceMac (string): The MAC address of the Systems Manager device which the list of events will be filtered with (optional)
            - smDeviceName (string): The name of the Systems Manager device which the list of events will be filtered with (optional)
            - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 10. (optional)
            - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - total_pages (integer or string): (defaults to "all") use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages (optional)
            - direction (string): direction to paginate, either "next" or "prev" (default) page (optional)
            - event_log_end_time (string): ISO8601 Zulu/UTC time, to use in conjunction with startingAfter, to retrieve events within a time window (optional)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkevents(
                networks= networks,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkEventsEventTypes(self, networks, **kwargs):
        """
        **List the event type to human-readable description**
        https://developer.cisco.com/meraki/api-v1/#!get-network-events-event-types

        networks: (list) List containing one or more networks (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkeventseventtypes(
                networks= networks,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkFirmwareUpgrades(self, networks, **kwargs):
        """
        **Get firmware upgrade information for a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-firmware-upgrades

        networks: (list) List containing one or more networks (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkfirmwareupgrades(
                networks= networks,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkFirmwareUpgradesStagedEvents(self, networks, **kwargs):
        """
        **Get the Staged Upgrade Event from a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-firmware-upgrades-staged-events

        networks: (list) List containing one or more networks (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkfirmwareupgradesstagedevents(
                networks= networks,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkFirmwareUpgradesStagedGroups(self, networks, **kwargs):
        """
        **List of Staged Upgrade Groups in a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-firmware-upgrades-staged-groups

        networks: (list) List containing one or more networks (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkfirmwareupgradesstagedgroups(
                networks= networks,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkFirmwareUpgradesStagedGroup(self, networks, **kwargs):
        """
        **Get a Staged Upgrade Group from a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-firmware-upgrades-staged-group

        networks: (list) List containing one or more networks (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
            - groupId (string): Group ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkfirmwareupgradesstagedgroup(
                networks= networks,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkFirmwareUpgradesStagedStages(self, networks, **kwargs):
        """
        **Order of Staged Upgrade Groups in a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-firmware-upgrades-staged-stages

        networks: (list) List containing one or more networks (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkfirmwareupgradesstagedstages(
                networks= networks,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkFloorPlans(self, networks, **kwargs):
        """
        **List the floor plans that belong to your network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-floor-plans

        networks: (list) List containing one or more networks (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkfloorplans(
                networks= networks,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkFloorPlan(self, networks, **kwargs):
        """
        **Find a floor plan by ID**
        https://developer.cisco.com/meraki/api-v1/#!get-network-floor-plan

        networks: (list) List containing one or more networks (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
            - floorPlanId (string): Floor plan ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkfloorplan(
                networks= networks,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkGroupPolicies(self, networks, **kwargs):
        """
        **List the group policies in a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-group-policies

        networks: (list) List containing one or more networks (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkgrouppolicies(
                networks= networks,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkGroupPolicy(self, networks, **kwargs):
        """
        **Display a group policy**
        https://developer.cisco.com/meraki/api-v1/#!get-network-group-policy

        networks: (list) List containing one or more networks (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
            - groupPolicyId (string): Group policy ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkgrouppolicy(
                networks= networks,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkHealthAlerts(self, networks, **kwargs):
        """
        **Return all global alerts on this network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-health-alerts

        networks: (list) List containing one or more networks (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkhealthalerts(
                networks= networks,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkMerakiAuthUsers(self, networks, **kwargs):
        """
        **List the users configured under Meraki Authentication for a network (splash guest or RADIUS users for a wireless network, or client VPN users for a MX network)**
        https://developer.cisco.com/meraki/api-v1/#!get-network-meraki-auth-users

        networks: (list) List containing one or more networks (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkmerakiauthusers(
                networks= networks,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkMerakiAuthUser(self, networks, **kwargs):
        """
        **Return the Meraki Auth splash guest, RADIUS, or client VPN user**
        https://developer.cisco.com/meraki/api-v1/#!get-network-meraki-auth-user

        networks: (list) List containing one or more networks (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
            - merakiAuthUserId (string): Meraki auth user ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkmerakiauthuser(
                networks= networks,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkMqttBrokers(self, networks, **kwargs):
        """
        **List the MQTT brokers for this network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-mqtt-brokers

        networks: (list) List containing one or more networks (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkmqttbrokers(
                networks= networks,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkMqttBroker(self, networks, **kwargs):
        """
        **Return an MQTT broker**
        https://developer.cisco.com/meraki/api-v1/#!get-network-mqtt-broker

        networks: (list) List containing one or more networks (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
            - mqttBrokerId (string): Mqtt broker ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkmqttbroker(
                networks= networks,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkNetflow(self, networks, **kwargs):
        """
        **Return the NetFlow traffic reporting settings for a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-netflow

        networks: (list) List containing one or more networks (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworknetflow(
                networks= networks,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkNetworkHealthChannelUtilization(self, networks, **kwargs):
        """
        **Get the channel utilization over each radio for all APs in a network.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-network-health-channel-utilization

        networks: (list) List containing one or more networks (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        
        The following optional paramaters can be passed directly to the class as arguments:
            - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today. (optional)
            - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day. (optional)
            - resolution (integer): The time resolution in seconds for returned data. The valid resolutions are: 600. The default is 600. (optional)
            - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100. Default is 10. (optional)
            - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - total_pages (integer or string): (defaults to "all") use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages (optional)
            - direction (string): direction to paginate, either "next" (default) or "prev" page (optional)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworknetworkhealthchannelutilization(
                networks= networks,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkPiiPiiKeys(self, networks, **kwargs):
        """
        **List the keys required to access Personally Identifiable Information (PII) for a given identifier. Exactly one identifier will be accepted. If the organization contains org-wide Systems Manager users matching the key provided then there will be an entry with the key "0" containing the applicable keys.

## ALTERNATE PATH

```
/organizations/{organizationId}/pii/piiKeys
```**
        https://developer.cisco.com/meraki/api-v1/#!get-network-pii-pii-keys

        networks: (list) List containing one or more networks (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        
        The following optional paramaters can be passed directly to the class as arguments:
            - username (string): The username of a Systems Manager user (optional)
            - email (string): The email of a network user account or a Systems Manager device (optional)
            - mac (string): The MAC of a network client device or a Systems Manager device (optional)
            - serial (string): The serial of a Systems Manager device (optional)
            - imei (string): The IMEI of a Systems Manager device (optional)
            - bluetoothMac (string): The MAC of a Bluetooth client (optional)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkpiipiikeys(
                networks= networks,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkPiiRequests(self, networks, **kwargs):
        """
        **List the PII requests for this network or organization

## ALTERNATE PATH

```
/organizations/{organizationId}/pii/requests
```**
        https://developer.cisco.com/meraki/api-v1/#!get-network-pii-requests

        networks: (list) List containing one or more networks (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkpiirequests(
                networks= networks,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkPiiRequest(self, networks, **kwargs):
        """
        **Return a PII request

## ALTERNATE PATH

```
/organizations/{organizationId}/pii/requests/{requestId}
```**
        https://developer.cisco.com/meraki/api-v1/#!get-network-pii-request

        networks: (list) List containing one or more networks (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
            - requestId (string): Request ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkpiirequest(
                networks= networks,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkPiiSmDevicesForKey(self, networks, **kwargs):
        """
        **Given a piece of Personally Identifiable Information (PII), return the Systems Manager device ID(s) associated with that identifier. These device IDs can be used with the Systems Manager API endpoints to retrieve device details. Exactly one identifier will be accepted.

## ALTERNATE PATH

```
/organizations/{organizationId}/pii/smDevicesForKey
```**
        https://developer.cisco.com/meraki/api-v1/#!get-network-pii-sm-devices-for-key

        networks: (list) List containing one or more networks (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        
        The following optional paramaters can be passed directly to the class as arguments:
            - username (string): The username of a Systems Manager user (optional)
            - email (string): The email of a network user account or a Systems Manager device (optional)
            - mac (string): The MAC of a network client device or a Systems Manager device (optional)
            - serial (string): The serial of a Systems Manager device (optional)
            - imei (string): The IMEI of a Systems Manager device (optional)
            - bluetoothMac (string): The MAC of a Bluetooth client (optional)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkpiismdevicesforkey(
                networks= networks,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkPiiSmOwnersForKey(self, networks, **kwargs):
        """
        **Given a piece of Personally Identifiable Information (PII), return the Systems Manager owner ID(s) associated with that identifier. These owner IDs can be used with the Systems Manager API endpoints to retrieve owner details. Exactly one identifier will be accepted.

## ALTERNATE PATH

```
/organizations/{organizationId}/pii/smOwnersForKey
```**
        https://developer.cisco.com/meraki/api-v1/#!get-network-pii-sm-owners-for-key

        networks: (list) List containing one or more networks (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        
        The following optional paramaters can be passed directly to the class as arguments:
            - username (string): The username of a Systems Manager user (optional)
            - email (string): The email of a network user account or a Systems Manager device (optional)
            - mac (string): The MAC of a network client device or a Systems Manager device (optional)
            - serial (string): The serial of a Systems Manager device (optional)
            - imei (string): The IMEI of a Systems Manager device (optional)
            - bluetoothMac (string): The MAC of a Bluetooth client (optional)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkpiismownersforkey(
                networks= networks,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkPoliciesByClient(self, networks, **kwargs):
        """
        **Get policies for all clients with policies**
        https://developer.cisco.com/meraki/api-v1/#!get-network-policies-by-client

        networks: (list) List containing one or more networks (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        
        The following optional paramaters can be passed directly to the class as arguments:
            - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 50. (optional)
            - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day. (optional)
            - total_pages (integer or string): (defaults to "all") use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages (optional)
            - direction (string): direction to paginate, either "next" (default) or "prev" page (optional)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkpoliciesbyclient(
                networks= networks,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkSettings(self, networks, **kwargs):
        """
        **Return the settings for a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-settings

        networks: (list) List containing one or more networks (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworksettings(
                networks= networks,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkSnmp(self, networks, **kwargs):
        """
        **Return the SNMP settings for a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-snmp

        networks: (list) List containing one or more networks (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworksnmp(
                networks= networks,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkSplashLoginAttempts(self, networks, **kwargs):
        """
        **List the splash login attempts for a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-splash-login-attempts

        networks: (list) List containing one or more networks (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        
        The following optional paramaters can be passed directly to the class as arguments:
            - ssidNumber (integer): Only return the login attempts for the specified SSID (optional)
            - loginIdentifier (string): The username, email, or phone number used during login (optional)
            - timespan (integer): The timespan, in seconds, for the login attempts. The period will be from [timespan] seconds ago until now. The maximum timespan is 3 months (optional)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworksplashloginattempts(
                networks= networks,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkSyslogServers(self, networks, **kwargs):
        """
        **List the syslog servers for a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-syslog-servers

        networks: (list) List containing one or more networks (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworksyslogservers(
                networks= networks,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkTopologyLinkLayer(self, networks, **kwargs):
        """
        **List the LLDP and CDP information for all discovered devices and connections in a network. At least one MX or MS device must be in the network in order to build the topology.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-topology-link-layer

        networks: (list) List containing one or more networks (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworktopologylinklayer(
                networks= networks,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkTraffic(self, networks, **kwargs):
        """
        **Return the traffic analysis data for this network. Traffic analysis with hostname visibility must be enabled on the network.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-traffic

        networks: (list) List containing one or more networks (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        
        The following optional paramaters can be passed directly to the class as arguments:
            - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 30 days from today. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 30 days. (optional)
            - deviceType (string): Filter the data by device type: 'combined', 'wireless', 'switch' or 'appliance'. Defaults to 'combined'. When using 'combined', for each rule the data will come from the device type with the most usage. (optional)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworktraffic(
                networks= networks,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkTrafficAnalysis(self, networks, **kwargs):
        """
        **Return the traffic analysis settings for a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-traffic-analysis

        networks: (list) List containing one or more networks (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworktrafficanalysis(
                networks= networks,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkTrafficShapingApplicationCategories(self, networks, **kwargs):
        """
        **Returns the application categories for traffic shaping rules. Only applicable on networks with a security applicance.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-traffic-shaping-application-categories

        networks: (list) List containing one or more networks (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworktrafficshapingapplicationcategories(
                networks= networks,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkTrafficShapingDscpTaggingOptions(self, networks, **kwargs):
        """
        **Returns the available DSCP tagging options for your traffic shaping rules.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-traffic-shaping-dscp-tagging-options

        networks: (list) List containing one or more networks (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworktrafficshapingdscptaggingoptions(
                networks= networks,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkVlanProfiles(self, networks, **kwargs):
        """
        **List VLAN profiles for a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-vlan-profiles

        networks: (list) List containing one or more networks (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkvlanprofiles(
                networks= networks,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkVlanProfilesAssignmentsByDevice(self, networks, **kwargs):
        """
        **Get the assigned VLAN Profiles for devices in a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-vlan-profiles-assignments-by-device

        networks: (list) List containing one or more networks (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        
        The following optional paramaters can be passed directly to the class as arguments:
            - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. (optional)
            - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - serials (array): Optional parameter to filter devices by serials. All devices returned belong to serial numbers that are an exact match. (optional)
            - productTypes (array): Optional parameter to filter devices by product types. (optional)
            - stackIds (array): Optional parameter to filter devices by Switch Stack ids. (optional)
            - total_pages (integer or string): (defaults to "all") use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages (optional)
            - direction (string): direction to paginate, either "next" (default) or "prev" page (optional)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkvlanprofilesassignmentsbydevice(
                networks= networks,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkVlanProfile(self, networks, **kwargs):
        """
        **Get an existing VLAN profile of a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-vlan-profile

        networks: (list) List containing one or more networks (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
            - iname (string): Iname (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkvlanprofile(
                networks= networks,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkWebhooksHttpServers(self, networks, **kwargs):
        """
        **List the HTTP servers for a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-webhooks-http-servers

        networks: (list) List containing one or more networks (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkwebhookshttpservers(
                networks= networks,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkWebhooksHttpServer(self, networks, **kwargs):
        """
        **Return an HTTP server for a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-webhooks-http-server

        networks: (list) List containing one or more networks (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
            - httpServerId (string): Http server ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkwebhookshttpserver(
                networks= networks,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkWebhooksPayloadTemplates(self, networks, **kwargs):
        """
        **List the webhook payload templates for a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-webhooks-payload-templates

        networks: (list) List containing one or more networks (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkwebhookspayloadtemplates(
                networks= networks,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkWebhooksPayloadTemplate(self, networks, **kwargs):
        """
        **Get the webhook payload template for a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-webhooks-payload-template

        networks: (list) List containing one or more networks (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
            - payloadTemplateId (string): Payload template ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkwebhookspayloadtemplate(
                networks= networks,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkWebhooksWebhookTest(self, networks, **kwargs):
        """
        **Return the status of a webhook test for a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-webhooks-webhook-test

        networks: (list) List containing one or more networks (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
            - webhookTestId (string): Webhook test ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkwebhookswebhooktest(
                networks= networks,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

