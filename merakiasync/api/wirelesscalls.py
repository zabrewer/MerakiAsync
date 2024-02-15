import asyncio

import merakiasync.asynctasks.wirelesstasks as async_tasks

class Wireless:
    def __init__(self, apikey, debug_dict):
        self._apikey = apikey
        self._debug_dict = debug_dict
        self._loop = asyncio.get_event_loop()

    def AsyncGetDeviceWirelessBluetoothSettings(self, all_wireless, **kwargs):
        """
        **Return the bluetooth settings for a wireless device**
        https://developer.cisco.com/meraki/api-v1/#!get-device-wireless-bluetooth-settings

        wireless: (list) List containing one or more wireless (dict).  Each nested dict must include following required keys/values:
            - serial (string): Serial (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getdevicewirelessbluetoothsettings(
                all_wireless= all_wireless,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetDeviceWirelessConnectionStats(self, all_wireless, **kwargs):
        """
        **Aggregated connectivity info for a given AP on this network**
        https://developer.cisco.com/meraki/api-v1/#!get-device-wireless-connection-stats

        wireless: (list) List containing one or more wireless (dict).  Each nested dict must include following required keys/values:
            - serial (string): Serial (required)
        
        The following optional paramaters can be passed directly to the class as arguments:
            - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today. (optional)
            - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. (optional)
            - band (string): Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information. (optional)
            - ssid (integer): Filter results by SSID (optional)
            - vlan (integer): Filter results by VLAN (optional)
            - apTag (string): Filter results by AP Tag (optional)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getdevicewirelessconnectionstats(
                all_wireless= all_wireless,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetDeviceWirelessLatencyStats(self, all_wireless, **kwargs):
        """
        **Aggregated latency info for a given AP on this network**
        https://developer.cisco.com/meraki/api-v1/#!get-device-wireless-latency-stats

        wireless: (list) List containing one or more wireless (dict).  Each nested dict must include following required keys/values:
            - serial (string): Serial (required)
        
        The following optional paramaters can be passed directly to the class as arguments:
            - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today. (optional)
            - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. (optional)
            - band (string): Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information. (optional)
            - ssid (integer): Filter results by SSID (optional)
            - vlan (integer): Filter results by VLAN (optional)
            - apTag (string): Filter results by AP Tag (optional)
            - fields (string): Partial selection: If present, this call will return only the selected fields of ["rawDistribution", "avg"]. All fields will be returned by default. Selected fields must be entered as a comma separated string. (optional)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getdevicewirelesslatencystats(
                all_wireless= all_wireless,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetDeviceWirelessRadioSettings(self, all_wireless, **kwargs):
        """
        **Return the radio settings of a device**
        https://developer.cisco.com/meraki/api-v1/#!get-device-wireless-radio-settings

        wireless: (list) List containing one or more wireless (dict).  Each nested dict must include following required keys/values:
            - serial (string): Serial (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getdevicewirelessradiosettings(
                all_wireless= all_wireless,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetDeviceWirelessStatus(self, all_wireless, **kwargs):
        """
        **Return the SSID statuses of an access point**
        https://developer.cisco.com/meraki/api-v1/#!get-device-wireless-status

        wireless: (list) List containing one or more wireless (dict).  Each nested dict must include following required keys/values:
            - serial (string): Serial (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getdevicewirelessstatus(
                all_wireless= all_wireless,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkWirelessAirMarshal(self, all_wireless, **kwargs):
        """
        **List Air Marshal scan results from a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-air-marshal

        wireless: (list) List containing one or more wireless (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        
        The following optional paramaters can be passed directly to the class as arguments:
            - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 7 days. (optional)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkwirelessairmarshal(
                all_wireless= all_wireless,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkWirelessAlternateManagementInterface(self, all_wireless, **kwargs):
        """
        **Return alternate management interface and devices with IP assigned**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-alternate-management-interface

        wireless: (list) List containing one or more wireless (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkwirelessalternatemanagementinterface(
                all_wireless= all_wireless,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkWirelessBilling(self, all_wireless, **kwargs):
        """
        **Return the billing settings of this network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-billing

        wireless: (list) List containing one or more wireless (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkwirelessbilling(
                all_wireless= all_wireless,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkWirelessBluetoothSettings(self, all_wireless, **kwargs):
        """
        **Return the Bluetooth settings for a network. <a href="https://documentation.meraki.com/MR/Bluetooth/Bluetooth_Low_Energy_(BLE)">Bluetooth settings</a> must be enabled on the network.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-bluetooth-settings

        wireless: (list) List containing one or more wireless (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkwirelessbluetoothsettings(
                all_wireless= all_wireless,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkWirelessChannelUtilizationHistory(self, all_wireless, **kwargs):
        """
        **Return AP channel utilization over time for a device or network client**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-channel-utilization-history

        wireless: (list) List containing one or more wireless (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        
        The following optional paramaters can be passed directly to the class as arguments:
            - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today. (optional)
            - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days. (optional)
            - resolution (integer): The time resolution in seconds for returned data. The valid resolutions are: 600, 1200, 3600, 14400, 86400. The default is 86400. (optional)
            - autoResolution (boolean): Automatically select a data resolution based on the given timespan; this overrides the value specified by the 'resolution' parameter. The default setting is false. (optional)
            - clientId (string): Filter results by network client to return per-device, per-band AP channel utilization metrics inner joined by the queried client's connection history. (optional)
            - deviceSerial (string): Filter results by device to return AP channel utilization metrics for the queried device; either :band or :clientId must be jointly specified. (optional)
            - apTag (string): Filter results by AP tag to return AP channel utilization metrics for devices labeled with the given tag; either :clientId or :deviceSerial must be jointly specified. (optional)
            - band (string): Filter results by band (either '2.4', '5' or '6'). (optional)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkwirelesschannelutilizationhistory(
                all_wireless= all_wireless,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkWirelessClientCountHistory(self, all_wireless, **kwargs):
        """
        **Return wireless client counts over time for a network, device, or network client**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-client-count-history

        wireless: (list) List containing one or more wireless (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        
        The following optional paramaters can be passed directly to the class as arguments:
            - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today. (optional)
            - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days. (optional)
            - resolution (integer): The time resolution in seconds for returned data. The valid resolutions are: 300, 600, 1200, 3600, 14400, 86400. The default is 86400. (optional)
            - autoResolution (boolean): Automatically select a data resolution based on the given timespan; this overrides the value specified by the 'resolution' parameter. The default setting is false. (optional)
            - clientId (string): Filter results by network client to return per-device client counts over time inner joined by the queried client's connection history. (optional)
            - deviceSerial (string): Filter results by device. (optional)
            - apTag (string): Filter results by AP tag. (optional)
            - band (string): Filter results by band (either '2.4', '5' or '6'). (optional)
            - ssid (integer): Filter results by SSID number. (optional)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkwirelessclientcounthistory(
                all_wireless= all_wireless,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkWirelessClientsConnectionStats(self, all_wireless, **kwargs):
        """
        **Aggregated connectivity info for this network, grouped by clients**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-clients-connection-stats

        wireless: (list) List containing one or more wireless (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        
        The following optional paramaters can be passed directly to the class as arguments:
            - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today. (optional)
            - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. (optional)
            - band (string): Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information. (optional)
            - ssid (integer): Filter results by SSID (optional)
            - vlan (integer): Filter results by VLAN (optional)
            - apTag (string): Filter results by AP Tag (optional)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkwirelessclientsconnectionstats(
                all_wireless= all_wireless,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkWirelessClientsLatencyStats(self, all_wireless, **kwargs):
        """
        **Aggregated latency info for this network, grouped by clients**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-clients-latency-stats

        wireless: (list) List containing one or more wireless (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        
        The following optional paramaters can be passed directly to the class as arguments:
            - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today. (optional)
            - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. (optional)
            - band (string): Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information. (optional)
            - ssid (integer): Filter results by SSID (optional)
            - vlan (integer): Filter results by VLAN (optional)
            - apTag (string): Filter results by AP Tag (optional)
            - fields (string): Partial selection: If present, this call will return only the selected fields of ["rawDistribution", "avg"]. All fields will be returned by default. Selected fields must be entered as a comma separated string. (optional)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkwirelessclientslatencystats(
                all_wireless= all_wireless,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkWirelessClientConnectionStats(self, all_wireless, **kwargs):
        """
        **Aggregated connectivity info for a given client on this network. Clients are identified by their MAC.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-client-connection-stats

        wireless: (list) List containing one or more wireless (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
            - clientId (string): Client ID (required)
        
        The following optional paramaters can be passed directly to the class as arguments:
            - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today. (optional)
            - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. (optional)
            - band (string): Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information. (optional)
            - ssid (integer): Filter results by SSID (optional)
            - vlan (integer): Filter results by VLAN (optional)
            - apTag (string): Filter results by AP Tag (optional)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkwirelessclientconnectionstats(
                all_wireless= all_wireless,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkWirelessClientConnectivityEvents(self, all_wireless, **kwargs):
        """
        **List the wireless connectivity events for a client within a network in the timespan.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-client-connectivity-events

        wireless: (list) List containing one or more wireless (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
            - clientId (string): Client ID (required)
        
        The following optional paramaters can be passed directly to the class as arguments:
            - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. (optional)
            - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today. (optional)
            - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day. (optional)
            - types (array): A list of event types to include. If not specified, events of all types will be returned. Valid types are 'assoc', 'disassoc', 'auth', 'deauth', 'dns', 'dhcp', 'roam', 'connection' and/or 'sticky'. (optional)
            - includedSeverities (array): A list of severities to include. If not specified, events of all severities will be returned. Valid severities are 'good', 'info', 'warn' and/or 'bad'. (optional)
            - band (string): Filter results by band (either '2.4', '5', '6'). (optional)
            - ssidNumber (integer): An SSID number to include. If not specified, events for all SSIDs will be returned. (optional)
            - deviceSerial (string): Filter results by an AP's serial number. (optional)
            - total_pages (integer or string): (defaults to "all") use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages (optional)
            - direction (string): direction to paginate, either "next" (default) or "prev" page (optional)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkwirelessclientconnectivityevents(
                all_wireless= all_wireless,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkWirelessClientLatencyHistory(self, all_wireless, **kwargs):
        """
        **Return the latency history for a client. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP. The latency data is from a sample of 2% of packets and is grouped into 4 traffic categories: background, best effort, video, voice. Within these categories the sampled packet counters are bucketed by latency in milliseconds.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-client-latency-history

        wireless: (list) List containing one or more wireless (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
            - clientId (string): Client ID (required)
        
        The following optional paramaters can be passed directly to the class as arguments:
            - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 791 days from today. (optional)
            - t1 (string): The end of the timespan for the data. t1 can be a maximum of 791 days after t0. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 791 days. The default is 1 day. (optional)
            - resolution (integer): The time resolution in seconds for returned data. The valid resolutions are: 86400. The default is 86400. (optional)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkwirelessclientlatencyhistory(
                all_wireless= all_wireless,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkWirelessClientLatencyStats(self, all_wireless, **kwargs):
        """
        **Aggregated latency info for a given client on this network. Clients are identified by their MAC.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-client-latency-stats

        wireless: (list) List containing one or more wireless (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
            - clientId (string): Client ID (required)
        
        The following optional paramaters can be passed directly to the class as arguments:
            - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today. (optional)
            - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. (optional)
            - band (string): Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information. (optional)
            - ssid (integer): Filter results by SSID (optional)
            - vlan (integer): Filter results by VLAN (optional)
            - apTag (string): Filter results by AP Tag (optional)
            - fields (string): Partial selection: If present, this call will return only the selected fields of ["rawDistribution", "avg"]. All fields will be returned by default. Selected fields must be entered as a comma separated string. (optional)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkwirelessclientlatencystats(
                all_wireless= all_wireless,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkWirelessConnectionStats(self, all_wireless, **kwargs):
        """
        **Aggregated connectivity info for this network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-connection-stats

        wireless: (list) List containing one or more wireless (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        
        The following optional paramaters can be passed directly to the class as arguments:
            - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today. (optional)
            - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. (optional)
            - band (string): Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information. (optional)
            - ssid (integer): Filter results by SSID (optional)
            - vlan (integer): Filter results by VLAN (optional)
            - apTag (string): Filter results by AP Tag (optional)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkwirelessconnectionstats(
                all_wireless= all_wireless,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkWirelessDataRateHistory(self, all_wireless, **kwargs):
        """
        **Return PHY data rates over time for a network, device, or network client**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-data-rate-history

        wireless: (list) List containing one or more wireless (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        
        The following optional paramaters can be passed directly to the class as arguments:
            - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today. (optional)
            - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days. (optional)
            - resolution (integer): The time resolution in seconds for returned data. The valid resolutions are: 300, 600, 1200, 3600, 14400, 86400. The default is 86400. (optional)
            - autoResolution (boolean): Automatically select a data resolution based on the given timespan; this overrides the value specified by the 'resolution' parameter. The default setting is false. (optional)
            - clientId (string): Filter results by network client. (optional)
            - deviceSerial (string): Filter results by device. (optional)
            - apTag (string): Filter results by AP tag. (optional)
            - band (string): Filter results by band (either '2.4', '5' or '6'). (optional)
            - ssid (integer): Filter results by SSID number. (optional)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkwirelessdataratehistory(
                all_wireless= all_wireless,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkWirelessDevicesConnectionStats(self, all_wireless, **kwargs):
        """
        **Aggregated connectivity info for this network, grouped by node**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-devices-connection-stats

        wireless: (list) List containing one or more wireless (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        
        The following optional paramaters can be passed directly to the class as arguments:
            - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today. (optional)
            - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. (optional)
            - band (string): Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information. (optional)
            - ssid (integer): Filter results by SSID (optional)
            - vlan (integer): Filter results by VLAN (optional)
            - apTag (string): Filter results by AP Tag (optional)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkwirelessdevicesconnectionstats(
                all_wireless= all_wireless,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkWirelessDevicesLatencyStats(self, all_wireless, **kwargs):
        """
        **Aggregated latency info for this network, grouped by node**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-devices-latency-stats

        wireless: (list) List containing one or more wireless (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        
        The following optional paramaters can be passed directly to the class as arguments:
            - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today. (optional)
            - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. (optional)
            - band (string): Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information. (optional)
            - ssid (integer): Filter results by SSID (optional)
            - vlan (integer): Filter results by VLAN (optional)
            - apTag (string): Filter results by AP Tag (optional)
            - fields (string): Partial selection: If present, this call will return only the selected fields of ["rawDistribution", "avg"]. All fields will be returned by default. Selected fields must be entered as a comma separated string. (optional)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkwirelessdeviceslatencystats(
                all_wireless= all_wireless,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkWirelessEthernetPortsProfiles(self, all_wireless, **kwargs):
        """
        **List the AP port profiles for this network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ethernet-ports-profiles

        wireless: (list) List containing one or more wireless (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkwirelessethernetportsprofiles(
                all_wireless= all_wireless,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkWirelessEthernetPortsProfile(self, all_wireless, **kwargs):
        """
        **Show the AP port profile by ID for this network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ethernet-ports-profile

        wireless: (list) List containing one or more wireless (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
            - profileId (string): Profile ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkwirelessethernetportsprofile(
                all_wireless= all_wireless,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkWirelessFailedConnections(self, all_wireless, **kwargs):
        """
        **List of all failed client connection events on this network in a given time range**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-failed-connections

        wireless: (list) List containing one or more wireless (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        
        The following optional paramaters can be passed directly to the class as arguments:
            - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today. (optional)
            - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. (optional)
            - band (string): Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information. (optional)
            - ssid (integer): Filter results by SSID (optional)
            - vlan (integer): Filter results by VLAN (optional)
            - apTag (string): Filter results by AP Tag (optional)
            - serial (string): Filter by AP (optional)
            - clientId (string): Filter by client MAC (optional)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkwirelessfailedconnections(
                all_wireless= all_wireless,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkWirelessLatencyHistory(self, all_wireless, **kwargs):
        """
        **Return average wireless latency over time for a network, device, or network client**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-latency-history

        wireless: (list) List containing one or more wireless (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        
        The following optional paramaters can be passed directly to the class as arguments:
            - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today. (optional)
            - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days. (optional)
            - resolution (integer): The time resolution in seconds for returned data. The valid resolutions are: 300, 600, 1200, 3600, 14400, 86400. The default is 86400. (optional)
            - autoResolution (boolean): Automatically select a data resolution based on the given timespan; this overrides the value specified by the 'resolution' parameter. The default setting is false. (optional)
            - clientId (string): Filter results by network client. (optional)
            - deviceSerial (string): Filter results by device. (optional)
            - apTag (string): Filter results by AP tag. (optional)
            - band (string): Filter results by band (either '2.4', '5' or '6'). (optional)
            - ssid (integer): Filter results by SSID number. (optional)
            - accessCategory (string): Filter by access category. (optional)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkwirelesslatencyhistory(
                all_wireless= all_wireless,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkWirelessLatencyStats(self, all_wireless, **kwargs):
        """
        **Aggregated latency info for this network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-latency-stats

        wireless: (list) List containing one or more wireless (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        
        The following optional paramaters can be passed directly to the class as arguments:
            - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today. (optional)
            - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. (optional)
            - band (string): Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information. (optional)
            - ssid (integer): Filter results by SSID (optional)
            - vlan (integer): Filter results by VLAN (optional)
            - apTag (string): Filter results by AP Tag (optional)
            - fields (string): Partial selection: If present, this call will return only the selected fields of ["rawDistribution", "avg"]. All fields will be returned by default. Selected fields must be entered as a comma separated string. (optional)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkwirelesslatencystats(
                all_wireless= all_wireless,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkWirelessMeshStatuses(self, all_wireless, **kwargs):
        """
        **List wireless mesh statuses for repeaters**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-mesh-statuses

        wireless: (list) List containing one or more wireless (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        
        The following optional paramaters can be passed directly to the class as arguments:
            - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 500. Default is 50. (optional)
            - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - total_pages (integer or string): (defaults to "all") use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages (optional)
            - direction (string): direction to paginate, either "next" (default) or "prev" page (optional)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkwirelessmeshstatuses(
                all_wireless= all_wireless,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkWirelessRfProfiles(self, all_wireless, **kwargs):
        """
        **List RF profiles for this network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-rf-profiles

        wireless: (list) List containing one or more wireless (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        
        The following optional paramaters can be passed directly to the class as arguments:
            - includeTemplateProfiles (boolean): If the network is bound to a template, this parameter controls whether or not the non-basic RF profiles defined on the template should be included in the response alongside the non-basic profiles defined on the bound network. Defaults to false. (optional)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkwirelessrfprofiles(
                all_wireless= all_wireless,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkWirelessRfProfile(self, all_wireless, **kwargs):
        """
        **Return a RF profile**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-rf-profile

        wireless: (list) List containing one or more wireless (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
            - rfProfileId (string): Rf profile ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkwirelessrfprofile(
                all_wireless= all_wireless,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkWirelessSettings(self, all_wireless, **kwargs):
        """
        **Return the wireless settings for a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-settings

        wireless: (list) List containing one or more wireless (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkwirelesssettings(
                all_wireless= all_wireless,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkWirelessSignalQualityHistory(self, all_wireless, **kwargs):
        """
        **Return signal quality (SNR/RSSI) over time for a device or network client**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-signal-quality-history

        wireless: (list) List containing one or more wireless (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        
        The following optional paramaters can be passed directly to the class as arguments:
            - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today. (optional)
            - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days. (optional)
            - resolution (integer): The time resolution in seconds for returned data. The valid resolutions are: 300, 600, 1200, 3600, 14400, 86400. The default is 86400. (optional)
            - autoResolution (boolean): Automatically select a data resolution based on the given timespan; this overrides the value specified by the 'resolution' parameter. The default setting is false. (optional)
            - clientId (string): Filter results by network client. (optional)
            - deviceSerial (string): Filter results by device. (optional)
            - apTag (string): Filter results by AP tag; either :clientId or :deviceSerial must be jointly specified. (optional)
            - band (string): Filter results by band (either '2.4', '5' or '6'). (optional)
            - ssid (integer): Filter results by SSID number. (optional)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkwirelesssignalqualityhistory(
                all_wireless= all_wireless,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkWirelessSsids(self, all_wireless, **kwargs):
        """
        **List the MR SSIDs in a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssids

        wireless: (list) List containing one or more wireless (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkwirelessssids(
                all_wireless= all_wireless,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkWirelessSsid(self, all_wireless, **kwargs):
        """
        **Return a single MR SSID**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid

        wireless: (list) List containing one or more wireless (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
            - number (string): Number (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkwirelessssid(
                all_wireless= all_wireless,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkWirelessSsidBonjourForwarding(self, all_wireless, **kwargs):
        """
        **List the Bonjour forwarding setting and rules for the SSID**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-bonjour-forwarding

        wireless: (list) List containing one or more wireless (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
            - number (string): Number (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkwirelessssidbonjourforwarding(
                all_wireless= all_wireless,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkWirelessSsidDeviceTypeGroupPolicies(self, all_wireless, **kwargs):
        """
        **List the device type group policies for the SSID**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-device-type-group-policies

        wireless: (list) List containing one or more wireless (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
            - number (string): Number (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkwirelessssiddevicetypegrouppolicies(
                all_wireless= all_wireless,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkWirelessSsidEapOverride(self, all_wireless, **kwargs):
        """
        **Return the EAP overridden parameters for an SSID**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-eap-override

        wireless: (list) List containing one or more wireless (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
            - number (string): Number (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkwirelessssideapoverride(
                all_wireless= all_wireless,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkWirelessSsidFirewallL3FirewallRules(self, all_wireless, **kwargs):
        """
        **Return the L3 firewall rules for an SSID on an MR network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-firewall-l-3-firewall-rules

        wireless: (list) List containing one or more wireless (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
            - number (string): Number (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkwirelessssidfirewalll3firewallrules(
                all_wireless= all_wireless,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkWirelessSsidFirewallL7FirewallRules(self, all_wireless, **kwargs):
        """
        **Return the L7 firewall rules for an SSID on an MR network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-firewall-l-7-firewall-rules

        wireless: (list) List containing one or more wireless (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
            - number (string): Number (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkwirelessssidfirewalll7firewallrules(
                all_wireless= all_wireless,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkWirelessSsidHotspot20(self, all_wireless, **kwargs):
        """
        **Return the Hotspot 2.0 settings for an SSID**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-hotspot-2-0

        wireless: (list) List containing one or more wireless (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
            - number (string): Number (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkwirelessssidhotspot20(
                all_wireless= all_wireless,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkWirelessSsidIdentityPsks(self, all_wireless, **kwargs):
        """
        **List all Identity PSKs in a wireless network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-identity-psks

        wireless: (list) List containing one or more wireless (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
            - number (string): Number (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkwirelessssididentitypsks(
                all_wireless= all_wireless,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkWirelessSsidIdentityPsk(self, all_wireless, **kwargs):
        """
        **Return an Identity PSK**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-identity-psk

        wireless: (list) List containing one or more wireless (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
            - number (string): Number (required)
            - identityPskId (string): Identity psk ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkwirelessssididentitypsk(
                all_wireless= all_wireless,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkWirelessSsidSchedules(self, all_wireless, **kwargs):
        """
        **List the outage schedule for the SSID**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-schedules

        wireless: (list) List containing one or more wireless (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
            - number (string): Number (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkwirelessssidschedules(
                all_wireless= all_wireless,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkWirelessSsidSplashSettings(self, all_wireless, **kwargs):
        """
        **Display the splash page settings for the given SSID**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-splash-settings

        wireless: (list) List containing one or more wireless (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
            - number (string): Number (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkwirelessssidsplashsettings(
                all_wireless= all_wireless,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkWirelessSsidTrafficShapingRules(self, all_wireless, **kwargs):
        """
        **Display the traffic shaping settings for a SSID on an MR network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-traffic-shaping-rules

        wireless: (list) List containing one or more wireless (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
            - number (string): Number (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkwirelessssidtrafficshapingrules(
                all_wireless= all_wireless,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkWirelessSsidVpn(self, all_wireless, **kwargs):
        """
        **List the VPN settings for the SSID.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-vpn

        wireless: (list) List containing one or more wireless (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
            - number (string): Number (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkwirelessssidvpn(
                all_wireless= all_wireless,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkWirelessUsageHistory(self, all_wireless, **kwargs):
        """
        **Return AP usage over time for a device or network client**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-usage-history

        wireless: (list) List containing one or more wireless (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        
        The following optional paramaters can be passed directly to the class as arguments:
            - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today. (optional)
            - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days. (optional)
            - resolution (integer): The time resolution in seconds for returned data. The valid resolutions are: 300, 600, 1200, 3600, 14400, 86400. The default is 86400. (optional)
            - autoResolution (boolean): Automatically select a data resolution based on the given timespan; this overrides the value specified by the 'resolution' parameter. The default setting is false. (optional)
            - clientId (string): Filter results by network client to return per-device AP usage over time inner joined by the queried client's connection history. (optional)
            - deviceSerial (string): Filter results by device. Requires :band. (optional)
            - apTag (string): Filter results by AP tag; either :clientId or :deviceSerial must be jointly specified. (optional)
            - band (string): Filter results by band (either '2.4', '5' or '6'). (optional)
            - ssid (integer): Filter results by SSID number. (optional)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkwirelessusagehistory(
                all_wireless= all_wireless,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationWirelessDevicesChannelUtilizationByDevice(self, all_wireless, **kwargs):
        """
        **Get average channel utilization for all bands in a network, split by AP**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-channel-utilization-by-device

        wireless: (list) List containing one or more wireless (dict).  Each nested dict must include following required keys/values:
            - organizationId (string): Organization ID (required)
        
        The following optional paramaters can be passed directly to the class as arguments:
            - networkIds (array): Filter results by network. (optional)
            - serials (array): Filter results by device. (optional)
            - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. (optional)
            - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 90 days from today. (optional)
            - t1 (string): The end of the timespan for the data. t1 can be a maximum of 90 days after t0. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 90 days. The default is 7 days. (optional)
            - interval (integer): The time interval in seconds for returned data. The valid intervals are: 300, 600, 3600, 7200, 14400, 21600. The default is 3600. (optional)
            - total_pages (integer or string): (defaults to "all") use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages (optional)
            - direction (string): direction to paginate, either "next" (default) or "prev" page (optional)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationwirelessdeviceschannelutilizationbydevice(
                all_wireless= all_wireless,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationWirelessDevicesChannelUtilizationByNetwork(self, all_wireless, **kwargs):
        """
        **Get average channel utilization across all bands for all networks in the organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-channel-utilization-by-network

        wireless: (list) List containing one or more wireless (dict).  Each nested dict must include following required keys/values:
            - organizationId (string): Organization ID (required)
        
        The following optional paramaters can be passed directly to the class as arguments:
            - networkIds (array): Filter results by network. (optional)
            - serials (array): Filter results by device. (optional)
            - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. (optional)
            - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 90 days from today. (optional)
            - t1 (string): The end of the timespan for the data. t1 can be a maximum of 90 days after t0. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 90 days. The default is 7 days. (optional)
            - interval (integer): The time interval in seconds for returned data. The valid intervals are: 300, 600, 3600, 7200, 14400, 21600. The default is 3600. (optional)
            - total_pages (integer or string): (defaults to "all") use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages (optional)
            - direction (string): direction to paginate, either "next" (default) or "prev" page (optional)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationwirelessdeviceschannelutilizationbynetwork(
                all_wireless= all_wireless,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationWirelessDevicesChannelUtilizationHistoryByDeviceByInterval(self, all_wireless, **kwargs):
        """
        **Get a time-series of average channel utilization for all bands, segmented by device.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-channel-utilization-history-by-device-by-interval

        wireless: (list) List containing one or more wireless (dict).  Each nested dict must include following required keys/values:
            - organizationId (string): Organization ID (required)
        
        The following optional paramaters can be passed directly to the class as arguments:
            - networkIds (array): Filter results by network. (optional)
            - serials (array): Filter results by device. (optional)
            - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. (optional)
            - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today. (optional)
            - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days. (optional)
            - interval (integer): The time interval in seconds for returned data. The valid intervals are: 300, 600, 3600, 7200, 14400, 21600. The default is 3600. (optional)
            - total_pages (integer or string): (defaults to "all") use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages (optional)
            - direction (string): direction to paginate, either "next" (default) or "prev" page (optional)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationwirelessdeviceschannelutilizationhistorybydevicebyinterval(
                all_wireless= all_wireless,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationWirelessDevicesChannelUtilizationHistoryByNetworkByInterval(self, all_wireless, **kwargs):
        """
        **Get a time-series of average channel utilization for all bands**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-channel-utilization-history-by-network-by-interval

        wireless: (list) List containing one or more wireless (dict).  Each nested dict must include following required keys/values:
            - organizationId (string): Organization ID (required)
        
        The following optional paramaters can be passed directly to the class as arguments:
            - networkIds (array): Filter results by network. (optional)
            - serials (array): Filter results by device. (optional)
            - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. (optional)
            - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today. (optional)
            - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days. (optional)
            - interval (integer): The time interval in seconds for returned data. The valid intervals are: 300, 600, 3600, 7200, 14400, 21600. The default is 3600. (optional)
            - total_pages (integer or string): (defaults to "all") use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages (optional)
            - direction (string): direction to paginate, either "next" (default) or "prev" page (optional)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationwirelessdeviceschannelutilizationhistorybynetworkbyinterval(
                all_wireless= all_wireless,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationWirelessDevicesEthernetStatuses(self, all_wireless, **kwargs):
        """
        **List the most recent Ethernet link speed, duplex, aggregation and power mode and status information for wireless devices.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-ethernet-statuses

        wireless: (list) List containing one or more wireless (dict).  Each nested dict must include following required keys/values:
            - organizationId (string): Organization ID (required)
        
        The following optional paramaters can be passed directly to the class as arguments:
            - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100. (optional)
            - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - networkIds (array): A list of Meraki network IDs to filter results to contain only specified networks. E.g.: networkIds[]=N_12345678&networkIds[]=L_3456 (optional)
            - total_pages (integer or string): (defaults to "all") use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages (optional)
            - direction (string): direction to paginate, either "next" (default) or "prev" page (optional)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationwirelessdevicesethernetstatuses(
                all_wireless= all_wireless,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationWirelessDevicesPacketLossByClient(self, all_wireless, **kwargs):
        """
        **Get average packet loss for the given timespan for all clients in the organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-packet-loss-by-client

        wireless: (list) List containing one or more wireless (dict).  Each nested dict must include following required keys/values:
            - organizationId (string): Organization ID (required)
        
        The following optional paramaters can be passed directly to the class as arguments:
            - networkIds (array): Filter results by network. (optional)
            - ssids (array): Filter results by SSID number. (optional)
            - bands (array): Filter results by band. Valid bands are: 2.4, 5, and 6. (optional)
            - macs (array): Filter results by client mac address(es). (optional)
            - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. (optional)
            - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 90 days from today. (optional)
            - t1 (string): The end of the timespan for the data. t1 can be a maximum of 90 days after t0. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 5 minutes and be less than or equal to 90 days. The default is 7 days. (optional)
            - total_pages (integer or string): (defaults to "all") use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages (optional)
            - direction (string): direction to paginate, either "next" (default) or "prev" page (optional)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationwirelessdevicespacketlossbyclient(
                all_wireless= all_wireless,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationWirelessDevicesPacketLossByDevice(self, all_wireless, **kwargs):
        """
        **Get average packet loss for the given timespan for all devices in the organization. Does not include device's own traffic.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-packet-loss-by-device

        wireless: (list) List containing one or more wireless (dict).  Each nested dict must include following required keys/values:
            - organizationId (string): Organization ID (required)
        
        The following optional paramaters can be passed directly to the class as arguments:
            - networkIds (array): Filter results by network. (optional)
            - serials (array): Filter results by device. (optional)
            - ssids (array): Filter results by SSID number. (optional)
            - bands (array): Filter results by band. Valid bands are: 2.4, 5, and 6. (optional)
            - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. (optional)
            - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 90 days from today. (optional)
            - t1 (string): The end of the timespan for the data. t1 can be a maximum of 90 days after t0. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 5 minutes and be less than or equal to 90 days. The default is 7 days. (optional)
            - total_pages (integer or string): (defaults to "all") use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages (optional)
            - direction (string): direction to paginate, either "next" (default) or "prev" page (optional)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationwirelessdevicespacketlossbydevice(
                all_wireless= all_wireless,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationWirelessDevicesPacketLossByNetwork(self, all_wireless, **kwargs):
        """
        **Get average packet loss for the given timespan for all networks in the organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-packet-loss-by-network

        wireless: (list) List containing one or more wireless (dict).  Each nested dict must include following required keys/values:
            - organizationId (string): Organization ID (required)
        
        The following optional paramaters can be passed directly to the class as arguments:
            - networkIds (array): Filter results by network. (optional)
            - serials (array): Filter results by device. (optional)
            - ssids (array): Filter results by SSID number. (optional)
            - bands (array): Filter results by band. Valid bands are: 2.4, 5, and 6. (optional)
            - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. (optional)
            - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 90 days from today. (optional)
            - t1 (string): The end of the timespan for the data. t1 can be a maximum of 90 days after t0. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 5 minutes and be less than or equal to 90 days. The default is 7 days. (optional)
            - total_pages (integer or string): (defaults to "all") use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages (optional)
            - direction (string): direction to paginate, either "next" (default) or "prev" page (optional)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationwirelessdevicespacketlossbynetwork(
                all_wireless= all_wireless,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

