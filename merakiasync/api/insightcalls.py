import asyncio

import merakiasync.asynctasks.insighttasks as async_tasks

class Insight:
    def __init__(self, apikey, debug_dict):
        self._apikey = apikey
        self._debug_dict = debug_dict
        self._loop = asyncio.get_event_loop()

    def AsyncGetNetworkInsightApplicationHealthByTime(self, insights, **kwargs):
        """
        **Get application health by time**
        https://developer.cisco.com/meraki/api-v1/#!get-network-insight-application-health-by-time

        insight: (list) List containing one or more insight (dict).  Each nested dict must include following required keys/values:
            - networkId (string): Network ID (required)
            - applicationId (string): Application ID (required)
        
        The following optional paramaters can be passed directly to the class as arguments:
            - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 7 days from today. (optional)
            - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. The default is 2 hours. (optional)
            - resolution (integer): The time resolution in seconds for returned data. The valid resolutions are: 60, 300, 3600, 86400. The default is 300. (optional)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getnetworkinsightapplicationhealthbytime(
                insights= insights,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationInsightApplications(self, insights, **kwargs):
        """
        **List all Insight tracked applications**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-insight-applications

        insight: (list) List containing one or more insight (dict).  Each nested dict must include following required keys/values:
            - organizationId (string): Organization ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationinsightapplications(
                insights= insights,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationInsightMonitoredMediaServers(self, insights, **kwargs):
        """
        **List the monitored media servers for this organization. Only valid for organizations with Meraki Insight.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-insight-monitored-media-servers

        insight: (list) List containing one or more insight (dict).  Each nested dict must include following required keys/values:
            - organizationId (string): Organization ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationinsightmonitoredmediaservers(
                insights= insights,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetOrganizationInsightMonitoredMediaServer(self, insights, **kwargs):
        """
        **Return a monitored media server for this organization. Only valid for organizations with Meraki Insight.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-insight-monitored-media-server

        insight: (list) List containing one or more insight (dict).  Each nested dict must include following required keys/values:
            - organizationId (string): Organization ID (required)
            - monitoredMediaServerId (string): Monitored media server ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationinsightmonitoredmediaserver(
                insights= insights,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

