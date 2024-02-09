import asyncio

import merakiasync.asynctasks.licensingtasks as async_tasks

class Licensing:
    def __init__(self, apikey, debug_dict):
        self._apikey = apikey
        self._debug_dict = debug_dict
        self._loop = asyncio.get_event_loop()

    def AsyncGetOrganizationLicensingCotermLicenses(self, all_licensing, **kwargs):
        """
        **List the licenses in a coterm organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-licensing-coterm-licenses

        licensing: (list) List containing one or more licensing (dict).  Each nested dict can include the following required and/or optional keys/values:
            - organizationId (string): Organization ID (required)
            - invalidated (boolean): Filter for licenses that are invalidated (optional)
            - expired (boolean): Filter for licenses that are expired (optional)

        These additional time based paramaters can be passed in directly to the class:
            - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. (optional)
            - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)
            - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. (optional)

        """
        return self._loop.run_until_complete(
            async_tasks._async_getorganizationlicensingcotermlicenses(
                all_licensing= all_licensing,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

