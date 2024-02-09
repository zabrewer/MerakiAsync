import asyncio

import merakiasync.asynctasks.organizationstasks as async_tasks

class Organizations:
    def __init__(self, apikey, debug_dict):
        self._apikey = apikey
        self._debug_dict = debug_dict
        self._loop = asyncio.get_event_loop()

    def AsyncGetOrganizations(self):
        """
        **List the organizations that the user has privileges on**
        https://developer.cisco.com/meraki/api-v1/#!get-organizations


        """

        return self._loop.run_until_complete(
            async_tasks._async_getorganizations(
                apikey=self._apikey,
                debug_dict=self._debug_dict,
            ))

    def AsyncGetOrganization(self, organizations, **kwargs):
        """
        **Return an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganization(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationActionBatches(self, organizations, **kwargs):
        """
        **Return the list of action batches in the organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-action-batches

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)
            - status (string): Filter batches by status. Valid types are pending, completed, and failed. (optional)

        These additional time based paramaters can be passed in directly to the class:

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationactionbatches(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationActionBatch(self, organizations, **kwargs):
        """
        **Return an action batch**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-action-batch

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)
            - actionBatchId (string): Action batch ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationactionbatch(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationAdaptivePolicyAcls(self, organizations, **kwargs):
        """
        **List adaptive policy ACLs in a organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-adaptive-policy-acls

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationadaptivepolicyacls(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationAdaptivePolicyAcl(self, organizations, **kwargs):
        """
        **Returns the adaptive policy ACL information**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-adaptive-policy-acl

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)
            - aclId (string): Acl ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationadaptivepolicyacl(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationAdaptivePolicyGroups(self, organizations, **kwargs):
        """
        **List adaptive policy groups in a organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-adaptive-policy-groups

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationadaptivepolicygroups(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationAdaptivePolicyGroup(self, organizations, **kwargs):
        """
        **Returns an adaptive policy group**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-adaptive-policy-group

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)
            - id (string): ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationadaptivepolicygroup(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationAdaptivePolicyOverview(self, organizations, **kwargs):
        """
        **Returns adaptive policy aggregate statistics for an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-adaptive-policy-overview

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationadaptivepolicyoverview(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationAdaptivePolicyPolicies(self, organizations, **kwargs):
        """
        **List adaptive policies in an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-adaptive-policy-policies

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationadaptivepolicypolicies(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationAdaptivePolicyPolicy(self, organizations, **kwargs):
        """
        **Return an adaptive policy**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-adaptive-policy-policy

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)
            - id (string): ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationadaptivepolicypolicy(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationAdaptivePolicySettings(self, organizations, **kwargs):
        """
        **Returns global adaptive policy settings in an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-adaptive-policy-settings

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationadaptivepolicysettings(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationAdmins(self, organizations, **kwargs):
        """
        **List the dashboard administrators in this organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-admins

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationadmins(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationAlertsProfiles(self, organizations, **kwargs):
        """
        **List all organization-wide alert configurations**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-alerts-profiles

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationalertsprofiles(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationApiRequests(self, organizations, **kwargs):
        """
        **List the API requests made by an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-api-requests

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)
            - adminId (string): Filter the results by the ID of the admin who made the API requests (optional)
            - path (string): Filter the results by the path of the API requests (optional)
            - method (string): Filter the results by the method of the API requests (must be 'GET', 'PUT', 'POST' or 'DELETE') (optional)
            - responseCode (integer): Filter the results by the response code of the API requests (optional)
            - sourceIp (string): Filter the results by the IP address of the originating API request (optional)
            - userAgent (string): Filter the results by the user agent string of the API request (optional)
            - version (integer): Filter the results by the API version of the API request (optional)
            - operationIds (array): Filter the results by one or more operation IDs for the API request (optional)

        These additional time based paramaters can be passed in directly to the class:
            - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today. (optional)
            - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 31 days. (optional)
            - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 50. (optional)
            - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationapirequests(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationApiRequestsOverview(self, organizations, **kwargs):
        """
        **Return an aggregated overview of API requests data**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-api-requests-overview

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)

        These additional time based paramaters can be passed in directly to the class:
            - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today. (optional)
            - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 31 days. (optional)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationapirequestsoverview(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationApiRequestsOverviewResponseCodesByInterval(self, organizations, **kwargs):
        """
        **Tracks organizations' API requests by response code across a given time period**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-api-requests-overview-response-codes-by-interval

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)
            - interval (integer): The time interval in seconds for returned data. The valid intervals are: 120, 3600, 14400, 21600. The default is 21600. Interval is calculated if time params are provided. (optional)
            - version (integer): Filter by API version of the endpoint. Allowable values are: [0, 1] (optional)
            - operationIds (array): Filter by operation ID of the endpoint (optional)
            - sourceIps (array): Filter by source IP that made the API request (optional)
            - adminIds (array): Filter by admin ID of user that made the API request (optional)
            - userAgent (string): Filter by user agent string for API request. This will filter by a complete or partial match. (optional)

        These additional time based paramaters can be passed in directly to the class:
            - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today. (optional)
            - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 31 days. If interval is provided, the timespan will be autocalculated. (optional)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationapirequestsoverviewresponsecodesbyinterval(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationBrandingPolicies(self, organizations, **kwargs):
        """
        **List the branding policies of an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-branding-policies

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationbrandingpolicies(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationBrandingPoliciesPriorities(self, organizations, **kwargs):
        """
        **Return the branding policy IDs of an organization in priority order. IDs are ordered in ascending order of priority (IDs later in the array have higher priority).**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-branding-policies-priorities

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationbrandingpoliciespriorities(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationBrandingPolicy(self, organizations, **kwargs):
        """
        **Return a branding policy**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-branding-policy

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)
            - brandingPolicyId (string): Branding policy ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationbrandingpolicy(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationClientsBandwidthUsageHistory(self, organizations, **kwargs):
        """
        **Return data usage (in megabits per second) over time for all clients in the given organization within a given time range.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-clients-bandwidth-usage-history

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)

        These additional time based paramaters can be passed in directly to the class:
            - t0 (string): The beginning of the timespan for the data. (optional)
            - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day. (optional)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationclientsbandwidthusagehistory(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationClientsOverview(self, organizations, **kwargs):
        """
        **Return summary information around client data usage (in mb) across the given organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-clients-overview

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)

        These additional time based paramaters can be passed in directly to the class:
            - t0 (string): The beginning of the timespan for the data. (optional)
            - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day. (optional)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationclientsoverview(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationClientsSearch(self, organizations, **kwargs):
        """
        **Return the client details in an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-clients-search

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)
            - mac (string): The MAC address of the client. Required. (required)

        These additional time based paramaters can be passed in directly to the class:
            - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 5. Default is 5. (optional)
            - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationclientssearch(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationConfigTemplates(self, organizations, **kwargs):
        """
        **List the configuration templates for this organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-config-templates

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationconfigtemplates(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationConfigTemplate(self, organizations, **kwargs):
        """
        **Return a single configuration template**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-config-template

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)
            - configTemplateId (string): Config template ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationconfigtemplate(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationConfigurationChanges(self, organizations, **kwargs):
        """
        **View the Change Log for your organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-configuration-changes

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)
            - networkId (string): Filters on the given network (optional)
            - adminId (string): Filters on the given Admin (optional)

        These additional time based paramaters can be passed in directly to the class:
            - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 365 days from today. (optional)
            - t1 (string): The end of the timespan for the data. t1 can be a maximum of 365 days after t0. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 365 days. The default is 365 days. (optional)
            - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 5000. Default is 5000. (optional)
            - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationconfigurationchanges(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationDevices(self, organizations, **kwargs):
        """
        **List the devices in an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)
            - configurationUpdatedAfter (string): Filter results by whether or not the device's configuration has been updated after the given timestamp (optional)
            - networkIds (array): Optional parameter to filter devices by network. (optional)
            - productTypes (array): Optional parameter to filter devices by product type. Valid types are wireless, appliance, switch, systemsManager, camera, cellularGateway, and sensor. (optional)
            - tags (array): Optional parameter to filter devices by tags. (optional)
            - tagsFilterType (string): Optional parameter of value 'withAnyTags' or 'withAllTags' to indicate whether to return networks which contain ANY or ALL of the included tags. If no type is included, 'withAnyTags' will be selected. (optional)
            - name (string): Optional parameter to filter devices by name. All returned devices will have a name that contains the search term or is an exact match. (optional)
            - mac (string): Optional parameter to filter devices by MAC address. All returned devices will have a MAC address that contains the search term or is an exact match. (optional)
            - serial (string): Optional parameter to filter devices by serial number. All returned devices will have a serial number that contains the search term or is an exact match. (optional)
            - model (string): Optional parameter to filter devices by model. All returned devices will have a model that contains the search term or is an exact match. (optional)
            - macs (array): Optional parameter to filter devices by one or more MAC addresses. All returned devices will have a MAC address that is an exact match. (optional)
            - serials (array): Optional parameter to filter devices by one or more serial numbers. All returned devices will have a serial number that is an exact match. (optional)
            - sensorMetrics (array): Optional parameter to filter devices by the metrics that they provide. Only applies to sensor devices. (optional)
            - sensorAlertProfileIds (array): Optional parameter to filter devices by the alert profiles that are bound to them. Only applies to sensor devices. (optional)
            - models (array): Optional parameter to filter devices by one or more models. All returned devices will have a model that is an exact match. (optional)

        These additional time based paramaters can be passed in directly to the class:
            - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. (optional)
            - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationdevices(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationDevicesAvailabilities(self, organizations, **kwargs):
        """
        **List the availability information for devices in an organization. The data returned by this endpoint is updated every 5 minutes.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-availabilities

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)
            - networkIds (array): Optional parameter to filter device availabilities by network ID. This filter uses multiple exact matches. (optional)
            - productTypes (array): Optional parameter to filter device availabilities by device product types. This filter uses multiple exact matches. (optional)
            - serials (array): Optional parameter to filter device availabilities by device serial numbers. This filter uses multiple exact matches. (optional)
            - tags (array): An optional parameter to filter devices by tags. The filtering is case-sensitive. If tags are included, 'tagsFilterType' should also be included (see below). This filter uses multiple exact matches. (optional)
            - tagsFilterType (string): An optional parameter of value 'withAnyTags' or 'withAllTags' to indicate whether to return devices which contain ANY or ALL of the included tags. If no type is included, 'withAnyTags' will be selected. (optional)

        These additional time based paramaters can be passed in directly to the class:
            - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. (optional)
            - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationdevicesavailabilities(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationDevicesAvailabilitiesChangeHistory(self, organizations, **kwargs):
        """
        **List the availability history information for devices in an organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-availabilities-change-history

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)
            - serials (array): Optional parameter to filter device availabilities history by device serial numbers (optional)
            - productTypes (array): Optional parameter to filter device availabilities history by device product types (optional)
            - networkIds (array): Optional parameter to filter device availabilities history by network IDs (optional)
            - statuses (array): Optional parameter to filter device availabilities history by device statuses (optional)

        These additional time based paramaters can be passed in directly to the class:
            - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. (optional)
            - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today. (optional)
            - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 14 days. The default is 1 day. (optional)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationdevicesavailabilitieschangehistory(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationDevicesPowerModulesStatusesByDevice(self, organizations, **kwargs):
        """
        **List the most recent status information for power modules in rackmount MX and MS devices that support them. The data returned by this endpoint is updated every 5 minutes.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-power-modules-statuses-by-device

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)
            - networkIds (array): Optional parameter to filter device availabilities by network ID. This filter uses multiple exact matches. (optional)
            - productTypes (array): Optional parameter to filter device availabilities by device product types. This filter uses multiple exact matches. (optional)
            - serials (array): Optional parameter to filter device availabilities by device serial numbers. This filter uses multiple exact matches. (optional)
            - tags (array): An optional parameter to filter devices by tags. The filtering is case-sensitive. If tags are included, 'tagsFilterType' should also be included (see below). This filter uses multiple exact matches. (optional)
            - tagsFilterType (string): An optional parameter of value 'withAnyTags' or 'withAllTags' to indicate whether to return devices which contain ANY or ALL of the included tags. If no type is included, 'withAnyTags' will be selected. (optional)

        These additional time based paramaters can be passed in directly to the class:
            - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. (optional)
            - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationdevicespowermodulesstatusesbydevice(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationDevicesProvisioningStatuses(self, organizations, **kwargs):
        """
        **List the provisioning statuses information for devices in an organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-provisioning-statuses

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)
            - networkIds (array): Optional parameter to filter device by network ID. This filter uses multiple exact matches. (optional)
            - productTypes (array): Optional parameter to filter device by device product types. This filter uses multiple exact matches. (optional)
            - serials (array): Optional parameter to filter device by device serial numbers. This filter uses multiple exact matches. (optional)
            - status (string): An optional parameter to filter devices by the provisioning status. Accepted statuses: unprovisioned, incomplete, complete. (optional)
            - tags (array): An optional parameter to filter devices by tags. The filtering is case-sensitive. If tags are included, 'tagsFilterType' should also be included (see below). This filter uses multiple exact matches. (optional)
            - tagsFilterType (string): An optional parameter of value 'withAnyTags' or 'withAllTags' to indicate whether to return devices which contain ANY or ALL of the included tags. If no type is included, 'withAnyTags' will be selected. (optional)

        These additional time based paramaters can be passed in directly to the class:
            - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. (optional)
            - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationdevicesprovisioningstatuses(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationDevicesStatuses(self, organizations, **kwargs):
        """
        **List the status of every Meraki device in the organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-statuses

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)
            - networkIds (array): Optional parameter to filter devices by network ids. (optional)
            - serials (array): Optional parameter to filter devices by serials. (optional)
            - statuses (array): Optional parameter to filter devices by statuses. Valid statuses are ["online", "alerting", "offline", "dormant"]. (optional)
            - productTypes (array): An optional parameter to filter device statuses by product type. Valid types are wireless, appliance, switch, systemsManager, camera, cellularGateway, and sensor. (optional)
            - models (array): Optional parameter to filter devices by models. (optional)
            - tags (array): An optional parameter to filter devices by tags. The filtering is case-sensitive. If tags are included, 'tagsFilterType' should also be included (see below). (optional)
            - tagsFilterType (string): An optional parameter of value 'withAnyTags' or 'withAllTags' to indicate whether to return devices which contain ANY or ALL of the included tags. If no type is included, 'withAnyTags' will be selected. (optional)

        These additional time based paramaters can be passed in directly to the class:
            - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. (optional)
            - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationdevicesstatuses(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationDevicesStatusesOverview(self, organizations, **kwargs):
        """
        **Return an overview of current device statuses**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-statuses-overview

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)
            - productTypes (array): An optional parameter to filter device statuses by product type. Valid types are wireless, appliance, switch, systemsManager, camera, cellularGateway, and sensor. (optional)
            - networkIds (array): An optional parameter to filter device statuses by network. (optional)

        These additional time based paramaters can be passed in directly to the class:

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationdevicesstatusesoverview(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationDevicesUplinksAddressesByDevice(self, organizations, **kwargs):
        """
        **List the current uplink addresses for devices in an organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-uplinks-addresses-by-device

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)
            - networkIds (array): Optional parameter to filter device uplinks by network ID. This filter uses multiple exact matches. (optional)
            - productTypes (array): Optional parameter to filter device uplinks by device product types. This filter uses multiple exact matches. (optional)
            - serials (array): Optional parameter to filter device availabilities by device serial numbers. This filter uses multiple exact matches. (optional)
            - tags (array): An optional parameter to filter devices by tags. The filtering is case-sensitive. If tags are included, 'tagsFilterType' should also be included (see below). This filter uses multiple exact matches. (optional)
            - tagsFilterType (string): An optional parameter of value 'withAnyTags' or 'withAllTags' to indicate whether to return devices which contain ANY or ALL of the included tags. If no type is included, 'withAnyTags' will be selected. (optional)

        These additional time based paramaters can be passed in directly to the class:
            - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. (optional)
            - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationdevicesuplinksaddressesbydevice(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationDevicesUplinksLossAndLatency(self, organizations, **kwargs):
        """
        **Return the uplink loss and latency for every MX in the organization from at latest 2 minutes ago**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-uplinks-loss-and-latency

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)
            - uplink (string): Optional filter for a specific WAN uplink. Valid uplinks are wan1, wan2, wan3, cellular. Default will return all uplinks. (optional)
            - ip (string): Optional filter for a specific destination IP. Default will return all destination IPs. (optional)

        These additional time based paramaters can be passed in directly to the class:
            - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 60 days from today. (optional)
            - t1 (string): The end of the timespan for the data. t1 can be a maximum of 5 minutes after t0. The latest possible time that t1 can be is 2 minutes into the past. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 5 minutes. The default is 5 minutes. (optional)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationdevicesuplinkslossandlatency(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationEarlyAccessFeatures(self, organizations, **kwargs):
        """
        **List the available early access features for organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-early-access-features

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationearlyaccessfeatures(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationEarlyAccessFeaturesOptIns(self, organizations, **kwargs):
        """
        **List the early access feature opt-ins for an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-early-access-features-opt-ins

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationearlyaccessfeaturesoptins(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationEarlyAccessFeaturesOptIn(self, organizations, **kwargs):
        """
        **Show an early access feature opt-in for an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-early-access-features-opt-in

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)
            - optInId (string): Opt in ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationearlyaccessfeaturesoptin(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationFirmwareUpgrades(self, organizations, **kwargs):
        """
        **Get firmware upgrade information for an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-firmware-upgrades

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)
            - status (array): Optional parameter to filter the upgrade by status. (optional)
            - productTypes (array): Optional parameter to filter the upgrade by product type. (optional)

        These additional time based paramaters can be passed in directly to the class:
            - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. (optional)
            - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationfirmwareupgrades(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationFirmwareUpgradesByDevice(self, organizations, **kwargs):
        """
        **Get firmware upgrade status for the filtered devices**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-firmware-upgrades-by-device

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)
            - networkIds (array): Optional parameter to filter by network (optional)
            - serials (array): Optional parameter to filter by serial number.  All returned devices will have a serial number that is an exact match. (optional)
            - macs (array): Optional parameter to filter by one or more MAC addresses belonging to devices. All devices returned belong to MAC addresses that are an exact match. (optional)
            - firmwareUpgradeBatchIds (array): Optional parameter to filter by firmware upgrade batch ids. (optional)
            - upgradeStatuses (array): Optional parameter to filter by firmware upgrade statuses. (optional)

        These additional time based paramaters can be passed in directly to the class:
            - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 50. (optional)
            - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationfirmwareupgradesbydevice(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationInventoryDevices(self, organizations, **kwargs):
        """
        **Return the device inventory for an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-inventory-devices

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)
            - usedState (string): Filter results by used or unused inventory. Accepted values are 'used' or 'unused'. (optional)
            - search (string): Search for devices in inventory based on serial number, mac address, or model. (optional)
            - macs (array): Search for devices in inventory based on mac addresses. (optional)
            - networkIds (array): Search for devices in inventory based on network ids. (optional)
            - serials (array): Search for devices in inventory based on serials. (optional)
            - models (array): Search for devices in inventory based on model. (optional)
            - orderNumbers (array): Search for devices in inventory based on order numbers. (optional)
            - tags (array): Filter devices by tags. The filtering is case-sensitive. If tags are included, 'tagsFilterType' should also be included (see below). (optional)
            - tagsFilterType (string): To use with 'tags' parameter, to filter devices which contain ANY or ALL given tags. Accepted values are 'withAnyTags' or 'withAllTags', default is 'withAnyTags'. (optional)
            - productTypes (array): Filter devices by product type. Accepted values are appliance, camera, cellularGateway, sensor, switch, systemsManager, and wireless. (optional)

        These additional time based paramaters can be passed in directly to the class:
            - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. (optional)
            - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationinventorydevices(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationInventoryDevice(self, organizations, **kwargs):
        """
        **Return a single device from the inventory of an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-inventory-device

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)
            - serial (string): Serial (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationinventorydevice(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationInventoryOnboardingCloudMonitoringImports(self, organizations, **kwargs):
        """
        **Check the status of a committed Import operation**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-inventory-onboarding-cloud-monitoring-imports

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)
            - importIds (array): import ids from an imports (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationinventoryonboardingcloudmonitoringimports(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationInventoryOnboardingCloudMonitoringNetworks(self, organizations, **kwargs):
        """
        **Returns list of networks eligible for adding cloud monitored device**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-inventory-onboarding-cloud-monitoring-networks

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)
            - deviceType (string): Device Type switch or wireless controller (required)

        These additional time based paramaters can be passed in directly to the class:
            - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100000. Default is 1000. (optional)
            - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationinventoryonboardingcloudmonitoringnetworks(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationLicenses(self, organizations, **kwargs):
        """
        **List the licenses for an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-licenses

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)
            - deviceSerial (string): Filter the licenses to those assigned to a particular device. Returned in the same order that they are queued to the device. (optional)
            - networkId (string): Filter the licenses to those assigned in a particular network (optional)
            - state (string): Filter the licenses to those in a particular state. Can be one of 'active', 'expired', 'expiring', 'recentlyQueued', 'unused' or 'unusedActive' (optional)

        These additional time based paramaters can be passed in directly to the class:
            - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. (optional)
            - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationlicenses(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationLicensesOverview(self, organizations, **kwargs):
        """
        **Return an overview of the license state for an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-licenses-overview

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationlicensesoverview(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationLicense(self, organizations, **kwargs):
        """
        **Display a license**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-license

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)
            - licenseId (string): License ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationlicense(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationLoginSecurity(self, organizations, **kwargs):
        """
        **Returns the login security settings for an organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-login-security

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationloginsecurity(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationNetworks(self, organizations, **kwargs):
        """
        **List the networks that the user has privileges on in an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-networks

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)
            - configTemplateId (string): An optional parameter that is the ID of a config template. Will return all networks bound to that template. (optional)
            - isBoundToConfigTemplate (boolean): An optional parameter to filter config template bound networks. If configTemplateId is set, this cannot be false. (optional)
            - tags (array): An optional parameter to filter networks by tags. The filtering is case-sensitive. If tags are included, 'tagsFilterType' should also be included (see below). (optional)
            - tagsFilterType (string): An optional parameter of value 'withAnyTags' or 'withAllTags' to indicate whether to return networks which contain ANY or ALL of the included tags. If no type is included, 'withAnyTags' will be selected. (optional)

        These additional time based paramaters can be passed in directly to the class:
            - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100000. Default is 1000. (optional)
            - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationnetworks(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationOpenapiSpec(self, organizations, **kwargs):
        """
        **Return the OpenAPI Specification of the organization's API documentation in JSON**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-openapi-spec

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)
            - version (integer): OpenAPI Specification version to return. Default is 2 (optional)

        These additional time based paramaters can be passed in directly to the class:

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationopenapispec(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationPolicyObjects(self, organizations, **kwargs):
        """
        **Lists Policy Objects belonging to the organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-policy-objects

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)

        These additional time based paramaters can be passed in directly to the class:
            - perPage (integer): The number of entries per page returned. Acceptable range is 10 - 5000. Default is 5000. (optional)
            - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationpolicyobjects(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationPolicyObjectsGroups(self, organizations, **kwargs):
        """
        **Lists Policy Object Groups belonging to the organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-policy-objects-groups

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)

        These additional time based paramaters can be passed in directly to the class:
            - perPage (integer): The number of entries per page returned. Acceptable range is 10 - 1000. Default is 1000. (optional)
            - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationpolicyobjectsgroups(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationPolicyObjectsGroup(self, organizations, **kwargs):
        """
        **Shows details of a Policy Object Group.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-policy-objects-group

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)
            - policyObjectGroupId (string): Policy object group ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationpolicyobjectsgroup(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationPolicyObject(self, organizations, **kwargs):
        """
        **Shows details of a Policy Object.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-policy-object

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)
            - policyObjectId (string): Policy object ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationpolicyobject(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationSaml(self, organizations, **kwargs):
        """
        **Returns the SAML SSO enabled settings for an organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-saml

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationsaml(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationSamlIdps(self, organizations, **kwargs):
        """
        **List the SAML IdPs in your organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-saml-idps

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationsamlidps(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationSamlIdp(self, organizations, **kwargs):
        """
        **Get a SAML IdP from your organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-saml-idp

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)
            - idpId (string): Idp ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationsamlidp(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationSamlRoles(self, organizations, **kwargs):
        """
        **List the SAML roles for this organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-saml-roles

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationsamlroles(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationSamlRole(self, organizations, **kwargs):
        """
        **Return a SAML role**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-saml-role

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)
            - samlRoleId (string): Saml role ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationsamlrole(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationSnmp(self, organizations, **kwargs):
        """
        **Return the SNMP settings for an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-snmp

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationsnmp(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationSummaryTopAppliancesByUtilization(self, organizations, **kwargs):
        """
        **Return the top 10 appliances sorted by utilization over given time range.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-summary-top-appliances-by-utilization

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)

        These additional time based paramaters can be passed in directly to the class:
            - t0 (string): The beginning of the timespan for the data. (optional)
            - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 25 minutes and be less than or equal to 31 days. The default is 1 day. (optional)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationsummarytopappliancesbyutilization(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationSummaryTopClientsByUsage(self, organizations, **kwargs):
        """
        **Return metrics for organization's top 10 clients by data usage (in mb) over given time range.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-summary-top-clients-by-usage

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)

        These additional time based paramaters can be passed in directly to the class:
            - t0 (string): The beginning of the timespan for the data. (optional)
            - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 8 hours and be less than or equal to 31 days. The default is 1 day. (optional)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationsummarytopclientsbyusage(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationSummaryTopClientsManufacturersByUsage(self, organizations, **kwargs):
        """
        **Return metrics for organization's top clients by data usage (in mb) over given time range, grouped by manufacturer.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-summary-top-clients-manufacturers-by-usage

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)

        These additional time based paramaters can be passed in directly to the class:
            - t0 (string): The beginning of the timespan for the data. (optional)
            - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day. (optional)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationsummarytopclientsmanufacturersbyusage(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationSummaryTopDevicesByUsage(self, organizations, **kwargs):
        """
        **Return metrics for organization's top 10 devices sorted by data usage over given time range. Default unit is megabytes.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-summary-top-devices-by-usage

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)

        These additional time based paramaters can be passed in directly to the class:
            - t0 (string): The beginning of the timespan for the data. (optional)
            - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 8 hours and be less than or equal to 31 days. The default is 1 day. (optional)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationsummarytopdevicesbyusage(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationSummaryTopDevicesModelsByUsage(self, organizations, **kwargs):
        """
        **Return metrics for organization's top 10 device models sorted by data usage over given time range. Default unit is megabytes.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-summary-top-devices-models-by-usage

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)

        These additional time based paramaters can be passed in directly to the class:
            - t0 (string): The beginning of the timespan for the data. (optional)
            - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 8 hours and be less than or equal to 31 days. The default is 1 day. (optional)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationsummarytopdevicesmodelsbyusage(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationSummaryTopSsidsByUsage(self, organizations, **kwargs):
        """
        **Return metrics for organization's top 10 ssids by data usage over given time range. Default unit is megabytes.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-summary-top-ssids-by-usage

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)

        These additional time based paramaters can be passed in directly to the class:
            - t0 (string): The beginning of the timespan for the data. (optional)
            - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 8 hours and be less than or equal to 31 days. The default is 1 day. (optional)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationsummarytopssidsbyusage(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationSummaryTopSwitchesByEnergyUsage(self, organizations, **kwargs):
        """
        **Return metrics for organization's top 10 switches by energy usage over given time range. Default unit is joules.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-summary-top-switches-by-energy-usage

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)

        These additional time based paramaters can be passed in directly to the class:
            - t0 (string): The beginning of the timespan for the data. (optional)
            - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 25 minutes and be less than or equal to 31 days. The default is 1 day. (optional)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationsummarytopswitchesbyenergyusage(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationUplinksStatuses(self, organizations, **kwargs):
        """
        **List the uplink status of every Meraki MX, MG and Z series devices in the organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-uplinks-statuses

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
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
            async_tasks._async_getorganizationuplinksstatuses(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationWebhooksAlertTypes(self, organizations, **kwargs):
        """
        **Return a list of alert types to be used with managing webhook alerts**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-webhooks-alert-types

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)
            - productType (string): Filter sample alerts to a specific product type (optional)

        These additional time based paramaters can be passed in directly to the class:

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationwebhooksalerttypes(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationWebhooksLogs(self, organizations, **kwargs):
        """
        **Return the log of webhook POSTs sent**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-webhooks-logs

        organizations: (list) List containing one or more organizations (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)
            - url (string): The URL the webhook was sent to (optional)

        These additional time based paramaters can be passed in directly to the class:
            - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 90 days from today. (optional)
            - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day. (optional)
            - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 50. (optional)
            - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationwebhookslogs(
                organizations= organizations,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

