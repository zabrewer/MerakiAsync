import asyncio

import merakiasync.asynctasks.cellularGatewaytasks as async_tasks

class CellularGateway:
    def __init__(self, apikey, debug_dict):
        self._apikey = apikey
        self._debug_dict = debug_dict
        self._loop = asyncio.get_event_loop()

    def AsyncGetDeviceCellularGatewayLan(self, cellularGateways, **kwargs):
        """
        **Show the LAN Settings of a MG**
        https://developer.cisco.com/meraki/api-v1/#!get-device-cellular-gateway-lan

        cellularGateway: (list) List containing one or more cellularGateway (dict).  Each nested dict must include following required keys/values:
            - serial (string): Serial (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getdevicecellulargatewaylan(
                cellularGateways= cellularGateways,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetDeviceCellularGatewayPortForwardingRules(self, cellularGateways, **kwargs):
        """
        **Returns the port forwarding rules for a single MG.**
        https://developer.cisco.com/meraki/api-v1/#!get-device-cellular-gateway-port-forwarding-rules

        cellularGateway: (list) List containing one or more cellularGateway (dict).  Each nested dict must include following required keys/values:
            - serial (string): Serial (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getdevicecellulargatewayportforwardingrules(
                cellularGateways= cellularGateways,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkCellularGatewayConnectivityMonitoringDestinations(self, cellularGateways, **kwargs):
        """
        **Return the connectivity testing destinations for an MG network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-cellular-gateway-connectivity-monitoring-destinations

        cellularGateway: (list) List containing one or more cellularGateway (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkcellulargatewayconnectivitymonitoringdestinations(
                cellularGateways= cellularGateways,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkCellularGatewayDhcp(self, cellularGateways, **kwargs):
        """
        **List common DHCP settings of MGs**
        https://developer.cisco.com/meraki/api-v1/#!get-network-cellular-gateway-dhcp

        cellularGateway: (list) List containing one or more cellularGateway (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkcellulargatewaydhcp(
                cellularGateways= cellularGateways,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkCellularGatewaySubnetPool(self, cellularGateways, **kwargs):
        """
        **Return the subnet pool and mask configured for MGs in the network.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-cellular-gateway-subnet-pool

        cellularGateway: (list) List containing one or more cellularGateway (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkcellulargatewaysubnetpool(
                cellularGateways= cellularGateways,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkCellularGatewayUplink(self, cellularGateways, **kwargs):
        """
        **Returns the uplink settings for your MG network.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-cellular-gateway-uplink

        cellularGateway: (list) List containing one or more cellularGateway (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkcellulargatewayuplink(
                cellularGateways= cellularGateways,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationCellularGatewayUplinkStatuses(self, cellularGateways, **kwargs):
        """
        **List the uplink status of every Meraki MG cellular gateway in the organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-cellular-gateway-uplink-statuses

        cellularGateway: (list) List containing one or more cellularGateway (dict).  Each nested dict must include following required keys/values:
            - organizationId (string): Organization ID (required)
        
        The following optional paramaters can be passed directly to the class as arguments:
            - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. (optional)
            - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - networkIds (array): A list of network IDs. The returned devices will be filtered to only include these networks. (optional)
            - serials (array): A list of serial numbers. The returned devices will be filtered to only include these serials. (optional)
            - iccids (array): A list of ICCIDs. The returned devices will be filtered to only include these ICCIDs. (optional)
            - total_pages (integer or string): (defaults to "all") use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages (optional)
            - direction (string): direction to paginate, either "next" (default) or "prev" page (optional)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationcellulargatewayuplinkstatuses(
                cellularGateways= cellularGateways,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

