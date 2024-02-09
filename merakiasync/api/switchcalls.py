import asyncio

import merakiasync.asynctasks.switchtasks as async_tasks

class Switch:
    def __init__(self, apikey, debug_dict):
        self._apikey = apikey
        self._debug_dict = debug_dict
        self._loop = asyncio.get_event_loop()

    def AsyncGetDeviceSwitchPorts(self, switches, **kwargs):
        """
        **List the switch ports for a switch**
        https://developer.cisco.com/meraki/api-v1/#!get-device-switch-ports

        switch: (list) List containing one or more switch (dict).  Each nested dict can include the following required and/or optional keys/values:
            - serial (string): Serial (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getdeviceswitchports(
                switches= switches,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetDeviceSwitchPortsStatuses(self, switches, **kwargs):
        """
        **Return the status for all the ports of a switch**
        https://developer.cisco.com/meraki/api-v1/#!get-device-switch-ports-statuses

        switch: (list) List containing one or more switch (dict).  Each nested dict can include the following required and/or optional keys/values:
            - serial (string): Serial (required)

        These additional time based paramaters can be passed in directly to the class:
            - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day. (optional)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getdeviceswitchportsstatuses(
                switches= switches,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetDeviceSwitchPortsStatusesPackets(self, switches, **kwargs):
        """
        **Return the packet counters for all the ports of a switch**
        https://developer.cisco.com/meraki/api-v1/#!get-device-switch-ports-statuses-packets

        switch: (list) List containing one or more switch (dict).  Each nested dict can include the following required and/or optional keys/values:
            - serial (string): Serial (required)

        These additional time based paramaters can be passed in directly to the class:
            - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 1 day from today. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 1 day. The default is 1 day. (optional)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getdeviceswitchportsstatusespackets(
                switches= switches,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetDeviceSwitchPort(self, switches, **kwargs):
        """
        **Return a switch port**
        https://developer.cisco.com/meraki/api-v1/#!get-device-switch-port

        switch: (list) List containing one or more switch (dict).  Each nested dict can include the following required and/or optional keys/values:
            - serial (string): Serial (required)
            - portId (string): Port ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getdeviceswitchport(
                switches= switches,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetDeviceSwitchRoutingInterfaces(self, switches, **kwargs):
        """
        **List layer 3 interfaces for a switch. Those for a stack may be found under switch stack routing.**
        https://developer.cisco.com/meraki/api-v1/#!get-device-switch-routing-interfaces

        switch: (list) List containing one or more switch (dict).  Each nested dict can include the following required and/or optional keys/values:
            - serial (string): Serial (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getdeviceswitchroutinginterfaces(
                switches= switches,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetDeviceSwitchRoutingInterface(self, switches, **kwargs):
        """
        **Return a layer 3 interface for a switch**
        https://developer.cisco.com/meraki/api-v1/#!get-device-switch-routing-interface

        switch: (list) List containing one or more switch (dict).  Each nested dict can include the following required and/or optional keys/values:
            - serial (string): Serial (required)
            - interfaceId (string): Interface ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getdeviceswitchroutinginterface(
                switches= switches,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetDeviceSwitchRoutingInterfaceDhcp(self, switches, **kwargs):
        """
        **Return a layer 3 interface DHCP configuration for a switch**
        https://developer.cisco.com/meraki/api-v1/#!get-device-switch-routing-interface-dhcp

        switch: (list) List containing one or more switch (dict).  Each nested dict can include the following required and/or optional keys/values:
            - serial (string): Serial (required)
            - interfaceId (string): Interface ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getdeviceswitchroutinginterfacedhcp(
                switches= switches,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetDeviceSwitchRoutingStaticRoutes(self, switches, **kwargs):
        """
        **List layer 3 static routes for a switch**
        https://developer.cisco.com/meraki/api-v1/#!get-device-switch-routing-static-routes

        switch: (list) List containing one or more switch (dict).  Each nested dict can include the following required and/or optional keys/values:
            - serial (string): Serial (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getdeviceswitchroutingstaticroutes(
                switches= switches,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetDeviceSwitchRoutingStaticRoute(self, switches, **kwargs):
        """
        **Return a layer 3 static route for a switch**
        https://developer.cisco.com/meraki/api-v1/#!get-device-switch-routing-static-route

        switch: (list) List containing one or more switch (dict).  Each nested dict can include the following required and/or optional keys/values:
            - serial (string): Serial (required)
            - staticRouteId (string): Static route ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getdeviceswitchroutingstaticroute(
                switches= switches,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetDeviceSwitchWarmSpare(self, switches, **kwargs):
        """
        **Return warm spare configuration for a switch**
        https://developer.cisco.com/meraki/api-v1/#!get-device-switch-warm-spare

        switch: (list) List containing one or more switch (dict).  Each nested dict can include the following required and/or optional keys/values:
            - serial (string): Serial (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getdeviceswitchwarmspare(
                switches= switches,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkSwitchAccessControlLists(self, switches, **kwargs):
        """
        **Return the access control lists for a MS network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-access-control-lists

        switch: (list) List containing one or more switch (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkswitchaccesscontrollists(
                switches= switches,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkSwitchAccessPolicies(self, switches, **kwargs):
        """
        **List the access policies for a switch network. Only returns access policies with 'my RADIUS server' as authentication method**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-access-policies

        switch: (list) List containing one or more switch (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkswitchaccesspolicies(
                switches= switches,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkSwitchAccessPolicy(self, switches, **kwargs):
        """
        **Return a specific access policy for a switch network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-access-policy

        switch: (list) List containing one or more switch (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)
            - accessPolicyNumber (string): Access policy number (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkswitchaccesspolicy(
                switches= switches,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkSwitchAlternateManagementInterface(self, switches, **kwargs):
        """
        **Return the switch alternate management interface for the network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-alternate-management-interface

        switch: (list) List containing one or more switch (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkswitchalternatemanagementinterface(
                switches= switches,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkSwitchDhcpV4ServersSeen(self, switches, **kwargs):
        """
        **Return the network's DHCPv4 servers seen within the selected timeframe (default 1 day)**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-dhcp-v-4-servers-seen

        switch: (list) List containing one or more switch (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)

        These additional time based paramaters can be passed in directly to the class:
            - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day. (optional)
            - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. (optional)
            - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkswitchdhcpv4serversseen(
                switches= switches,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkSwitchDhcpServerPolicy(self, switches, **kwargs):
        """
        **Return the DHCP server settings. Blocked/allowed servers are only applied when default policy is allow/block, respectively**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-dhcp-server-policy

        switch: (list) List containing one or more switch (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkswitchdhcpserverpolicy(
                switches= switches,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers(self, switches, **kwargs):
        """
        **Return the list of servers trusted by Dynamic ARP Inspection on this network. These are also known as allow listed snoop entries**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-dhcp-server-policy-arp-inspection-trusted-servers

        switch: (list) List containing one or more switch (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)

        These additional time based paramaters can be passed in directly to the class:
            - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. (optional)
            - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkswitchdhcpserverpolicyarpinspectiontrustedservers(
                switches= switches,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice(self, switches, **kwargs):
        """
        **Return the devices that have a Dynamic ARP Inspection warning and their warnings**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-dhcp-server-policy-arp-inspection-warnings-by-device

        switch: (list) List containing one or more switch (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)

        These additional time based paramaters can be passed in directly to the class:
            - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. (optional)
            - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkswitchdhcpserverpolicyarpinspectionwarningsbydevice(
                switches= switches,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkSwitchDscpToCosMappings(self, switches, **kwargs):
        """
        **Return the DSCP to CoS mappings**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-dscp-to-cos-mappings

        switch: (list) List containing one or more switch (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkswitchdscptocosmappings(
                switches= switches,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkSwitchLinkAggregations(self, switches, **kwargs):
        """
        **List link aggregation groups**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-link-aggregations

        switch: (list) List containing one or more switch (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkswitchlinkaggregations(
                switches= switches,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkSwitchMtu(self, switches, **kwargs):
        """
        **Return the MTU configuration**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-mtu

        switch: (list) List containing one or more switch (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkswitchmtu(
                switches= switches,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkSwitchPortSchedules(self, switches, **kwargs):
        """
        **List switch port schedules**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-port-schedules

        switch: (list) List containing one or more switch (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkswitchportschedules(
                switches= switches,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkSwitchQosRules(self, switches, **kwargs):
        """
        **List quality of service rules**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-qos-rules

        switch: (list) List containing one or more switch (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkswitchqosrules(
                switches= switches,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkSwitchQosRulesOrder(self, switches, **kwargs):
        """
        **Return the quality of service rule IDs by order in which they will be processed by the switch**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-qos-rules-order

        switch: (list) List containing one or more switch (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkswitchqosrulesorder(
                switches= switches,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkSwitchQosRule(self, switches, **kwargs):
        """
        **Return a quality of service rule**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-qos-rule

        switch: (list) List containing one or more switch (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)
            - qosRuleId (string): Qos rule ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkswitchqosrule(
                switches= switches,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkSwitchRoutingMulticast(self, switches, **kwargs):
        """
        **Return multicast settings for a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-routing-multicast

        switch: (list) List containing one or more switch (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkswitchroutingmulticast(
                switches= switches,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkSwitchRoutingMulticastRendezvousPoints(self, switches, **kwargs):
        """
        **List multicast rendezvous points**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-routing-multicast-rendezvous-points

        switch: (list) List containing one or more switch (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkswitchroutingmulticastrendezvouspoints(
                switches= switches,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkSwitchRoutingMulticastRendezvousPoint(self, switches, **kwargs):
        """
        **Return a multicast rendezvous point**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-routing-multicast-rendezvous-point

        switch: (list) List containing one or more switch (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)
            - rendezvousPointId (string): Rendezvous point ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkswitchroutingmulticastrendezvouspoint(
                switches= switches,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkSwitchRoutingOspf(self, switches, **kwargs):
        """
        **Return layer 3 OSPF routing configuration**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-routing-ospf

        switch: (list) List containing one or more switch (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkswitchroutingospf(
                switches= switches,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkSwitchSettings(self, switches, **kwargs):
        """
        **Returns the switch network settings**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-settings

        switch: (list) List containing one or more switch (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkswitchsettings(
                switches= switches,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkSwitchStacks(self, switches, **kwargs):
        """
        **List the switch stacks in a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-stacks

        switch: (list) List containing one or more switch (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkswitchstacks(
                switches= switches,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkSwitchStack(self, switches, **kwargs):
        """
        **Show a switch stack**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-stack

        switch: (list) List containing one or more switch (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)
            - switchStackId (string): Switch stack ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkswitchstack(
                switches= switches,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkSwitchStackRoutingInterfaces(self, switches, **kwargs):
        """
        **List layer 3 interfaces for a switch stack**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-stack-routing-interfaces

        switch: (list) List containing one or more switch (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)
            - switchStackId (string): Switch stack ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkswitchstackroutinginterfaces(
                switches= switches,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkSwitchStackRoutingInterface(self, switches, **kwargs):
        """
        **Return a layer 3 interface from a switch stack**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-stack-routing-interface

        switch: (list) List containing one or more switch (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)
            - switchStackId (string): Switch stack ID (required)
            - interfaceId (string): Interface ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkswitchstackroutinginterface(
                switches= switches,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkSwitchStackRoutingInterfaceDhcp(self, switches, **kwargs):
        """
        **Return a layer 3 interface DHCP configuration for a switch stack**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-stack-routing-interface-dhcp

        switch: (list) List containing one or more switch (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)
            - switchStackId (string): Switch stack ID (required)
            - interfaceId (string): Interface ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkswitchstackroutinginterfacedhcp(
                switches= switches,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkSwitchStackRoutingStaticRoutes(self, switches, **kwargs):
        """
        **List layer 3 static routes for a switch stack**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-stack-routing-static-routes

        switch: (list) List containing one or more switch (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)
            - switchStackId (string): Switch stack ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkswitchstackroutingstaticroutes(
                switches= switches,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkSwitchStackRoutingStaticRoute(self, switches, **kwargs):
        """
        **Return a layer 3 static route for a switch stack**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-stack-routing-static-route

        switch: (list) List containing one or more switch (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)
            - switchStackId (string): Switch stack ID (required)
            - staticRouteId (string): Static route ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkswitchstackroutingstaticroute(
                switches= switches,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkSwitchStormControl(self, switches, **kwargs):
        """
        **Return the storm control configuration for a switch network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-storm-control

        switch: (list) List containing one or more switch (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkswitchstormcontrol(
                switches= switches,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkSwitchStp(self, switches, **kwargs):
        """
        **Returns STP settings**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-stp

        switch: (list) List containing one or more switch (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkswitchstp(
                switches= switches,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationConfigTemplateSwitchProfiles(self, switches, **kwargs):
        """
        **List the switch templates for your switch template configuration**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-config-template-switch-profiles

        switch: (list) List containing one or more switch (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)
            - configTemplateId (string): Config template ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationconfigtemplateswitchprofiles(
                switches= switches,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationConfigTemplateSwitchProfilePorts(self, switches, **kwargs):
        """
        **Return all the ports of a switch template**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-config-template-switch-profile-ports

        switch: (list) List containing one or more switch (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)
            - configTemplateId (string): Config template ID (required)
            - profileId (string): Profile ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationconfigtemplateswitchprofileports(
                switches= switches,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationConfigTemplateSwitchProfilePort(self, switches, **kwargs):
        """
        **Return a switch template port**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-config-template-switch-profile-port

        switch: (list) List containing one or more switch (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)
            - configTemplateId (string): Config template ID (required)
            - profileId (string): Profile ID (required)
            - portId (string): Port ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationconfigtemplateswitchprofileport(
                switches= switches,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationSwitchPortsBySwitch(self, switches, **kwargs):
        """
        **List the switchports in an organization by switch**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-ports-by-switch

        switch: (list) List containing one or more switch (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)
            - networkIds (array): Optional parameter to filter switchports by network. (optional)
            - portProfileIds (array): Optional parameter to filter switchports belonging to the specified port profiles. (optional)
            - name (string): Optional parameter to filter switchports belonging to switches by name. All returned switches will have a name that contains the search term or is an exact match. (optional)
            - mac (string): Optional parameter to filter switchports belonging to switches by MAC address. All returned switches will have a MAC address that contains the search term or is an exact match. (optional)
            - macs (array): Optional parameter to filter switchports by one or more MAC addresses belonging to devices. All switchports returned belong to MAC addresses of switches that are an exact match. (optional)
            - serial (string): Optional parameter to filter switchports belonging to switches by serial number. All returned switches will have a serial number that contains the search term or is an exact match. (optional)
            - serials (array): Optional parameter to filter switchports belonging to switches with one or more serial numbers. All switchports returned belong to serial numbers of switches that are an exact match. (optional)
            - configurationUpdatedAfter (string): Optional parameter to filter results by switches where the configuration has been updated after the given timestamp. (optional)

        These additional time based paramaters can be passed in directly to the class:
            - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 50. Default is 50. (optional)
            - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationswitchportsbyswitch(
                switches= switches,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

