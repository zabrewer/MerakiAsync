import asyncio

import merakiasync.asynctasks.appliancetasks as async_tasks

class Appliance:
    def __init__(self, apikey, debug_dict):
        self._apikey = apikey
        self._debug_dict = debug_dict
        self._loop = asyncio.get_event_loop()

    def AsyncGetDeviceApplianceDhcpSubnets(self, appliances, **kwargs):
        """
        **Return the DHCP subnet information for an appliance**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-dhcp-subnets

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - serial (string): Serial (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getdeviceappliancedhcpsubnets(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetDeviceAppliancePerformance(self, appliances, **kwargs):
        """
        **Return the performance score for a single MX. Only primary MX devices supported. If no data is available, a 204 error code is returned.**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-performance

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - serial (string): Serial (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getdeviceapplianceperformance(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetDeviceAppliancePrefixesDelegated(self, appliances, **kwargs):
        """
        **Return current delegated IPv6 prefixes on an appliance.**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-prefixes-delegated

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - serial (string): Serial (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getdeviceapplianceprefixesdelegated(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetDeviceAppliancePrefixesDelegatedVlanAssignments(self, appliances, **kwargs):
        """
        **Return prefixes assigned to all IPv6 enabled VLANs on an appliance.**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-prefixes-delegated-vlan-assignments

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - serial (string): Serial (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getdeviceapplianceprefixesdelegatedvlanassignments(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetDeviceApplianceRadioSettings(self, appliances, **kwargs):
        """
        **Return the radio settings of an appliance**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-radio-settings

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - serial (string): Serial (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getdeviceapplianceradiosettings(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetDeviceApplianceUplinksSettings(self, appliances, **kwargs):
        """
        **Return the uplink settings for an MX appliance**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-uplinks-settings

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - serial (string): Serial (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getdeviceapplianceuplinkssettings(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkApplianceClientSecurityEvents(self, appliances, **kwargs):
        """
        **List the security events for a client. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-client-security-events

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)
            - clientId (string): Client ID (required)

        These additional time based paramaters can be passed in directly to the class:
            - t0 (string): The beginning of the timespan for the data. Data is gathered after the specified t0 value. The maximum lookback period is 791 days from today. (optional)
            - t1 (string): The end of the timespan for the data. t1 can be a maximum of 791 days after t0. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 791 days. The default is 31 days. (optional)
            - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100. (optional)
            - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - sortOrder (string): Sorted order of security events based on event detection time. Order options are 'ascending' or 'descending'. Default is ascending order. (optional)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkapplianceclientsecurityevents(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkApplianceConnectivityMonitoringDestinations(self, appliances, **kwargs):
        """
        **Return the connectivity testing destinations for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-connectivity-monitoring-destinations

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkapplianceconnectivitymonitoringdestinations(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkApplianceContentFiltering(self, appliances, **kwargs):
        """
        **Return the content filtering settings for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-content-filtering

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkappliancecontentfiltering(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkApplianceContentFilteringCategories(self, appliances, **kwargs):
        """
        **List all available content filtering categories for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-content-filtering-categories

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkappliancecontentfilteringcategories(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkApplianceFirewallCellularFirewallRules(self, appliances, **kwargs):
        """
        **Return the cellular firewall rules for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-cellular-firewall-rules

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkappliancefirewallcellularfirewallrules(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkApplianceFirewallFirewalledServices(self, appliances, **kwargs):
        """
        **List the appliance services and their accessibility rules**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-firewalled-services

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkappliancefirewallfirewalledservices(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkApplianceFirewallFirewalledService(self, appliances, **kwargs):
        """
        **Return the accessibility settings of the given service ('ICMP', 'web', or 'SNMP')**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-firewalled-service

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)
            - service (string): Service (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkappliancefirewallfirewalledservice(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkApplianceFirewallInboundCellularFirewallRules(self, appliances, **kwargs):
        """
        **Return the inbound cellular firewall rules for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-inbound-cellular-firewall-rules

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkappliancefirewallinboundcellularfirewallrules(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkApplianceFirewallInboundFirewallRules(self, appliances, **kwargs):
        """
        **Return the inbound firewall rules for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-inbound-firewall-rules

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkappliancefirewallinboundfirewallrules(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkApplianceFirewallL3FirewallRules(self, appliances, **kwargs):
        """
        **Return the L3 firewall rules for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-l-3-firewall-rules

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkappliancefirewalll3firewallrules(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkApplianceFirewallL7FirewallRules(self, appliances, **kwargs):
        """
        **List the MX L7 firewall rules for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-l-7-firewall-rules

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkappliancefirewalll7firewallrules(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkApplianceFirewallL7FirewallRulesApplicationCategories(self, appliances, **kwargs):
        """
        **Return the L7 firewall application categories and their associated applications for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-l-7-firewall-rules-application-categories

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkappliancefirewalll7firewallrulesapplicationcategories(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkApplianceFirewallOneToManyNatRules(self, appliances, **kwargs):
        """
        **Return the 1:Many NAT mapping rules for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-one-to-many-nat-rules

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkappliancefirewallonetomanynatrules(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkApplianceFirewallOneToOneNatRules(self, appliances, **kwargs):
        """
        **Return the 1:1 NAT mapping rules for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-one-to-one-nat-rules

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkappliancefirewallonetoonenatrules(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkApplianceFirewallPortForwardingRules(self, appliances, **kwargs):
        """
        **Return the port forwarding rules for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-port-forwarding-rules

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkappliancefirewallportforwardingrules(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkApplianceFirewallSettings(self, appliances, **kwargs):
        """
        **Return the firewall settings for this network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-settings

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkappliancefirewallsettings(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkAppliancePorts(self, appliances, **kwargs):
        """
        **List per-port VLAN settings for all ports of a MX.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-ports

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkapplianceports(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkAppliancePort(self, appliances, **kwargs):
        """
        **Return per-port VLAN settings for a single MX port.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-port

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)
            - portId (string): Port ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkapplianceport(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkAppliancePrefixesDelegatedStatics(self, appliances, **kwargs):
        """
        **List static delegated prefixes for a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-prefixes-delegated-statics

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkapplianceprefixesdelegatedstatics(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkAppliancePrefixesDelegatedStatic(self, appliances, **kwargs):
        """
        **Return a static delegated prefix from a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-prefixes-delegated-static

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)
            - staticDelegatedPrefixId (string): Static delegated prefix ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkapplianceprefixesdelegatedstatic(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkApplianceRfProfiles(self, appliances, **kwargs):
        """
        **List the RF profiles for this network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-rf-profiles

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkappliancerfprofiles(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkApplianceRfProfile(self, appliances, **kwargs):
        """
        **Return a RF profile**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-rf-profile

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)
            - rfProfileId (string): Rf profile ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkappliancerfprofile(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkApplianceSecurityEvents(self, appliances, **kwargs):
        """
        **List the security events for a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-security-events

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)

        These additional time based paramaters can be passed in directly to the class:
            - t0 (string): The beginning of the timespan for the data. Data is gathered after the specified t0 value. The maximum lookback period is 365 days from today. (optional)
            - t1 (string): The end of the timespan for the data. t1 can be a maximum of 365 days after t0. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 365 days. The default is 31 days. (optional)
            - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100. (optional)
            - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - sortOrder (string): Sorted order of security events based on event detection time. Order options are 'ascending' or 'descending'. Default is ascending order. (optional)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkappliancesecurityevents(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkApplianceSecurityIntrusion(self, appliances, **kwargs):
        """
        **Returns all supported intrusion settings for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-security-intrusion

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkappliancesecurityintrusion(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkApplianceSecurityMalware(self, appliances, **kwargs):
        """
        **Returns all supported malware settings for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-security-malware

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkappliancesecuritymalware(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkApplianceSettings(self, appliances, **kwargs):
        """
        **Return the appliance settings for a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-settings

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkappliancesettings(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkApplianceSingleLan(self, appliances, **kwargs):
        """
        **Return single LAN configuration**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-single-lan

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkappliancesinglelan(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkApplianceSsids(self, appliances, **kwargs):
        """
        **List the MX SSIDs in a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-ssids

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkappliancessids(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkApplianceSsid(self, appliances, **kwargs):
        """
        **Return a single MX SSID**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-ssid

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)
            - number (string): Number (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkappliancessid(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkApplianceStaticRoutes(self, appliances, **kwargs):
        """
        **List the static routes for an MX or teleworker network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-static-routes

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkappliancestaticroutes(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkApplianceStaticRoute(self, appliances, **kwargs):
        """
        **Return a static route for an MX or teleworker network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-static-route

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)
            - staticRouteId (string): Static route ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkappliancestaticroute(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkApplianceTrafficShaping(self, appliances, **kwargs):
        """
        **Display the traffic shaping settings for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-traffic-shaping

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkappliancetrafficshaping(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkApplianceTrafficShapingCustomPerformanceClasses(self, appliances, **kwargs):
        """
        **List all custom performance classes for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-traffic-shaping-custom-performance-classes

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkappliancetrafficshapingcustomperformanceclasses(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkApplianceTrafficShapingCustomPerformanceClass(self, appliances, **kwargs):
        """
        **Return a custom performance class for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-traffic-shaping-custom-performance-class

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)
            - customPerformanceClassId (string): Custom performance class ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkappliancetrafficshapingcustomperformanceclass(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkApplianceTrafficShapingRules(self, appliances, **kwargs):
        """
        **Display the traffic shaping settings rules for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-traffic-shaping-rules

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkappliancetrafficshapingrules(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkApplianceTrafficShapingUplinkBandwidth(self, appliances, **kwargs):
        """
        **Returns the uplink bandwidth limits for your MX network. This may not reflect the affected device's hardware capabilities.  For more information on your device's hardware capabilities, please consult our MX Family Datasheet - [https://meraki.cisco.com/product-collateral/mx-family-datasheet/?file]**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-traffic-shaping-uplink-bandwidth

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkappliancetrafficshapinguplinkbandwidth(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkApplianceTrafficShapingUplinkSelection(self, appliances, **kwargs):
        """
        **Show uplink selection settings for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-traffic-shaping-uplink-selection

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkappliancetrafficshapinguplinkselection(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkApplianceUplinksUsageHistory(self, appliances, **kwargs):
        """
        **Get the sent and received bytes for each uplink of a network.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-uplinks-usage-history

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)

        These additional time based paramaters can be passed in directly to the class:
            - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 365 days from today. (optional)
            - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 10 minutes. (optional)
            - resolution (integer): The time resolution in seconds for returned data. The valid resolutions are: 60, 300, 600, 1800, 3600, 86400. The default is 60. (optional)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkapplianceuplinksusagehistory(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkApplianceVlans(self, appliances, **kwargs):
        """
        **List the VLANs for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-vlans

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkappliancevlans(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkApplianceVlansSettings(self, appliances, **kwargs):
        """
        **Returns the enabled status of VLANs for the network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-vlans-settings

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkappliancevlanssettings(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkApplianceVlan(self, appliances, **kwargs):
        """
        **Return a VLAN**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-vlan

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)
            - vlanId (string): Vlan ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkappliancevlan(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkApplianceVpnBgp(self, appliances, **kwargs):
        """
        **Return a Hub BGP Configuration**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-vpn-bgp

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkappliancevpnbgp(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkApplianceVpnSiteToSiteVpn(self, appliances, **kwargs):
        """
        **Return the site-to-site VPN settings of a network. Only valid for MX networks.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-vpn-site-to-site-vpn

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkappliancevpnsitetositevpn(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetNetworkApplianceWarmSpare(self, appliances, **kwargs):
        """
        **Return MX warm spare settings**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-warm-spare

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - networkId (string): Network ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkappliancewarmspare(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationApplianceSecurityEvents(self, appliances, **kwargs):
        """
        **List the security events for an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-security-events

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)

        These additional time based paramaters can be passed in directly to the class:
            - t0 (string): The beginning of the timespan for the data. Data is gathered after the specified t0 value. The maximum lookback period is 365 days from today. (optional)
            - t1 (string): The end of the timespan for the data. t1 can be a maximum of 365 days after t0. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 365 days. The default is 31 days. (optional)
            - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100. (optional)
            - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - sortOrder (string): Sorted order of security events based on event detection time. Order options are 'ascending' or 'descending'. Default is ascending order. (optional)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationappliancesecurityevents(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationApplianceSecurityIntrusion(self, appliances, **kwargs):
        """
        **Returns all supported intrusion settings for an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-security-intrusion

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationappliancesecurityintrusion(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationApplianceTrafficShapingVpnExclusionsByNetwork(self, appliances, **kwargs):
        """
        **Display VPN exclusion rules for MX networks.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-traffic-shaping-vpn-exclusions-by-network

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)
            - networkIds (array): Optional parameter to filter the results by network IDs (optional)

        These additional time based paramaters can be passed in directly to the class:
            - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 50. (optional)
            - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationappliancetrafficshapingvpnexclusionsbynetwork(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationApplianceUplinkStatuses(self, appliances, **kwargs):
        """
        **List the uplink status of every Meraki MX and Z series appliances in the organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-uplink-statuses

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)
            - networkIds (array): A list of network IDs. The returned devices will be filtered to only include these networks. (optional)
            - serials (array): A list of serial numbers. The returned devices will be filtered to only include these serials. (optional)
            - iccids (array): A list of ICCIDs. The returned devices will be filtered to only include these ICCIDs. (optional)

        These additional time based paramaters can be passed in directly to the class:
            - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. (optional)
            - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationapplianceuplinkstatuses(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationApplianceUplinksUsageByNetwork(self, appliances, **kwargs):
        """
        **Get the sent and received bytes for each uplink of all MX and Z networks within an organization. If more than one device was active during the specified timespan, then the sent and received bytes will be aggregated by interface.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-uplinks-usage-by-network

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)

        These additional time based paramaters can be passed in directly to the class:
            - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 365 days from today. (optional)
            - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 14 days. The default is 1 day. (optional)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationapplianceuplinksusagebynetwork(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationApplianceVpnStats(self, appliances, **kwargs):
        """
        **Show VPN history stat for networks in an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-vpn-stats

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)
            - networkIds (array): A list of Meraki network IDs to filter results to contain only specified networks. E.g.: networkIds[]=N_12345678&networkIds[]=L_3456 (optional)

        These additional time based paramaters can be passed in directly to the class:
            - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 300. Default is 300. (optional)
            - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today. (optional)
            - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day. (optional)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationappliancevpnstats(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationApplianceVpnStatuses(self, appliances, **kwargs):
        """
        **Show VPN status for networks in an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-vpn-statuses

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)
            - networkIds (array): A list of Meraki network IDs to filter results to contain only specified networks. E.g.: networkIds[]=N_12345678&networkIds[]=L_3456 (optional)

        These additional time based paramaters can be passed in directly to the class:
            - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 300. Default is 300. (optional)
            - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationappliancevpnstatuses(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationApplianceVpnThirdPartyVPNPeers(self, appliances, **kwargs):
        """
        **Return the third party VPN peers for an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-vpn-third-party-v-p-n-peers

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationappliancevpnthirdpartyvpnpeers(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationApplianceVpnVpnFirewallRules(self, appliances, **kwargs):
        """
        **Return the firewall rules for an organization's site-to-site VPN**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-vpn-vpn-firewall-rules

        appliance: (list) List containing one or more appliance (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationappliancevpnvpnfirewallrules(
                appliances= appliances,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

