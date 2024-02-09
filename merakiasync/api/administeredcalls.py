import asyncio

import merakiasync.asynctasks.administeredtasks as async_tasks

class Administered:
    def __init__(self, apikey, debug_dict):
        self._apikey = apikey
        self._debug_dict = debug_dict
        self._loop = asyncio.get_event_loop()

    def AsyncGetAdministeredIdentitiesMe(self):
        """
        **Returns the identity of the current user.**
        https://developer.cisco.com/meraki/api-v1/#!get-administered-identities-me


        """

        return self._loop.run_until_complete(
            async_tasks._async_getadministeredidentitiesme(
                apikey=self._apikey,
                debug_dict=self._debug_dict,
            ))

