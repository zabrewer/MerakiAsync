import asyncio

import merakiasync.asynctasks.licensingtasks as async_tasks

class Licensing:
    def __init__(self, apikey, debug_dict):
        self._apikey = apikey
        self._debug_dict = debug_dict
        self._loop = asyncio.get_event_loop()

    def AsyncGetAdministeredLicensingSubscriptionSubscriptions(self):
        """
        **List available subscriptions**
        https://developer.cisco.com/meraki/api-v1/#!get-administered-licensing-subscription-subscriptions

        
        The following optional paramaters can be passed directly to the class as arguments:
            - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. (optional)
            - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - subscriptionIds (array): List of subscription ids to fetch (optional)
            - organizationIds (array): Organizations to get associated subscriptions for (optional)
            - startDate (string): Filter subscriptions by start date, ISO 8601 format. To filter with a range of dates, use 'startDate[<option>]=?' in the request. Accepted options include lt, gt, lte, gte. (optional)
            - endDate (string): Filter subscriptions by end date, ISO 8601 format. To filter with a range of dates, use 'endDate[<option>]=?' in the request. Accepted options include lt, gt, lte, gte. (optional)
            - statuses (array): List of statuses that returned subscriptions can have (optional)
            - productTypes (array): List of product types that returned subscriptions need to have entitlements for. (optional)
            - total_pages (integer or string): (defaults to "all") use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages (optional)
            - direction (string): direction to paginate, either "next" (default) or "prev" page (optional)
        """

        return self._loop.run_until_complete(
            async_tasks._async_getadministeredlicensingsubscriptionsubscriptions(
                apikey=self._apikey,
                debug_dict=self._debug_dict,
            ))

    def AsyncGetOrganizationLicensingCotermLicenses(self, all_licensing, **kwargs):
        """
        **List the licenses in a coterm organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-licensing-coterm-licenses

        licensing: (list) List containing one or more licensing (dict).  Each nested dict must include following required keys/values:
            - organizationId (string): Organization ID (required)
        
        The following optional paramaters can be passed directly to the class as arguments:
            - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. (optional)
            - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - invalidated (boolean): Filter for licenses that are invalidated (optional)
            - expired (boolean): Filter for licenses that are expired (optional)
            - total_pages (integer or string): (defaults to "all") use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages (optional)
            - direction (string): direction to paginate, either "next" (default) or "prev" page (optional)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationlicensingcotermlicenses(
                all_licensing= all_licensing,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

