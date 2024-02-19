import asyncio

import merakiasync.asynctasks.devicestasks as async_tasks

class Devices:
    def __init__(self, apikey, debug_dict):
        self._apikey = apikey
        self._debug_dict = debug_dict
        self._loop = asyncio.get_event_loop()

    def AsyncGetDevice(self, devices, **kwargs):
        """
        **Return a single device**
        https://developer.cisco.com/meraki/api-v1/#!get-device

        devices: (list) List containing one or more devices (dict).  Each nested dict must include following required keys/values:
            - serial (string): Serial (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getdevice(
                devices= devices,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetDeviceCellularSims(self, devices, **kwargs):
        """
        **Return the SIM and APN configurations for a cellular device.**
        https://developer.cisco.com/meraki/api-v1/#!get-device-cellular-sims

        devices: (list) List containing one or more devices (dict).  Each nested dict must include following required keys/values:
            - serial (string): Serial (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getdevicecellularsims(
                devices= devices,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetDeviceClients(self, devices, **kwargs):
        """
        **List the clients of a device, up to a maximum of a month ago. The usage of each client is returned in kilobytes. If the device is a switch, the switchport is returned; otherwise the switchport field is null.**
        https://developer.cisco.com/meraki/api-v1/#!get-device-clients

        devices: (list) List containing one or more devices (dict).  Each nested dict must include following required keys/values:
            - serial (string): Serial (required)
        
        The following optional paramaters can be passed directly to the class as arguments:
            - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day. (optional)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getdeviceclients(
                devices= devices,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetDeviceLiveToolsArpTable(self, devices, **kwargs):
        """
        **Return an ARP table live tool job.**
        https://developer.cisco.com/meraki/api-v1/#!get-device-live-tools-arp-table

        devices: (list) List containing one or more devices (dict).  Each nested dict must include following required keys/values:
            - serial (string): Serial (required)
            - arpTableId (string): Arp table ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getdevicelivetoolsarptable(
                devices= devices,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetDeviceLiveToolsCableTest(self, devices, **kwargs):
        """
        **Return a cable test live tool job.**
        https://developer.cisco.com/meraki/api-v1/#!get-device-live-tools-cable-test

        devices: (list) List containing one or more devices (dict).  Each nested dict must include following required keys/values:
            - serial (string): Serial (required)
            - id (string): ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getdevicelivetoolscabletest(
                devices= devices,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetDeviceLiveToolsPing(self, devices, **kwargs):
        """
        **Return a ping job. Latency unit in response is in milliseconds. Size is in bytes.**
        https://developer.cisco.com/meraki/api-v1/#!get-device-live-tools-ping

        devices: (list) List containing one or more devices (dict).  Each nested dict must include following required keys/values:
            - serial (string): Serial (required)
            - id (string): ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getdevicelivetoolsping(
                devices= devices,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetDeviceLiveToolsPingDevice(self, devices, **kwargs):
        """
        **Return a ping device job. Latency unit in response is in milliseconds. Size is in bytes.**
        https://developer.cisco.com/meraki/api-v1/#!get-device-live-tools-ping-device

        devices: (list) List containing one or more devices (dict).  Each nested dict must include following required keys/values:
            - serial (string): Serial (required)
            - id (string): ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getdevicelivetoolspingdevice(
                devices= devices,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetDeviceLiveToolsThroughputTest(self, devices, **kwargs):
        """
        **Return a throughput test job**
        https://developer.cisco.com/meraki/api-v1/#!get-device-live-tools-throughput-test

        devices: (list) List containing one or more devices (dict).  Each nested dict must include following required keys/values:
            - serial (string): Serial (required)
            - throughputTestId (string): Throughput test ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getdevicelivetoolsthroughputtest(
                devices= devices,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetDeviceLiveToolsWakeOnLan(self, devices, **kwargs):
        """
        **Return a Wake-on-LAN job**
        https://developer.cisco.com/meraki/api-v1/#!get-device-live-tools-wake-on-lan

        devices: (list) List containing one or more devices (dict).  Each nested dict must include following required keys/values:
            - serial (string): Serial (required)
            - wakeOnLanId (string): Wake on lan ID (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getdevicelivetoolswakeonlan(
                devices= devices,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetDeviceLldpCdp(self, devices, **kwargs):
        """
        **List LLDP and CDP information for a device**
        https://developer.cisco.com/meraki/api-v1/#!get-device-lldp-cdp

        devices: (list) List containing one or more devices (dict).  Each nested dict must include following required keys/values:
            - serial (string): Serial (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getdevicelldpcdp(
                devices= devices,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetDeviceLossAndLatencyHistory(self, devices, **kwargs):
        """
        **Get the uplink loss percentage and latency in milliseconds, and goodput in kilobits per second for MX, MG and Z devices.**
        https://developer.cisco.com/meraki/api-v1/#!get-device-loss-and-latency-history

        devices: (list) List containing one or more devices (dict).  Each nested dict must include following required keys/values:
            - serial (string): Serial (required)
            - ip (string): The destination IP used to obtain the requested stats. This is required. (required)
        
        The following optional paramaters can be passed directly to the class as arguments:
            - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 60 days from today. (optional)
            - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0. (optional)
            - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day. (optional)
            - resolution (integer): The time resolution in seconds for returned data. The valid resolutions are: 60, 600, 3600, 86400. The default is 60. (optional)
            - uplink (string): The WAN uplink used to obtain the requested stats. Valid uplinks are wan1, wan2, wan3, cellular. The default is wan1. (optional)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getdevicelossandlatencyhistory(
                devices= devices,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

    def AsyncGetDeviceManagementInterface(self, devices, **kwargs):
        """
        **Return the management interface settings for a device**
        https://developer.cisco.com/meraki/api-v1/#!get-device-management-interface

        devices: (list) List containing one or more devices (dict).  Each nested dict must include following required keys/values:
            - serial (string): Serial (required)
        """
        return self._loop.run_until_complete(
            async_tasks._async_getdevicemanagementinterface(
                devices= devices,
                apikey=self._apikey,
                debug_dict=self._debug_dict,
                **kwargs
            ))

