import meraki.aio
import asyncio
import tqdm

def return_message(data):
    if isinstance(data, (list)):
        error_data = data[0]
    elif isinstance(data, (dict)):
        error_data = data

    data_keys = set(error_data.keys())
    relevent_keys = {'id', 'name', 'organizationName', 'organizationId', 'networkName', 'networkId'}
    contained_keys = list(data_keys.intersection(relevent_keys))
    message_data = {}
    for each_key, each_value in data.items():
        if each_key in contained_keys:
            message_data[each_key] = each_value

    return message_data

def add_keys(input_json, output_json):
    input_keys = set(input_json.keys())
    output_keys = set(output_json.keys())
    relevent_keys = {'organizationName', 'organizationId', 'networkName', 'networkId'}

    contains_relevent_input = (bool(set(input_keys) & set(relevent_keys)))

    if not contains_relevent_input:
        return output_json
    else:
        relevant_keys_input = set(input_keys) & set(relevent_keys)
        for each_key in relevant_keys_input:
            if each_key not in output_keys:
                output_json[each_key] = input_json[each_key]
        
        return output_json

async def _call_getdevicewirelessbluetoothsettings(aiomeraki, wireless, **kwargs):
    try:
        returned_json = await aiomeraki.wireless.getDeviceWirelessBluetoothSettings(
            serial=wireless['serial'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=wireless)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=wireless)
        print('Non Meraki API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    if returned_json:

        if isinstance(returned_json, (list)):
            updated_json = []
            for each_dict in returned_json:
                keys_added = add_keys(input_json=wireless, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=wireless, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getdevicewirelessbluetoothsettings(apikey, debug_dict, all_wireless, **kwargs):
    async with meraki.aio.AsyncDashboardAPI(
        api_key=apikey,
        base_url=debug_dict['base_url'],
        log_file_prefix=debug_dict['log_file_prefix'],
        log_path=debug_dict['log_path'],
        maximum_concurrent_requests=debug_dict['maximum_concurrent_requests'],
        maximum_retries=debug_dict['maximum_retries'],
        wait_on_rate_limit=debug_dict['wait_on_rate_limit'],
        output_log=debug_dict['output_log'],
        print_console=debug_dict['print_console'],
        suppress_logging=debug_dict['suppress_logging'],
        caller=debug_dict['caller'],
    ) as aiomeraki:

        wireless_tasks = [
            _call_getdevicewirelessbluetoothsettings(aiomeraki, wireless, **kwargs) for wireless in all_wireless
            ]
        all_wireless_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(wireless_tasks),
                total=len(wireless_tasks),
                colour='green',
        ):
            wireless_json = await task
            if wireless_json:
                all_wireless_json.extend(iter(wireless_json))
        return all_wireless_json

async def _call_getdevicewirelessconnectionstats(aiomeraki, wireless, **kwargs):
    try:
        returned_json = await aiomeraki.wireless.getDeviceWirelessConnectionStats(
            serial=wireless['serial'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=wireless)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=wireless)
        print('Non Meraki API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    if returned_json:

        if isinstance(returned_json, (list)):
            updated_json = []
            for each_dict in returned_json:
                keys_added = add_keys(input_json=wireless, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=wireless, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getdevicewirelessconnectionstats(apikey, debug_dict, all_wireless, **kwargs):
    async with meraki.aio.AsyncDashboardAPI(
        api_key=apikey,
        base_url=debug_dict['base_url'],
        log_file_prefix=debug_dict['log_file_prefix'],
        log_path=debug_dict['log_path'],
        maximum_concurrent_requests=debug_dict['maximum_concurrent_requests'],
        maximum_retries=debug_dict['maximum_retries'],
        wait_on_rate_limit=debug_dict['wait_on_rate_limit'],
        output_log=debug_dict['output_log'],
        print_console=debug_dict['print_console'],
        suppress_logging=debug_dict['suppress_logging'],
        caller=debug_dict['caller'],
    ) as aiomeraki:

        wireless_tasks = [
            _call_getdevicewirelessconnectionstats(aiomeraki, wireless, **kwargs) for wireless in all_wireless
            ]
        all_wireless_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(wireless_tasks),
                total=len(wireless_tasks),
                colour='green',
        ):
            wireless_json = await task
            if wireless_json:
                all_wireless_json.extend(iter(wireless_json))
        return all_wireless_json

async def _call_getdevicewirelesslatencystats(aiomeraki, wireless, **kwargs):
    try:
        returned_json = await aiomeraki.wireless.getDeviceWirelessLatencyStats(
            serial=wireless['serial'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=wireless)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=wireless)
        print('Non Meraki API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    if returned_json:

        if isinstance(returned_json, (list)):
            updated_json = []
            for each_dict in returned_json:
                keys_added = add_keys(input_json=wireless, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=wireless, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getdevicewirelesslatencystats(apikey, debug_dict, all_wireless, **kwargs):
    async with meraki.aio.AsyncDashboardAPI(
        api_key=apikey,
        base_url=debug_dict['base_url'],
        log_file_prefix=debug_dict['log_file_prefix'],
        log_path=debug_dict['log_path'],
        maximum_concurrent_requests=debug_dict['maximum_concurrent_requests'],
        maximum_retries=debug_dict['maximum_retries'],
        wait_on_rate_limit=debug_dict['wait_on_rate_limit'],
        output_log=debug_dict['output_log'],
        print_console=debug_dict['print_console'],
        suppress_logging=debug_dict['suppress_logging'],
        caller=debug_dict['caller'],
    ) as aiomeraki:

        wireless_tasks = [
            _call_getdevicewirelesslatencystats(aiomeraki, wireless, **kwargs) for wireless in all_wireless
            ]
        all_wireless_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(wireless_tasks),
                total=len(wireless_tasks),
                colour='green',
        ):
            wireless_json = await task
            if wireless_json:
                all_wireless_json.extend(iter(wireless_json))
        return all_wireless_json

async def _call_getdevicewirelessradiosettings(aiomeraki, wireless, **kwargs):
    try:
        returned_json = await aiomeraki.wireless.getDeviceWirelessRadioSettings(
            serial=wireless['serial'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=wireless)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=wireless)
        print('Non Meraki API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    if returned_json:

        if isinstance(returned_json, (list)):
            updated_json = []
            for each_dict in returned_json:
                keys_added = add_keys(input_json=wireless, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=wireless, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getdevicewirelessradiosettings(apikey, debug_dict, all_wireless, **kwargs):
    async with meraki.aio.AsyncDashboardAPI(
        api_key=apikey,
        base_url=debug_dict['base_url'],
        log_file_prefix=debug_dict['log_file_prefix'],
        log_path=debug_dict['log_path'],
        maximum_concurrent_requests=debug_dict['maximum_concurrent_requests'],
        maximum_retries=debug_dict['maximum_retries'],
        wait_on_rate_limit=debug_dict['wait_on_rate_limit'],
        output_log=debug_dict['output_log'],
        print_console=debug_dict['print_console'],
        suppress_logging=debug_dict['suppress_logging'],
        caller=debug_dict['caller'],
    ) as aiomeraki:

        wireless_tasks = [
            _call_getdevicewirelessradiosettings(aiomeraki, wireless, **kwargs) for wireless in all_wireless
            ]
        all_wireless_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(wireless_tasks),
                total=len(wireless_tasks),
                colour='green',
        ):
            wireless_json = await task
            if wireless_json:
                all_wireless_json.extend(iter(wireless_json))
        return all_wireless_json

async def _call_getdevicewirelessstatus(aiomeraki, wireless, **kwargs):
    try:
        returned_json = await aiomeraki.wireless.getDeviceWirelessStatus(
            serial=wireless['serial'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=wireless)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=wireless)
        print('Non Meraki API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    if returned_json:

        if isinstance(returned_json, (list)):
            updated_json = []
            for each_dict in returned_json:
                keys_added = add_keys(input_json=wireless, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=wireless, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getdevicewirelessstatus(apikey, debug_dict, all_wireless, **kwargs):
    async with meraki.aio.AsyncDashboardAPI(
        api_key=apikey,
        base_url=debug_dict['base_url'],
        log_file_prefix=debug_dict['log_file_prefix'],
        log_path=debug_dict['log_path'],
        maximum_concurrent_requests=debug_dict['maximum_concurrent_requests'],
        maximum_retries=debug_dict['maximum_retries'],
        wait_on_rate_limit=debug_dict['wait_on_rate_limit'],
        output_log=debug_dict['output_log'],
        print_console=debug_dict['print_console'],
        suppress_logging=debug_dict['suppress_logging'],
        caller=debug_dict['caller'],
    ) as aiomeraki:

        wireless_tasks = [
            _call_getdevicewirelessstatus(aiomeraki, wireless, **kwargs) for wireless in all_wireless
            ]
        all_wireless_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(wireless_tasks),
                total=len(wireless_tasks),
                colour='green',
        ):
            wireless_json = await task
            if wireless_json:
                all_wireless_json.extend(iter(wireless_json))
        return all_wireless_json

async def _call_getnetworkwirelessairmarshal(aiomeraki, wireless, **kwargs):
    try:
        returned_json = await aiomeraki.wireless.getNetworkWirelessAirMarshal(
            networkId=wireless['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=wireless)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=wireless)
        print('Non Meraki API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    if returned_json:

        if isinstance(returned_json, (list)):
            updated_json = []
            for each_dict in returned_json:
                keys_added = add_keys(input_json=wireless, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=wireless, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkwirelessairmarshal(apikey, debug_dict, all_wireless, **kwargs):
    async with meraki.aio.AsyncDashboardAPI(
        api_key=apikey,
        base_url=debug_dict['base_url'],
        log_file_prefix=debug_dict['log_file_prefix'],
        log_path=debug_dict['log_path'],
        maximum_concurrent_requests=debug_dict['maximum_concurrent_requests'],
        maximum_retries=debug_dict['maximum_retries'],
        wait_on_rate_limit=debug_dict['wait_on_rate_limit'],
        output_log=debug_dict['output_log'],
        print_console=debug_dict['print_console'],
        suppress_logging=debug_dict['suppress_logging'],
        caller=debug_dict['caller'],
    ) as aiomeraki:

        wireless_tasks = [
            _call_getnetworkwirelessairmarshal(aiomeraki, wireless, **kwargs) for wireless in all_wireless
            ]
        all_wireless_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(wireless_tasks),
                total=len(wireless_tasks),
                colour='green',
        ):
            wireless_json = await task
            if wireless_json:
                all_wireless_json.extend(iter(wireless_json))
        return all_wireless_json

async def _call_getnetworkwirelessalternatemanagementinterface(aiomeraki, wireless, **kwargs):
    try:
        returned_json = await aiomeraki.wireless.getNetworkWirelessAlternateManagementInterface(
            networkId=wireless['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=wireless)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=wireless)
        print('Non Meraki API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    if returned_json:

        if isinstance(returned_json, (list)):
            updated_json = []
            for each_dict in returned_json:
                keys_added = add_keys(input_json=wireless, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=wireless, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkwirelessalternatemanagementinterface(apikey, debug_dict, all_wireless, **kwargs):
    async with meraki.aio.AsyncDashboardAPI(
        api_key=apikey,
        base_url=debug_dict['base_url'],
        log_file_prefix=debug_dict['log_file_prefix'],
        log_path=debug_dict['log_path'],
        maximum_concurrent_requests=debug_dict['maximum_concurrent_requests'],
        maximum_retries=debug_dict['maximum_retries'],
        wait_on_rate_limit=debug_dict['wait_on_rate_limit'],
        output_log=debug_dict['output_log'],
        print_console=debug_dict['print_console'],
        suppress_logging=debug_dict['suppress_logging'],
        caller=debug_dict['caller'],
    ) as aiomeraki:

        wireless_tasks = [
            _call_getnetworkwirelessalternatemanagementinterface(aiomeraki, wireless, **kwargs) for wireless in all_wireless
            ]
        all_wireless_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(wireless_tasks),
                total=len(wireless_tasks),
                colour='green',
        ):
            wireless_json = await task
            if wireless_json:
                all_wireless_json.extend(iter(wireless_json))
        return all_wireless_json

async def _call_getnetworkwirelessbilling(aiomeraki, wireless, **kwargs):
    try:
        returned_json = await aiomeraki.wireless.getNetworkWirelessBilling(
            networkId=wireless['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=wireless)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=wireless)
        print('Non Meraki API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    if returned_json:

        if isinstance(returned_json, (list)):
            updated_json = []
            for each_dict in returned_json:
                keys_added = add_keys(input_json=wireless, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=wireless, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkwirelessbilling(apikey, debug_dict, all_wireless, **kwargs):
    async with meraki.aio.AsyncDashboardAPI(
        api_key=apikey,
        base_url=debug_dict['base_url'],
        log_file_prefix=debug_dict['log_file_prefix'],
        log_path=debug_dict['log_path'],
        maximum_concurrent_requests=debug_dict['maximum_concurrent_requests'],
        maximum_retries=debug_dict['maximum_retries'],
        wait_on_rate_limit=debug_dict['wait_on_rate_limit'],
        output_log=debug_dict['output_log'],
        print_console=debug_dict['print_console'],
        suppress_logging=debug_dict['suppress_logging'],
        caller=debug_dict['caller'],
    ) as aiomeraki:

        wireless_tasks = [
            _call_getnetworkwirelessbilling(aiomeraki, wireless, **kwargs) for wireless in all_wireless
            ]
        all_wireless_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(wireless_tasks),
                total=len(wireless_tasks),
                colour='green',
        ):
            wireless_json = await task
            if wireless_json:
                all_wireless_json.extend(iter(wireless_json))
        return all_wireless_json

async def _call_getnetworkwirelessbluetoothsettings(aiomeraki, wireless, **kwargs):
    try:
        returned_json = await aiomeraki.wireless.getNetworkWirelessBluetoothSettings(
            networkId=wireless['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=wireless)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=wireless)
        print('Non Meraki API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    if returned_json:

        if isinstance(returned_json, (list)):
            updated_json = []
            for each_dict in returned_json:
                keys_added = add_keys(input_json=wireless, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=wireless, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkwirelessbluetoothsettings(apikey, debug_dict, all_wireless, **kwargs):
    async with meraki.aio.AsyncDashboardAPI(
        api_key=apikey,
        base_url=debug_dict['base_url'],
        log_file_prefix=debug_dict['log_file_prefix'],
        log_path=debug_dict['log_path'],
        maximum_concurrent_requests=debug_dict['maximum_concurrent_requests'],
        maximum_retries=debug_dict['maximum_retries'],
        wait_on_rate_limit=debug_dict['wait_on_rate_limit'],
        output_log=debug_dict['output_log'],
        print_console=debug_dict['print_console'],
        suppress_logging=debug_dict['suppress_logging'],
        caller=debug_dict['caller'],
    ) as aiomeraki:

        wireless_tasks = [
            _call_getnetworkwirelessbluetoothsettings(aiomeraki, wireless, **kwargs) for wireless in all_wireless
            ]
        all_wireless_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(wireless_tasks),
                total=len(wireless_tasks),
                colour='green',
        ):
            wireless_json = await task
            if wireless_json:
                all_wireless_json.extend(iter(wireless_json))
        return all_wireless_json

async def _call_getnetworkwirelesschannelutilizationhistory(aiomeraki, wireless, **kwargs):
    try:
        returned_json = await aiomeraki.wireless.getNetworkWirelessChannelUtilizationHistory(
            networkId=wireless['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=wireless)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=wireless)
        print('Non Meraki API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    if returned_json:

        if isinstance(returned_json, (list)):
            updated_json = []
            for each_dict in returned_json:
                keys_added = add_keys(input_json=wireless, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=wireless, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkwirelesschannelutilizationhistory(apikey, debug_dict, all_wireless, **kwargs):
    async with meraki.aio.AsyncDashboardAPI(
        api_key=apikey,
        base_url=debug_dict['base_url'],
        log_file_prefix=debug_dict['log_file_prefix'],
        log_path=debug_dict['log_path'],
        maximum_concurrent_requests=debug_dict['maximum_concurrent_requests'],
        maximum_retries=debug_dict['maximum_retries'],
        wait_on_rate_limit=debug_dict['wait_on_rate_limit'],
        output_log=debug_dict['output_log'],
        print_console=debug_dict['print_console'],
        suppress_logging=debug_dict['suppress_logging'],
        caller=debug_dict['caller'],
    ) as aiomeraki:

        wireless_tasks = [
            _call_getnetworkwirelesschannelutilizationhistory(aiomeraki, wireless, **kwargs) for wireless in all_wireless
            ]
        all_wireless_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(wireless_tasks),
                total=len(wireless_tasks),
                colour='green',
        ):
            wireless_json = await task
            if wireless_json:
                all_wireless_json.extend(iter(wireless_json))
        return all_wireless_json

async def _call_getnetworkwirelessclientcounthistory(aiomeraki, wireless, **kwargs):
    try:
        returned_json = await aiomeraki.wireless.getNetworkWirelessClientCountHistory(
            networkId=wireless['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=wireless)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=wireless)
        print('Non Meraki API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    if returned_json:

        if isinstance(returned_json, (list)):
            updated_json = []
            for each_dict in returned_json:
                keys_added = add_keys(input_json=wireless, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=wireless, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkwirelessclientcounthistory(apikey, debug_dict, all_wireless, **kwargs):
    async with meraki.aio.AsyncDashboardAPI(
        api_key=apikey,
        base_url=debug_dict['base_url'],
        log_file_prefix=debug_dict['log_file_prefix'],
        log_path=debug_dict['log_path'],
        maximum_concurrent_requests=debug_dict['maximum_concurrent_requests'],
        maximum_retries=debug_dict['maximum_retries'],
        wait_on_rate_limit=debug_dict['wait_on_rate_limit'],
        output_log=debug_dict['output_log'],
        print_console=debug_dict['print_console'],
        suppress_logging=debug_dict['suppress_logging'],
        caller=debug_dict['caller'],
    ) as aiomeraki:

        wireless_tasks = [
            _call_getnetworkwirelessclientcounthistory(aiomeraki, wireless, **kwargs) for wireless in all_wireless
            ]
        all_wireless_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(wireless_tasks),
                total=len(wireless_tasks),
                colour='green',
        ):
            wireless_json = await task
            if wireless_json:
                all_wireless_json.extend(iter(wireless_json))
        return all_wireless_json

async def _call_getnetworkwirelessclientsconnectionstats(aiomeraki, wireless, **kwargs):
    try:
        returned_json = await aiomeraki.wireless.getNetworkWirelessClientsConnectionStats(
            networkId=wireless['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=wireless)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=wireless)
        print('Non Meraki API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    if returned_json:

        if isinstance(returned_json, (list)):
            updated_json = []
            for each_dict in returned_json:
                keys_added = add_keys(input_json=wireless, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=wireless, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkwirelessclientsconnectionstats(apikey, debug_dict, all_wireless, **kwargs):
    async with meraki.aio.AsyncDashboardAPI(
        api_key=apikey,
        base_url=debug_dict['base_url'],
        log_file_prefix=debug_dict['log_file_prefix'],
        log_path=debug_dict['log_path'],
        maximum_concurrent_requests=debug_dict['maximum_concurrent_requests'],
        maximum_retries=debug_dict['maximum_retries'],
        wait_on_rate_limit=debug_dict['wait_on_rate_limit'],
        output_log=debug_dict['output_log'],
        print_console=debug_dict['print_console'],
        suppress_logging=debug_dict['suppress_logging'],
        caller=debug_dict['caller'],
    ) as aiomeraki:

        wireless_tasks = [
            _call_getnetworkwirelessclientsconnectionstats(aiomeraki, wireless, **kwargs) for wireless in all_wireless
            ]
        all_wireless_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(wireless_tasks),
                total=len(wireless_tasks),
                colour='green',
        ):
            wireless_json = await task
            if wireless_json:
                all_wireless_json.extend(iter(wireless_json))
        return all_wireless_json

async def _call_getnetworkwirelessclientslatencystats(aiomeraki, wireless, **kwargs):
    try:
        returned_json = await aiomeraki.wireless.getNetworkWirelessClientsLatencyStats(
            networkId=wireless['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=wireless)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=wireless)
        print('Non Meraki API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    if returned_json:

        if isinstance(returned_json, (list)):
            updated_json = []
            for each_dict in returned_json:
                keys_added = add_keys(input_json=wireless, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=wireless, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkwirelessclientslatencystats(apikey, debug_dict, all_wireless, **kwargs):
    async with meraki.aio.AsyncDashboardAPI(
        api_key=apikey,
        base_url=debug_dict['base_url'],
        log_file_prefix=debug_dict['log_file_prefix'],
        log_path=debug_dict['log_path'],
        maximum_concurrent_requests=debug_dict['maximum_concurrent_requests'],
        maximum_retries=debug_dict['maximum_retries'],
        wait_on_rate_limit=debug_dict['wait_on_rate_limit'],
        output_log=debug_dict['output_log'],
        print_console=debug_dict['print_console'],
        suppress_logging=debug_dict['suppress_logging'],
        caller=debug_dict['caller'],
    ) as aiomeraki:

        wireless_tasks = [
            _call_getnetworkwirelessclientslatencystats(aiomeraki, wireless, **kwargs) for wireless in all_wireless
            ]
        all_wireless_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(wireless_tasks),
                total=len(wireless_tasks),
                colour='green',
        ):
            wireless_json = await task
            if wireless_json:
                all_wireless_json.extend(iter(wireless_json))
        return all_wireless_json

async def _call_getnetworkwirelessclientconnectionstats(aiomeraki, wireless, **kwargs):
    try:
        returned_json = await aiomeraki.wireless.getNetworkWirelessClientConnectionStats(
            networkId=wireless['networkId'],
            clientId=wireless['clientId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=wireless)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=wireless)
        print('Non Meraki API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    if returned_json:

        if isinstance(returned_json, (list)):
            updated_json = []
            for each_dict in returned_json:
                keys_added = add_keys(input_json=wireless, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=wireless, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkwirelessclientconnectionstats(apikey, debug_dict, all_wireless, **kwargs):
    async with meraki.aio.AsyncDashboardAPI(
        api_key=apikey,
        base_url=debug_dict['base_url'],
        log_file_prefix=debug_dict['log_file_prefix'],
        log_path=debug_dict['log_path'],
        maximum_concurrent_requests=debug_dict['maximum_concurrent_requests'],
        maximum_retries=debug_dict['maximum_retries'],
        wait_on_rate_limit=debug_dict['wait_on_rate_limit'],
        output_log=debug_dict['output_log'],
        print_console=debug_dict['print_console'],
        suppress_logging=debug_dict['suppress_logging'],
        caller=debug_dict['caller'],
    ) as aiomeraki:

        wireless_tasks = [
            _call_getnetworkwirelessclientconnectionstats(aiomeraki, wireless, **kwargs) for wireless in all_wireless
            ]
        all_wireless_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(wireless_tasks),
                total=len(wireless_tasks),
                colour='green',
        ):
            wireless_json = await task
            if wireless_json:
                all_wireless_json.extend(iter(wireless_json))
        return all_wireless_json

async def _call_getnetworkwirelessclientconnectivityevents(aiomeraki, wireless, **kwargs):
    try:
        returned_json = await aiomeraki.wireless.getNetworkWirelessClientConnectivityEvents(
            networkId=wireless['networkId'],
            clientId=wireless['clientId'],
            total_pages='all',
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=wireless)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=wireless)
        print('Non Meraki API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    if returned_json:

        if isinstance(returned_json, (list)):
            updated_json = []
            for each_dict in returned_json:
                keys_added = add_keys(input_json=wireless, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=wireless, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkwirelessclientconnectivityevents(apikey, debug_dict, all_wireless, **kwargs):
    async with meraki.aio.AsyncDashboardAPI(
        api_key=apikey,
        base_url=debug_dict['base_url'],
        log_file_prefix=debug_dict['log_file_prefix'],
        log_path=debug_dict['log_path'],
        maximum_concurrent_requests=debug_dict['maximum_concurrent_requests'],
        maximum_retries=debug_dict['maximum_retries'],
        wait_on_rate_limit=debug_dict['wait_on_rate_limit'],
        output_log=debug_dict['output_log'],
        print_console=debug_dict['print_console'],
        suppress_logging=debug_dict['suppress_logging'],
        caller=debug_dict['caller'],
    ) as aiomeraki:

        wireless_tasks = [
            _call_getnetworkwirelessclientconnectivityevents(aiomeraki, wireless, **kwargs) for wireless in all_wireless
            ]
        all_wireless_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(wireless_tasks),
                total=len(wireless_tasks),
                colour='green',
        ):
            wireless_json = await task
            if wireless_json:
                all_wireless_json.extend(iter(wireless_json))
        return all_wireless_json

async def _call_getnetworkwirelessclientlatencyhistory(aiomeraki, wireless, **kwargs):
    try:
        returned_json = await aiomeraki.wireless.getNetworkWirelessClientLatencyHistory(
            networkId=wireless['networkId'],
            clientId=wireless['clientId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=wireless)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=wireless)
        print('Non Meraki API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    if returned_json:

        if isinstance(returned_json, (list)):
            updated_json = []
            for each_dict in returned_json:
                keys_added = add_keys(input_json=wireless, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=wireless, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkwirelessclientlatencyhistory(apikey, debug_dict, all_wireless, **kwargs):
    async with meraki.aio.AsyncDashboardAPI(
        api_key=apikey,
        base_url=debug_dict['base_url'],
        log_file_prefix=debug_dict['log_file_prefix'],
        log_path=debug_dict['log_path'],
        maximum_concurrent_requests=debug_dict['maximum_concurrent_requests'],
        maximum_retries=debug_dict['maximum_retries'],
        wait_on_rate_limit=debug_dict['wait_on_rate_limit'],
        output_log=debug_dict['output_log'],
        print_console=debug_dict['print_console'],
        suppress_logging=debug_dict['suppress_logging'],
        caller=debug_dict['caller'],
    ) as aiomeraki:

        wireless_tasks = [
            _call_getnetworkwirelessclientlatencyhistory(aiomeraki, wireless, **kwargs) for wireless in all_wireless
            ]
        all_wireless_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(wireless_tasks),
                total=len(wireless_tasks),
                colour='green',
        ):
            wireless_json = await task
            if wireless_json:
                all_wireless_json.extend(iter(wireless_json))
        return all_wireless_json

async def _call_getnetworkwirelessclientlatencystats(aiomeraki, wireless, **kwargs):
    try:
        returned_json = await aiomeraki.wireless.getNetworkWirelessClientLatencyStats(
            networkId=wireless['networkId'],
            clientId=wireless['clientId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=wireless)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=wireless)
        print('Non Meraki API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    if returned_json:

        if isinstance(returned_json, (list)):
            updated_json = []
            for each_dict in returned_json:
                keys_added = add_keys(input_json=wireless, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=wireless, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkwirelessclientlatencystats(apikey, debug_dict, all_wireless, **kwargs):
    async with meraki.aio.AsyncDashboardAPI(
        api_key=apikey,
        base_url=debug_dict['base_url'],
        log_file_prefix=debug_dict['log_file_prefix'],
        log_path=debug_dict['log_path'],
        maximum_concurrent_requests=debug_dict['maximum_concurrent_requests'],
        maximum_retries=debug_dict['maximum_retries'],
        wait_on_rate_limit=debug_dict['wait_on_rate_limit'],
        output_log=debug_dict['output_log'],
        print_console=debug_dict['print_console'],
        suppress_logging=debug_dict['suppress_logging'],
        caller=debug_dict['caller'],
    ) as aiomeraki:

        wireless_tasks = [
            _call_getnetworkwirelessclientlatencystats(aiomeraki, wireless, **kwargs) for wireless in all_wireless
            ]
        all_wireless_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(wireless_tasks),
                total=len(wireless_tasks),
                colour='green',
        ):
            wireless_json = await task
            if wireless_json:
                all_wireless_json.extend(iter(wireless_json))
        return all_wireless_json

async def _call_getnetworkwirelessconnectionstats(aiomeraki, wireless, **kwargs):
    try:
        returned_json = await aiomeraki.wireless.getNetworkWirelessConnectionStats(
            networkId=wireless['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=wireless)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=wireless)
        print('Non Meraki API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    if returned_json:

        if isinstance(returned_json, (list)):
            updated_json = []
            for each_dict in returned_json:
                keys_added = add_keys(input_json=wireless, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=wireless, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkwirelessconnectionstats(apikey, debug_dict, all_wireless, **kwargs):
    async with meraki.aio.AsyncDashboardAPI(
        api_key=apikey,
        base_url=debug_dict['base_url'],
        log_file_prefix=debug_dict['log_file_prefix'],
        log_path=debug_dict['log_path'],
        maximum_concurrent_requests=debug_dict['maximum_concurrent_requests'],
        maximum_retries=debug_dict['maximum_retries'],
        wait_on_rate_limit=debug_dict['wait_on_rate_limit'],
        output_log=debug_dict['output_log'],
        print_console=debug_dict['print_console'],
        suppress_logging=debug_dict['suppress_logging'],
        caller=debug_dict['caller'],
    ) as aiomeraki:

        wireless_tasks = [
            _call_getnetworkwirelessconnectionstats(aiomeraki, wireless, **kwargs) for wireless in all_wireless
            ]
        all_wireless_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(wireless_tasks),
                total=len(wireless_tasks),
                colour='green',
        ):
            wireless_json = await task
            if wireless_json:
                all_wireless_json.extend(iter(wireless_json))
        return all_wireless_json

async def _call_getnetworkwirelessdataratehistory(aiomeraki, wireless, **kwargs):
    try:
        returned_json = await aiomeraki.wireless.getNetworkWirelessDataRateHistory(
            networkId=wireless['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=wireless)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=wireless)
        print('Non Meraki API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    if returned_json:

        if isinstance(returned_json, (list)):
            updated_json = []
            for each_dict in returned_json:
                keys_added = add_keys(input_json=wireless, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=wireless, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkwirelessdataratehistory(apikey, debug_dict, all_wireless, **kwargs):
    async with meraki.aio.AsyncDashboardAPI(
        api_key=apikey,
        base_url=debug_dict['base_url'],
        log_file_prefix=debug_dict['log_file_prefix'],
        log_path=debug_dict['log_path'],
        maximum_concurrent_requests=debug_dict['maximum_concurrent_requests'],
        maximum_retries=debug_dict['maximum_retries'],
        wait_on_rate_limit=debug_dict['wait_on_rate_limit'],
        output_log=debug_dict['output_log'],
        print_console=debug_dict['print_console'],
        suppress_logging=debug_dict['suppress_logging'],
        caller=debug_dict['caller'],
    ) as aiomeraki:

        wireless_tasks = [
            _call_getnetworkwirelessdataratehistory(aiomeraki, wireless, **kwargs) for wireless in all_wireless
            ]
        all_wireless_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(wireless_tasks),
                total=len(wireless_tasks),
                colour='green',
        ):
            wireless_json = await task
            if wireless_json:
                all_wireless_json.extend(iter(wireless_json))
        return all_wireless_json

async def _call_getnetworkwirelessdevicesconnectionstats(aiomeraki, wireless, **kwargs):
    try:
        returned_json = await aiomeraki.wireless.getNetworkWirelessDevicesConnectionStats(
            networkId=wireless['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=wireless)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=wireless)
        print('Non Meraki API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    if returned_json:

        if isinstance(returned_json, (list)):
            updated_json = []
            for each_dict in returned_json:
                keys_added = add_keys(input_json=wireless, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=wireless, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkwirelessdevicesconnectionstats(apikey, debug_dict, all_wireless, **kwargs):
    async with meraki.aio.AsyncDashboardAPI(
        api_key=apikey,
        base_url=debug_dict['base_url'],
        log_file_prefix=debug_dict['log_file_prefix'],
        log_path=debug_dict['log_path'],
        maximum_concurrent_requests=debug_dict['maximum_concurrent_requests'],
        maximum_retries=debug_dict['maximum_retries'],
        wait_on_rate_limit=debug_dict['wait_on_rate_limit'],
        output_log=debug_dict['output_log'],
        print_console=debug_dict['print_console'],
        suppress_logging=debug_dict['suppress_logging'],
        caller=debug_dict['caller'],
    ) as aiomeraki:

        wireless_tasks = [
            _call_getnetworkwirelessdevicesconnectionstats(aiomeraki, wireless, **kwargs) for wireless in all_wireless
            ]
        all_wireless_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(wireless_tasks),
                total=len(wireless_tasks),
                colour='green',
        ):
            wireless_json = await task
            if wireless_json:
                all_wireless_json.extend(iter(wireless_json))
        return all_wireless_json

async def _call_getnetworkwirelessdeviceslatencystats(aiomeraki, wireless, **kwargs):
    try:
        returned_json = await aiomeraki.wireless.getNetworkWirelessDevicesLatencyStats(
            networkId=wireless['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=wireless)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=wireless)
        print('Non Meraki API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    if returned_json:

        if isinstance(returned_json, (list)):
            updated_json = []
            for each_dict in returned_json:
                keys_added = add_keys(input_json=wireless, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=wireless, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkwirelessdeviceslatencystats(apikey, debug_dict, all_wireless, **kwargs):
    async with meraki.aio.AsyncDashboardAPI(
        api_key=apikey,
        base_url=debug_dict['base_url'],
        log_file_prefix=debug_dict['log_file_prefix'],
        log_path=debug_dict['log_path'],
        maximum_concurrent_requests=debug_dict['maximum_concurrent_requests'],
        maximum_retries=debug_dict['maximum_retries'],
        wait_on_rate_limit=debug_dict['wait_on_rate_limit'],
        output_log=debug_dict['output_log'],
        print_console=debug_dict['print_console'],
        suppress_logging=debug_dict['suppress_logging'],
        caller=debug_dict['caller'],
    ) as aiomeraki:

        wireless_tasks = [
            _call_getnetworkwirelessdeviceslatencystats(aiomeraki, wireless, **kwargs) for wireless in all_wireless
            ]
        all_wireless_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(wireless_tasks),
                total=len(wireless_tasks),
                colour='green',
        ):
            wireless_json = await task
            if wireless_json:
                all_wireless_json.extend(iter(wireless_json))
        return all_wireless_json

async def _call_getnetworkwirelessethernetportsprofiles(aiomeraki, wireless, **kwargs):
    try:
        returned_json = await aiomeraki.wireless.getNetworkWirelessEthernetPortsProfiles(
            networkId=wireless['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=wireless)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=wireless)
        print('Non Meraki API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    if returned_json:

        if isinstance(returned_json, (list)):
            updated_json = []
            for each_dict in returned_json:
                keys_added = add_keys(input_json=wireless, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=wireless, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkwirelessethernetportsprofiles(apikey, debug_dict, all_wireless, **kwargs):
    async with meraki.aio.AsyncDashboardAPI(
        api_key=apikey,
        base_url=debug_dict['base_url'],
        log_file_prefix=debug_dict['log_file_prefix'],
        log_path=debug_dict['log_path'],
        maximum_concurrent_requests=debug_dict['maximum_concurrent_requests'],
        maximum_retries=debug_dict['maximum_retries'],
        wait_on_rate_limit=debug_dict['wait_on_rate_limit'],
        output_log=debug_dict['output_log'],
        print_console=debug_dict['print_console'],
        suppress_logging=debug_dict['suppress_logging'],
        caller=debug_dict['caller'],
    ) as aiomeraki:

        wireless_tasks = [
            _call_getnetworkwirelessethernetportsprofiles(aiomeraki, wireless, **kwargs) for wireless in all_wireless
            ]
        all_wireless_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(wireless_tasks),
                total=len(wireless_tasks),
                colour='green',
        ):
            wireless_json = await task
            if wireless_json:
                all_wireless_json.extend(iter(wireless_json))
        return all_wireless_json

async def _call_getnetworkwirelessethernetportsprofile(aiomeraki, wireless, **kwargs):
    try:
        returned_json = await aiomeraki.wireless.getNetworkWirelessEthernetPortsProfile(
            networkId=wireless['networkId'],
            profileId=wireless['profileId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=wireless)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=wireless)
        print('Non Meraki API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    if returned_json:

        if isinstance(returned_json, (list)):
            updated_json = []
            for each_dict in returned_json:
                keys_added = add_keys(input_json=wireless, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=wireless, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkwirelessethernetportsprofile(apikey, debug_dict, all_wireless, **kwargs):
    async with meraki.aio.AsyncDashboardAPI(
        api_key=apikey,
        base_url=debug_dict['base_url'],
        log_file_prefix=debug_dict['log_file_prefix'],
        log_path=debug_dict['log_path'],
        maximum_concurrent_requests=debug_dict['maximum_concurrent_requests'],
        maximum_retries=debug_dict['maximum_retries'],
        wait_on_rate_limit=debug_dict['wait_on_rate_limit'],
        output_log=debug_dict['output_log'],
        print_console=debug_dict['print_console'],
        suppress_logging=debug_dict['suppress_logging'],
        caller=debug_dict['caller'],
    ) as aiomeraki:

        wireless_tasks = [
            _call_getnetworkwirelessethernetportsprofile(aiomeraki, wireless, **kwargs) for wireless in all_wireless
            ]
        all_wireless_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(wireless_tasks),
                total=len(wireless_tasks),
                colour='green',
        ):
            wireless_json = await task
            if wireless_json:
                all_wireless_json.extend(iter(wireless_json))
        return all_wireless_json

async def _call_getnetworkwirelessfailedconnections(aiomeraki, wireless, **kwargs):
    try:
        returned_json = await aiomeraki.wireless.getNetworkWirelessFailedConnections(
            networkId=wireless['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=wireless)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=wireless)
        print('Non Meraki API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    if returned_json:

        if isinstance(returned_json, (list)):
            updated_json = []
            for each_dict in returned_json:
                keys_added = add_keys(input_json=wireless, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=wireless, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkwirelessfailedconnections(apikey, debug_dict, all_wireless, **kwargs):
    async with meraki.aio.AsyncDashboardAPI(
        api_key=apikey,
        base_url=debug_dict['base_url'],
        log_file_prefix=debug_dict['log_file_prefix'],
        log_path=debug_dict['log_path'],
        maximum_concurrent_requests=debug_dict['maximum_concurrent_requests'],
        maximum_retries=debug_dict['maximum_retries'],
        wait_on_rate_limit=debug_dict['wait_on_rate_limit'],
        output_log=debug_dict['output_log'],
        print_console=debug_dict['print_console'],
        suppress_logging=debug_dict['suppress_logging'],
        caller=debug_dict['caller'],
    ) as aiomeraki:

        wireless_tasks = [
            _call_getnetworkwirelessfailedconnections(aiomeraki, wireless, **kwargs) for wireless in all_wireless
            ]
        all_wireless_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(wireless_tasks),
                total=len(wireless_tasks),
                colour='green',
        ):
            wireless_json = await task
            if wireless_json:
                all_wireless_json.extend(iter(wireless_json))
        return all_wireless_json

async def _call_getnetworkwirelesslatencyhistory(aiomeraki, wireless, **kwargs):
    try:
        returned_json = await aiomeraki.wireless.getNetworkWirelessLatencyHistory(
            networkId=wireless['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=wireless)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=wireless)
        print('Non Meraki API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    if returned_json:

        if isinstance(returned_json, (list)):
            updated_json = []
            for each_dict in returned_json:
                keys_added = add_keys(input_json=wireless, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=wireless, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkwirelesslatencyhistory(apikey, debug_dict, all_wireless, **kwargs):
    async with meraki.aio.AsyncDashboardAPI(
        api_key=apikey,
        base_url=debug_dict['base_url'],
        log_file_prefix=debug_dict['log_file_prefix'],
        log_path=debug_dict['log_path'],
        maximum_concurrent_requests=debug_dict['maximum_concurrent_requests'],
        maximum_retries=debug_dict['maximum_retries'],
        wait_on_rate_limit=debug_dict['wait_on_rate_limit'],
        output_log=debug_dict['output_log'],
        print_console=debug_dict['print_console'],
        suppress_logging=debug_dict['suppress_logging'],
        caller=debug_dict['caller'],
    ) as aiomeraki:

        wireless_tasks = [
            _call_getnetworkwirelesslatencyhistory(aiomeraki, wireless, **kwargs) for wireless in all_wireless
            ]
        all_wireless_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(wireless_tasks),
                total=len(wireless_tasks),
                colour='green',
        ):
            wireless_json = await task
            if wireless_json:
                all_wireless_json.extend(iter(wireless_json))
        return all_wireless_json

async def _call_getnetworkwirelesslatencystats(aiomeraki, wireless, **kwargs):
    try:
        returned_json = await aiomeraki.wireless.getNetworkWirelessLatencyStats(
            networkId=wireless['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=wireless)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=wireless)
        print('Non Meraki API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    if returned_json:

        if isinstance(returned_json, (list)):
            updated_json = []
            for each_dict in returned_json:
                keys_added = add_keys(input_json=wireless, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=wireless, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkwirelesslatencystats(apikey, debug_dict, all_wireless, **kwargs):
    async with meraki.aio.AsyncDashboardAPI(
        api_key=apikey,
        base_url=debug_dict['base_url'],
        log_file_prefix=debug_dict['log_file_prefix'],
        log_path=debug_dict['log_path'],
        maximum_concurrent_requests=debug_dict['maximum_concurrent_requests'],
        maximum_retries=debug_dict['maximum_retries'],
        wait_on_rate_limit=debug_dict['wait_on_rate_limit'],
        output_log=debug_dict['output_log'],
        print_console=debug_dict['print_console'],
        suppress_logging=debug_dict['suppress_logging'],
        caller=debug_dict['caller'],
    ) as aiomeraki:

        wireless_tasks = [
            _call_getnetworkwirelesslatencystats(aiomeraki, wireless, **kwargs) for wireless in all_wireless
            ]
        all_wireless_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(wireless_tasks),
                total=len(wireless_tasks),
                colour='green',
        ):
            wireless_json = await task
            if wireless_json:
                all_wireless_json.extend(iter(wireless_json))
        return all_wireless_json

async def _call_getnetworkwirelessmeshstatuses(aiomeraki, wireless, **kwargs):
    try:
        returned_json = await aiomeraki.wireless.getNetworkWirelessMeshStatuses(
            networkId=wireless['networkId'],
            total_pages='all',
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=wireless)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=wireless)
        print('Non Meraki API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    if returned_json:

        if isinstance(returned_json, (list)):
            updated_json = []
            for each_dict in returned_json:
                keys_added = add_keys(input_json=wireless, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=wireless, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkwirelessmeshstatuses(apikey, debug_dict, all_wireless, **kwargs):
    async with meraki.aio.AsyncDashboardAPI(
        api_key=apikey,
        base_url=debug_dict['base_url'],
        log_file_prefix=debug_dict['log_file_prefix'],
        log_path=debug_dict['log_path'],
        maximum_concurrent_requests=debug_dict['maximum_concurrent_requests'],
        maximum_retries=debug_dict['maximum_retries'],
        wait_on_rate_limit=debug_dict['wait_on_rate_limit'],
        output_log=debug_dict['output_log'],
        print_console=debug_dict['print_console'],
        suppress_logging=debug_dict['suppress_logging'],
        caller=debug_dict['caller'],
    ) as aiomeraki:

        wireless_tasks = [
            _call_getnetworkwirelessmeshstatuses(aiomeraki, wireless, **kwargs) for wireless in all_wireless
            ]
        all_wireless_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(wireless_tasks),
                total=len(wireless_tasks),
                colour='green',
        ):
            wireless_json = await task
            if wireless_json:
                all_wireless_json.extend(iter(wireless_json))
        return all_wireless_json

async def _call_getnetworkwirelessrfprofiles(aiomeraki, wireless, **kwargs):
    try:
        returned_json = await aiomeraki.wireless.getNetworkWirelessRfProfiles(
            networkId=wireless['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=wireless)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=wireless)
        print('Non Meraki API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    if returned_json:

        if isinstance(returned_json, (list)):
            updated_json = []
            for each_dict in returned_json:
                keys_added = add_keys(input_json=wireless, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=wireless, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkwirelessrfprofiles(apikey, debug_dict, all_wireless, **kwargs):
    async with meraki.aio.AsyncDashboardAPI(
        api_key=apikey,
        base_url=debug_dict['base_url'],
        log_file_prefix=debug_dict['log_file_prefix'],
        log_path=debug_dict['log_path'],
        maximum_concurrent_requests=debug_dict['maximum_concurrent_requests'],
        maximum_retries=debug_dict['maximum_retries'],
        wait_on_rate_limit=debug_dict['wait_on_rate_limit'],
        output_log=debug_dict['output_log'],
        print_console=debug_dict['print_console'],
        suppress_logging=debug_dict['suppress_logging'],
        caller=debug_dict['caller'],
    ) as aiomeraki:

        wireless_tasks = [
            _call_getnetworkwirelessrfprofiles(aiomeraki, wireless, **kwargs) for wireless in all_wireless
            ]
        all_wireless_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(wireless_tasks),
                total=len(wireless_tasks),
                colour='green',
        ):
            wireless_json = await task
            if wireless_json:
                all_wireless_json.extend(iter(wireless_json))
        return all_wireless_json

async def _call_getnetworkwirelessrfprofile(aiomeraki, wireless, **kwargs):
    try:
        returned_json = await aiomeraki.wireless.getNetworkWirelessRfProfile(
            networkId=wireless['networkId'],
            rfProfileId=wireless['rfProfileId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=wireless)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=wireless)
        print('Non Meraki API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    if returned_json:

        if isinstance(returned_json, (list)):
            updated_json = []
            for each_dict in returned_json:
                keys_added = add_keys(input_json=wireless, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=wireless, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkwirelessrfprofile(apikey, debug_dict, all_wireless, **kwargs):
    async with meraki.aio.AsyncDashboardAPI(
        api_key=apikey,
        base_url=debug_dict['base_url'],
        log_file_prefix=debug_dict['log_file_prefix'],
        log_path=debug_dict['log_path'],
        maximum_concurrent_requests=debug_dict['maximum_concurrent_requests'],
        maximum_retries=debug_dict['maximum_retries'],
        wait_on_rate_limit=debug_dict['wait_on_rate_limit'],
        output_log=debug_dict['output_log'],
        print_console=debug_dict['print_console'],
        suppress_logging=debug_dict['suppress_logging'],
        caller=debug_dict['caller'],
    ) as aiomeraki:

        wireless_tasks = [
            _call_getnetworkwirelessrfprofile(aiomeraki, wireless, **kwargs) for wireless in all_wireless
            ]
        all_wireless_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(wireless_tasks),
                total=len(wireless_tasks),
                colour='green',
        ):
            wireless_json = await task
            if wireless_json:
                all_wireless_json.extend(iter(wireless_json))
        return all_wireless_json

async def _call_getnetworkwirelesssettings(aiomeraki, wireless, **kwargs):
    try:
        returned_json = await aiomeraki.wireless.getNetworkWirelessSettings(
            networkId=wireless['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=wireless)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=wireless)
        print('Non Meraki API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    if returned_json:

        if isinstance(returned_json, (list)):
            updated_json = []
            for each_dict in returned_json:
                keys_added = add_keys(input_json=wireless, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=wireless, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkwirelesssettings(apikey, debug_dict, all_wireless, **kwargs):
    async with meraki.aio.AsyncDashboardAPI(
        api_key=apikey,
        base_url=debug_dict['base_url'],
        log_file_prefix=debug_dict['log_file_prefix'],
        log_path=debug_dict['log_path'],
        maximum_concurrent_requests=debug_dict['maximum_concurrent_requests'],
        maximum_retries=debug_dict['maximum_retries'],
        wait_on_rate_limit=debug_dict['wait_on_rate_limit'],
        output_log=debug_dict['output_log'],
        print_console=debug_dict['print_console'],
        suppress_logging=debug_dict['suppress_logging'],
        caller=debug_dict['caller'],
    ) as aiomeraki:

        wireless_tasks = [
            _call_getnetworkwirelesssettings(aiomeraki, wireless, **kwargs) for wireless in all_wireless
            ]
        all_wireless_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(wireless_tasks),
                total=len(wireless_tasks),
                colour='green',
        ):
            wireless_json = await task
            if wireless_json:
                all_wireless_json.extend(iter(wireless_json))
        return all_wireless_json

async def _call_getnetworkwirelesssignalqualityhistory(aiomeraki, wireless, **kwargs):
    try:
        returned_json = await aiomeraki.wireless.getNetworkWirelessSignalQualityHistory(
            networkId=wireless['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=wireless)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=wireless)
        print('Non Meraki API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    if returned_json:

        if isinstance(returned_json, (list)):
            updated_json = []
            for each_dict in returned_json:
                keys_added = add_keys(input_json=wireless, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=wireless, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkwirelesssignalqualityhistory(apikey, debug_dict, all_wireless, **kwargs):
    async with meraki.aio.AsyncDashboardAPI(
        api_key=apikey,
        base_url=debug_dict['base_url'],
        log_file_prefix=debug_dict['log_file_prefix'],
        log_path=debug_dict['log_path'],
        maximum_concurrent_requests=debug_dict['maximum_concurrent_requests'],
        maximum_retries=debug_dict['maximum_retries'],
        wait_on_rate_limit=debug_dict['wait_on_rate_limit'],
        output_log=debug_dict['output_log'],
        print_console=debug_dict['print_console'],
        suppress_logging=debug_dict['suppress_logging'],
        caller=debug_dict['caller'],
    ) as aiomeraki:

        wireless_tasks = [
            _call_getnetworkwirelesssignalqualityhistory(aiomeraki, wireless, **kwargs) for wireless in all_wireless
            ]
        all_wireless_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(wireless_tasks),
                total=len(wireless_tasks),
                colour='green',
        ):
            wireless_json = await task
            if wireless_json:
                all_wireless_json.extend(iter(wireless_json))
        return all_wireless_json

async def _call_getnetworkwirelessssids(aiomeraki, wireless, **kwargs):
    try:
        returned_json = await aiomeraki.wireless.getNetworkWirelessSsids(
            networkId=wireless['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=wireless)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=wireless)
        print('Non Meraki API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    if returned_json:

        if isinstance(returned_json, (list)):
            updated_json = []
            for each_dict in returned_json:
                keys_added = add_keys(input_json=wireless, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=wireless, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkwirelessssids(apikey, debug_dict, all_wireless, **kwargs):
    async with meraki.aio.AsyncDashboardAPI(
        api_key=apikey,
        base_url=debug_dict['base_url'],
        log_file_prefix=debug_dict['log_file_prefix'],
        log_path=debug_dict['log_path'],
        maximum_concurrent_requests=debug_dict['maximum_concurrent_requests'],
        maximum_retries=debug_dict['maximum_retries'],
        wait_on_rate_limit=debug_dict['wait_on_rate_limit'],
        output_log=debug_dict['output_log'],
        print_console=debug_dict['print_console'],
        suppress_logging=debug_dict['suppress_logging'],
        caller=debug_dict['caller'],
    ) as aiomeraki:

        wireless_tasks = [
            _call_getnetworkwirelessssids(aiomeraki, wireless, **kwargs) for wireless in all_wireless
            ]
        all_wireless_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(wireless_tasks),
                total=len(wireless_tasks),
                colour='green',
        ):
            wireless_json = await task
            if wireless_json:
                all_wireless_json.extend(iter(wireless_json))
        return all_wireless_json

async def _call_getnetworkwirelessssid(aiomeraki, wireless, **kwargs):
    try:
        returned_json = await aiomeraki.wireless.getNetworkWirelessSsid(
            networkId=wireless['networkId'],
            number=wireless['number'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=wireless)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=wireless)
        print('Non Meraki API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    if returned_json:

        if isinstance(returned_json, (list)):
            updated_json = []
            for each_dict in returned_json:
                keys_added = add_keys(input_json=wireless, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=wireless, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkwirelessssid(apikey, debug_dict, all_wireless, **kwargs):
    async with meraki.aio.AsyncDashboardAPI(
        api_key=apikey,
        base_url=debug_dict['base_url'],
        log_file_prefix=debug_dict['log_file_prefix'],
        log_path=debug_dict['log_path'],
        maximum_concurrent_requests=debug_dict['maximum_concurrent_requests'],
        maximum_retries=debug_dict['maximum_retries'],
        wait_on_rate_limit=debug_dict['wait_on_rate_limit'],
        output_log=debug_dict['output_log'],
        print_console=debug_dict['print_console'],
        suppress_logging=debug_dict['suppress_logging'],
        caller=debug_dict['caller'],
    ) as aiomeraki:

        wireless_tasks = [
            _call_getnetworkwirelessssid(aiomeraki, wireless, **kwargs) for wireless in all_wireless
            ]
        all_wireless_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(wireless_tasks),
                total=len(wireless_tasks),
                colour='green',
        ):
            wireless_json = await task
            if wireless_json:
                all_wireless_json.extend(iter(wireless_json))
        return all_wireless_json

async def _call_getnetworkwirelessssidbonjourforwarding(aiomeraki, wireless, **kwargs):
    try:
        returned_json = await aiomeraki.wireless.getNetworkWirelessSsidBonjourForwarding(
            networkId=wireless['networkId'],
            number=wireless['number'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=wireless)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=wireless)
        print('Non Meraki API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    if returned_json:

        if isinstance(returned_json, (list)):
            updated_json = []
            for each_dict in returned_json:
                keys_added = add_keys(input_json=wireless, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=wireless, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkwirelessssidbonjourforwarding(apikey, debug_dict, all_wireless, **kwargs):
    async with meraki.aio.AsyncDashboardAPI(
        api_key=apikey,
        base_url=debug_dict['base_url'],
        log_file_prefix=debug_dict['log_file_prefix'],
        log_path=debug_dict['log_path'],
        maximum_concurrent_requests=debug_dict['maximum_concurrent_requests'],
        maximum_retries=debug_dict['maximum_retries'],
        wait_on_rate_limit=debug_dict['wait_on_rate_limit'],
        output_log=debug_dict['output_log'],
        print_console=debug_dict['print_console'],
        suppress_logging=debug_dict['suppress_logging'],
        caller=debug_dict['caller'],
    ) as aiomeraki:

        wireless_tasks = [
            _call_getnetworkwirelessssidbonjourforwarding(aiomeraki, wireless, **kwargs) for wireless in all_wireless
            ]
        all_wireless_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(wireless_tasks),
                total=len(wireless_tasks),
                colour='green',
        ):
            wireless_json = await task
            if wireless_json:
                all_wireless_json.extend(iter(wireless_json))
        return all_wireless_json

async def _call_getnetworkwirelessssiddevicetypegrouppolicies(aiomeraki, wireless, **kwargs):
    try:
        returned_json = await aiomeraki.wireless.getNetworkWirelessSsidDeviceTypeGroupPolicies(
            networkId=wireless['networkId'],
            number=wireless['number'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=wireless)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=wireless)
        print('Non Meraki API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    if returned_json:

        if isinstance(returned_json, (list)):
            updated_json = []
            for each_dict in returned_json:
                keys_added = add_keys(input_json=wireless, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=wireless, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkwirelessssiddevicetypegrouppolicies(apikey, debug_dict, all_wireless, **kwargs):
    async with meraki.aio.AsyncDashboardAPI(
        api_key=apikey,
        base_url=debug_dict['base_url'],
        log_file_prefix=debug_dict['log_file_prefix'],
        log_path=debug_dict['log_path'],
        maximum_concurrent_requests=debug_dict['maximum_concurrent_requests'],
        maximum_retries=debug_dict['maximum_retries'],
        wait_on_rate_limit=debug_dict['wait_on_rate_limit'],
        output_log=debug_dict['output_log'],
        print_console=debug_dict['print_console'],
        suppress_logging=debug_dict['suppress_logging'],
        caller=debug_dict['caller'],
    ) as aiomeraki:

        wireless_tasks = [
            _call_getnetworkwirelessssiddevicetypegrouppolicies(aiomeraki, wireless, **kwargs) for wireless in all_wireless
            ]
        all_wireless_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(wireless_tasks),
                total=len(wireless_tasks),
                colour='green',
        ):
            wireless_json = await task
            if wireless_json:
                all_wireless_json.extend(iter(wireless_json))
        return all_wireless_json

async def _call_getnetworkwirelessssideapoverride(aiomeraki, wireless, **kwargs):
    try:
        returned_json = await aiomeraki.wireless.getNetworkWirelessSsidEapOverride(
            networkId=wireless['networkId'],
            number=wireless['number'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=wireless)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=wireless)
        print('Non Meraki API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    if returned_json:

        if isinstance(returned_json, (list)):
            updated_json = []
            for each_dict in returned_json:
                keys_added = add_keys(input_json=wireless, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=wireless, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkwirelessssideapoverride(apikey, debug_dict, all_wireless, **kwargs):
    async with meraki.aio.AsyncDashboardAPI(
        api_key=apikey,
        base_url=debug_dict['base_url'],
        log_file_prefix=debug_dict['log_file_prefix'],
        log_path=debug_dict['log_path'],
        maximum_concurrent_requests=debug_dict['maximum_concurrent_requests'],
        maximum_retries=debug_dict['maximum_retries'],
        wait_on_rate_limit=debug_dict['wait_on_rate_limit'],
        output_log=debug_dict['output_log'],
        print_console=debug_dict['print_console'],
        suppress_logging=debug_dict['suppress_logging'],
        caller=debug_dict['caller'],
    ) as aiomeraki:

        wireless_tasks = [
            _call_getnetworkwirelessssideapoverride(aiomeraki, wireless, **kwargs) for wireless in all_wireless
            ]
        all_wireless_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(wireless_tasks),
                total=len(wireless_tasks),
                colour='green',
        ):
            wireless_json = await task
            if wireless_json:
                all_wireless_json.extend(iter(wireless_json))
        return all_wireless_json

async def _call_getnetworkwirelessssidfirewalll3firewallrules(aiomeraki, wireless, **kwargs):
    try:
        returned_json = await aiomeraki.wireless.getNetworkWirelessSsidFirewallL3FirewallRules(
            networkId=wireless['networkId'],
            number=wireless['number'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=wireless)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=wireless)
        print('Non Meraki API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    if returned_json:

        if isinstance(returned_json, (list)):
            updated_json = []
            for each_dict in returned_json:
                keys_added = add_keys(input_json=wireless, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=wireless, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkwirelessssidfirewalll3firewallrules(apikey, debug_dict, all_wireless, **kwargs):
    async with meraki.aio.AsyncDashboardAPI(
        api_key=apikey,
        base_url=debug_dict['base_url'],
        log_file_prefix=debug_dict['log_file_prefix'],
        log_path=debug_dict['log_path'],
        maximum_concurrent_requests=debug_dict['maximum_concurrent_requests'],
        maximum_retries=debug_dict['maximum_retries'],
        wait_on_rate_limit=debug_dict['wait_on_rate_limit'],
        output_log=debug_dict['output_log'],
        print_console=debug_dict['print_console'],
        suppress_logging=debug_dict['suppress_logging'],
        caller=debug_dict['caller'],
    ) as aiomeraki:

        wireless_tasks = [
            _call_getnetworkwirelessssidfirewalll3firewallrules(aiomeraki, wireless, **kwargs) for wireless in all_wireless
            ]
        all_wireless_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(wireless_tasks),
                total=len(wireless_tasks),
                colour='green',
        ):
            wireless_json = await task
            if wireless_json:
                all_wireless_json.extend(iter(wireless_json))
        return all_wireless_json

async def _call_getnetworkwirelessssidfirewalll7firewallrules(aiomeraki, wireless, **kwargs):
    try:
        returned_json = await aiomeraki.wireless.getNetworkWirelessSsidFirewallL7FirewallRules(
            networkId=wireless['networkId'],
            number=wireless['number'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=wireless)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=wireless)
        print('Non Meraki API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    if returned_json:

        if isinstance(returned_json, (list)):
            updated_json = []
            for each_dict in returned_json:
                keys_added = add_keys(input_json=wireless, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=wireless, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkwirelessssidfirewalll7firewallrules(apikey, debug_dict, all_wireless, **kwargs):
    async with meraki.aio.AsyncDashboardAPI(
        api_key=apikey,
        base_url=debug_dict['base_url'],
        log_file_prefix=debug_dict['log_file_prefix'],
        log_path=debug_dict['log_path'],
        maximum_concurrent_requests=debug_dict['maximum_concurrent_requests'],
        maximum_retries=debug_dict['maximum_retries'],
        wait_on_rate_limit=debug_dict['wait_on_rate_limit'],
        output_log=debug_dict['output_log'],
        print_console=debug_dict['print_console'],
        suppress_logging=debug_dict['suppress_logging'],
        caller=debug_dict['caller'],
    ) as aiomeraki:

        wireless_tasks = [
            _call_getnetworkwirelessssidfirewalll7firewallrules(aiomeraki, wireless, **kwargs) for wireless in all_wireless
            ]
        all_wireless_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(wireless_tasks),
                total=len(wireless_tasks),
                colour='green',
        ):
            wireless_json = await task
            if wireless_json:
                all_wireless_json.extend(iter(wireless_json))
        return all_wireless_json

async def _call_getnetworkwirelessssidhotspot20(aiomeraki, wireless, **kwargs):
    try:
        returned_json = await aiomeraki.wireless.getNetworkWirelessSsidHotspot20(
            networkId=wireless['networkId'],
            number=wireless['number'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=wireless)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=wireless)
        print('Non Meraki API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    if returned_json:

        if isinstance(returned_json, (list)):
            updated_json = []
            for each_dict in returned_json:
                keys_added = add_keys(input_json=wireless, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=wireless, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkwirelessssidhotspot20(apikey, debug_dict, all_wireless, **kwargs):
    async with meraki.aio.AsyncDashboardAPI(
        api_key=apikey,
        base_url=debug_dict['base_url'],
        log_file_prefix=debug_dict['log_file_prefix'],
        log_path=debug_dict['log_path'],
        maximum_concurrent_requests=debug_dict['maximum_concurrent_requests'],
        maximum_retries=debug_dict['maximum_retries'],
        wait_on_rate_limit=debug_dict['wait_on_rate_limit'],
        output_log=debug_dict['output_log'],
        print_console=debug_dict['print_console'],
        suppress_logging=debug_dict['suppress_logging'],
        caller=debug_dict['caller'],
    ) as aiomeraki:

        wireless_tasks = [
            _call_getnetworkwirelessssidhotspot20(aiomeraki, wireless, **kwargs) for wireless in all_wireless
            ]
        all_wireless_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(wireless_tasks),
                total=len(wireless_tasks),
                colour='green',
        ):
            wireless_json = await task
            if wireless_json:
                all_wireless_json.extend(iter(wireless_json))
        return all_wireless_json

async def _call_getnetworkwirelessssididentitypsks(aiomeraki, wireless, **kwargs):
    try:
        returned_json = await aiomeraki.wireless.getNetworkWirelessSsidIdentityPsks(
            networkId=wireless['networkId'],
            number=wireless['number'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=wireless)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=wireless)
        print('Non Meraki API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    if returned_json:

        if isinstance(returned_json, (list)):
            updated_json = []
            for each_dict in returned_json:
                keys_added = add_keys(input_json=wireless, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=wireless, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkwirelessssididentitypsks(apikey, debug_dict, all_wireless, **kwargs):
    async with meraki.aio.AsyncDashboardAPI(
        api_key=apikey,
        base_url=debug_dict['base_url'],
        log_file_prefix=debug_dict['log_file_prefix'],
        log_path=debug_dict['log_path'],
        maximum_concurrent_requests=debug_dict['maximum_concurrent_requests'],
        maximum_retries=debug_dict['maximum_retries'],
        wait_on_rate_limit=debug_dict['wait_on_rate_limit'],
        output_log=debug_dict['output_log'],
        print_console=debug_dict['print_console'],
        suppress_logging=debug_dict['suppress_logging'],
        caller=debug_dict['caller'],
    ) as aiomeraki:

        wireless_tasks = [
            _call_getnetworkwirelessssididentitypsks(aiomeraki, wireless, **kwargs) for wireless in all_wireless
            ]
        all_wireless_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(wireless_tasks),
                total=len(wireless_tasks),
                colour='green',
        ):
            wireless_json = await task
            if wireless_json:
                all_wireless_json.extend(iter(wireless_json))
        return all_wireless_json

async def _call_getnetworkwirelessssididentitypsk(aiomeraki, wireless, **kwargs):
    try:
        returned_json = await aiomeraki.wireless.getNetworkWirelessSsidIdentityPsk(
            networkId=wireless['networkId'],
            number=wireless['number'],
            identityPskId=wireless['identityPskId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=wireless)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=wireless)
        print('Non Meraki API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    if returned_json:

        if isinstance(returned_json, (list)):
            updated_json = []
            for each_dict in returned_json:
                keys_added = add_keys(input_json=wireless, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=wireless, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkwirelessssididentitypsk(apikey, debug_dict, all_wireless, **kwargs):
    async with meraki.aio.AsyncDashboardAPI(
        api_key=apikey,
        base_url=debug_dict['base_url'],
        log_file_prefix=debug_dict['log_file_prefix'],
        log_path=debug_dict['log_path'],
        maximum_concurrent_requests=debug_dict['maximum_concurrent_requests'],
        maximum_retries=debug_dict['maximum_retries'],
        wait_on_rate_limit=debug_dict['wait_on_rate_limit'],
        output_log=debug_dict['output_log'],
        print_console=debug_dict['print_console'],
        suppress_logging=debug_dict['suppress_logging'],
        caller=debug_dict['caller'],
    ) as aiomeraki:

        wireless_tasks = [
            _call_getnetworkwirelessssididentitypsk(aiomeraki, wireless, **kwargs) for wireless in all_wireless
            ]
        all_wireless_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(wireless_tasks),
                total=len(wireless_tasks),
                colour='green',
        ):
            wireless_json = await task
            if wireless_json:
                all_wireless_json.extend(iter(wireless_json))
        return all_wireless_json

async def _call_getnetworkwirelessssidschedules(aiomeraki, wireless, **kwargs):
    try:
        returned_json = await aiomeraki.wireless.getNetworkWirelessSsidSchedules(
            networkId=wireless['networkId'],
            number=wireless['number'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=wireless)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=wireless)
        print('Non Meraki API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    if returned_json:

        if isinstance(returned_json, (list)):
            updated_json = []
            for each_dict in returned_json:
                keys_added = add_keys(input_json=wireless, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=wireless, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkwirelessssidschedules(apikey, debug_dict, all_wireless, **kwargs):
    async with meraki.aio.AsyncDashboardAPI(
        api_key=apikey,
        base_url=debug_dict['base_url'],
        log_file_prefix=debug_dict['log_file_prefix'],
        log_path=debug_dict['log_path'],
        maximum_concurrent_requests=debug_dict['maximum_concurrent_requests'],
        maximum_retries=debug_dict['maximum_retries'],
        wait_on_rate_limit=debug_dict['wait_on_rate_limit'],
        output_log=debug_dict['output_log'],
        print_console=debug_dict['print_console'],
        suppress_logging=debug_dict['suppress_logging'],
        caller=debug_dict['caller'],
    ) as aiomeraki:

        wireless_tasks = [
            _call_getnetworkwirelessssidschedules(aiomeraki, wireless, **kwargs) for wireless in all_wireless
            ]
        all_wireless_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(wireless_tasks),
                total=len(wireless_tasks),
                colour='green',
        ):
            wireless_json = await task
            if wireless_json:
                all_wireless_json.extend(iter(wireless_json))
        return all_wireless_json

async def _call_getnetworkwirelessssidsplashsettings(aiomeraki, wireless, **kwargs):
    try:
        returned_json = await aiomeraki.wireless.getNetworkWirelessSsidSplashSettings(
            networkId=wireless['networkId'],
            number=wireless['number'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=wireless)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=wireless)
        print('Non Meraki API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    if returned_json:

        if isinstance(returned_json, (list)):
            updated_json = []
            for each_dict in returned_json:
                keys_added = add_keys(input_json=wireless, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=wireless, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkwirelessssidsplashsettings(apikey, debug_dict, all_wireless, **kwargs):
    async with meraki.aio.AsyncDashboardAPI(
        api_key=apikey,
        base_url=debug_dict['base_url'],
        log_file_prefix=debug_dict['log_file_prefix'],
        log_path=debug_dict['log_path'],
        maximum_concurrent_requests=debug_dict['maximum_concurrent_requests'],
        maximum_retries=debug_dict['maximum_retries'],
        wait_on_rate_limit=debug_dict['wait_on_rate_limit'],
        output_log=debug_dict['output_log'],
        print_console=debug_dict['print_console'],
        suppress_logging=debug_dict['suppress_logging'],
        caller=debug_dict['caller'],
    ) as aiomeraki:

        wireless_tasks = [
            _call_getnetworkwirelessssidsplashsettings(aiomeraki, wireless, **kwargs) for wireless in all_wireless
            ]
        all_wireless_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(wireless_tasks),
                total=len(wireless_tasks),
                colour='green',
        ):
            wireless_json = await task
            if wireless_json:
                all_wireless_json.extend(iter(wireless_json))
        return all_wireless_json

async def _call_getnetworkwirelessssidtrafficshapingrules(aiomeraki, wireless, **kwargs):
    try:
        returned_json = await aiomeraki.wireless.getNetworkWirelessSsidTrafficShapingRules(
            networkId=wireless['networkId'],
            number=wireless['number'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=wireless)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=wireless)
        print('Non Meraki API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    if returned_json:

        if isinstance(returned_json, (list)):
            updated_json = []
            for each_dict in returned_json:
                keys_added = add_keys(input_json=wireless, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=wireless, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkwirelessssidtrafficshapingrules(apikey, debug_dict, all_wireless, **kwargs):
    async with meraki.aio.AsyncDashboardAPI(
        api_key=apikey,
        base_url=debug_dict['base_url'],
        log_file_prefix=debug_dict['log_file_prefix'],
        log_path=debug_dict['log_path'],
        maximum_concurrent_requests=debug_dict['maximum_concurrent_requests'],
        maximum_retries=debug_dict['maximum_retries'],
        wait_on_rate_limit=debug_dict['wait_on_rate_limit'],
        output_log=debug_dict['output_log'],
        print_console=debug_dict['print_console'],
        suppress_logging=debug_dict['suppress_logging'],
        caller=debug_dict['caller'],
    ) as aiomeraki:

        wireless_tasks = [
            _call_getnetworkwirelessssidtrafficshapingrules(aiomeraki, wireless, **kwargs) for wireless in all_wireless
            ]
        all_wireless_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(wireless_tasks),
                total=len(wireless_tasks),
                colour='green',
        ):
            wireless_json = await task
            if wireless_json:
                all_wireless_json.extend(iter(wireless_json))
        return all_wireless_json

async def _call_getnetworkwirelessssidvpn(aiomeraki, wireless, **kwargs):
    try:
        returned_json = await aiomeraki.wireless.getNetworkWirelessSsidVpn(
            networkId=wireless['networkId'],
            number=wireless['number'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=wireless)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=wireless)
        print('Non Meraki API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    if returned_json:

        if isinstance(returned_json, (list)):
            updated_json = []
            for each_dict in returned_json:
                keys_added = add_keys(input_json=wireless, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=wireless, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkwirelessssidvpn(apikey, debug_dict, all_wireless, **kwargs):
    async with meraki.aio.AsyncDashboardAPI(
        api_key=apikey,
        base_url=debug_dict['base_url'],
        log_file_prefix=debug_dict['log_file_prefix'],
        log_path=debug_dict['log_path'],
        maximum_concurrent_requests=debug_dict['maximum_concurrent_requests'],
        maximum_retries=debug_dict['maximum_retries'],
        wait_on_rate_limit=debug_dict['wait_on_rate_limit'],
        output_log=debug_dict['output_log'],
        print_console=debug_dict['print_console'],
        suppress_logging=debug_dict['suppress_logging'],
        caller=debug_dict['caller'],
    ) as aiomeraki:

        wireless_tasks = [
            _call_getnetworkwirelessssidvpn(aiomeraki, wireless, **kwargs) for wireless in all_wireless
            ]
        all_wireless_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(wireless_tasks),
                total=len(wireless_tasks),
                colour='green',
        ):
            wireless_json = await task
            if wireless_json:
                all_wireless_json.extend(iter(wireless_json))
        return all_wireless_json

async def _call_getnetworkwirelessusagehistory(aiomeraki, wireless, **kwargs):
    try:
        returned_json = await aiomeraki.wireless.getNetworkWirelessUsageHistory(
            networkId=wireless['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=wireless)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=wireless)
        print('Non Meraki API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    if returned_json:

        if isinstance(returned_json, (list)):
            updated_json = []
            for each_dict in returned_json:
                keys_added = add_keys(input_json=wireless, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=wireless, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkwirelessusagehistory(apikey, debug_dict, all_wireless, **kwargs):
    async with meraki.aio.AsyncDashboardAPI(
        api_key=apikey,
        base_url=debug_dict['base_url'],
        log_file_prefix=debug_dict['log_file_prefix'],
        log_path=debug_dict['log_path'],
        maximum_concurrent_requests=debug_dict['maximum_concurrent_requests'],
        maximum_retries=debug_dict['maximum_retries'],
        wait_on_rate_limit=debug_dict['wait_on_rate_limit'],
        output_log=debug_dict['output_log'],
        print_console=debug_dict['print_console'],
        suppress_logging=debug_dict['suppress_logging'],
        caller=debug_dict['caller'],
    ) as aiomeraki:

        wireless_tasks = [
            _call_getnetworkwirelessusagehistory(aiomeraki, wireless, **kwargs) for wireless in all_wireless
            ]
        all_wireless_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(wireless_tasks),
                total=len(wireless_tasks),
                colour='green',
        ):
            wireless_json = await task
            if wireless_json:
                all_wireless_json.extend(iter(wireless_json))
        return all_wireless_json

async def _call_getorganizationwirelessdeviceschannelutilizationbydevice(aiomeraki, wireless, **kwargs):
    try:
        returned_json = await aiomeraki.wireless.getOrganizationWirelessDevicesChannelUtilizationByDevice(
            organizationId=wireless['organizationId'],
            total_pages='all',
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=wireless)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=wireless)
        print('Non Meraki API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    if returned_json:

        if isinstance(returned_json, (list)):
            updated_json = []
            for each_dict in returned_json:
                keys_added = add_keys(input_json=wireless, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=wireless, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getorganizationwirelessdeviceschannelutilizationbydevice(apikey, debug_dict, all_wireless, **kwargs):
    async with meraki.aio.AsyncDashboardAPI(
        api_key=apikey,
        base_url=debug_dict['base_url'],
        log_file_prefix=debug_dict['log_file_prefix'],
        log_path=debug_dict['log_path'],
        maximum_concurrent_requests=debug_dict['maximum_concurrent_requests'],
        maximum_retries=debug_dict['maximum_retries'],
        wait_on_rate_limit=debug_dict['wait_on_rate_limit'],
        output_log=debug_dict['output_log'],
        print_console=debug_dict['print_console'],
        suppress_logging=debug_dict['suppress_logging'],
        caller=debug_dict['caller'],
    ) as aiomeraki:

        wireless_tasks = [
            _call_getorganizationwirelessdeviceschannelutilizationbydevice(aiomeraki, wireless, **kwargs) for wireless in all_wireless
            ]
        all_wireless_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(wireless_tasks),
                total=len(wireless_tasks),
                colour='green',
        ):
            wireless_json = await task
            if wireless_json:
                all_wireless_json.extend(iter(wireless_json))
        return all_wireless_json

async def _call_getorganizationwirelessdeviceschannelutilizationbynetwork(aiomeraki, wireless, **kwargs):
    try:
        returned_json = await aiomeraki.wireless.getOrganizationWirelessDevicesChannelUtilizationByNetwork(
            organizationId=wireless['organizationId'],
            total_pages='all',
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=wireless)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=wireless)
        print('Non Meraki API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    if returned_json:

        if isinstance(returned_json, (list)):
            updated_json = []
            for each_dict in returned_json:
                keys_added = add_keys(input_json=wireless, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=wireless, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getorganizationwirelessdeviceschannelutilizationbynetwork(apikey, debug_dict, all_wireless, **kwargs):
    async with meraki.aio.AsyncDashboardAPI(
        api_key=apikey,
        base_url=debug_dict['base_url'],
        log_file_prefix=debug_dict['log_file_prefix'],
        log_path=debug_dict['log_path'],
        maximum_concurrent_requests=debug_dict['maximum_concurrent_requests'],
        maximum_retries=debug_dict['maximum_retries'],
        wait_on_rate_limit=debug_dict['wait_on_rate_limit'],
        output_log=debug_dict['output_log'],
        print_console=debug_dict['print_console'],
        suppress_logging=debug_dict['suppress_logging'],
        caller=debug_dict['caller'],
    ) as aiomeraki:

        wireless_tasks = [
            _call_getorganizationwirelessdeviceschannelutilizationbynetwork(aiomeraki, wireless, **kwargs) for wireless in all_wireless
            ]
        all_wireless_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(wireless_tasks),
                total=len(wireless_tasks),
                colour='green',
        ):
            wireless_json = await task
            if wireless_json:
                all_wireless_json.extend(iter(wireless_json))
        return all_wireless_json

async def _call_getorganizationwirelessdeviceschannelutilizationhistorybydevicebyinterval(aiomeraki, wireless, **kwargs):
    try:
        returned_json = await aiomeraki.wireless.getOrganizationWirelessDevicesChannelUtilizationHistoryByDeviceByInterval(
            organizationId=wireless['organizationId'],
            total_pages='all',
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=wireless)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=wireless)
        print('Non Meraki API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    if returned_json:

        if isinstance(returned_json, (list)):
            updated_json = []
            for each_dict in returned_json:
                keys_added = add_keys(input_json=wireless, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=wireless, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getorganizationwirelessdeviceschannelutilizationhistorybydevicebyinterval(apikey, debug_dict, all_wireless, **kwargs):
    async with meraki.aio.AsyncDashboardAPI(
        api_key=apikey,
        base_url=debug_dict['base_url'],
        log_file_prefix=debug_dict['log_file_prefix'],
        log_path=debug_dict['log_path'],
        maximum_concurrent_requests=debug_dict['maximum_concurrent_requests'],
        maximum_retries=debug_dict['maximum_retries'],
        wait_on_rate_limit=debug_dict['wait_on_rate_limit'],
        output_log=debug_dict['output_log'],
        print_console=debug_dict['print_console'],
        suppress_logging=debug_dict['suppress_logging'],
        caller=debug_dict['caller'],
    ) as aiomeraki:

        wireless_tasks = [
            _call_getorganizationwirelessdeviceschannelutilizationhistorybydevicebyinterval(aiomeraki, wireless, **kwargs) for wireless in all_wireless
            ]
        all_wireless_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(wireless_tasks),
                total=len(wireless_tasks),
                colour='green',
        ):
            wireless_json = await task
            if wireless_json:
                all_wireless_json.extend(iter(wireless_json))
        return all_wireless_json

async def _call_getorganizationwirelessdeviceschannelutilizationhistorybynetworkbyinterval(aiomeraki, wireless, **kwargs):
    try:
        returned_json = await aiomeraki.wireless.getOrganizationWirelessDevicesChannelUtilizationHistoryByNetworkByInterval(
            organizationId=wireless['organizationId'],
            total_pages='all',
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=wireless)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=wireless)
        print('Non Meraki API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    if returned_json:

        if isinstance(returned_json, (list)):
            updated_json = []
            for each_dict in returned_json:
                keys_added = add_keys(input_json=wireless, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=wireless, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getorganizationwirelessdeviceschannelutilizationhistorybynetworkbyinterval(apikey, debug_dict, all_wireless, **kwargs):
    async with meraki.aio.AsyncDashboardAPI(
        api_key=apikey,
        base_url=debug_dict['base_url'],
        log_file_prefix=debug_dict['log_file_prefix'],
        log_path=debug_dict['log_path'],
        maximum_concurrent_requests=debug_dict['maximum_concurrent_requests'],
        maximum_retries=debug_dict['maximum_retries'],
        wait_on_rate_limit=debug_dict['wait_on_rate_limit'],
        output_log=debug_dict['output_log'],
        print_console=debug_dict['print_console'],
        suppress_logging=debug_dict['suppress_logging'],
        caller=debug_dict['caller'],
    ) as aiomeraki:

        wireless_tasks = [
            _call_getorganizationwirelessdeviceschannelutilizationhistorybynetworkbyinterval(aiomeraki, wireless, **kwargs) for wireless in all_wireless
            ]
        all_wireless_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(wireless_tasks),
                total=len(wireless_tasks),
                colour='green',
        ):
            wireless_json = await task
            if wireless_json:
                all_wireless_json.extend(iter(wireless_json))
        return all_wireless_json

async def _call_getorganizationwirelessdevicesethernetstatuses(aiomeraki, wireless, **kwargs):
    try:
        returned_json = await aiomeraki.wireless.getOrganizationWirelessDevicesEthernetStatuses(
            organizationId=wireless['organizationId'],
            total_pages='all',
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=wireless)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=wireless)
        print('Non Meraki API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    if returned_json:

        if isinstance(returned_json, (list)):
            updated_json = []
            for each_dict in returned_json:
                keys_added = add_keys(input_json=wireless, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=wireless, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getorganizationwirelessdevicesethernetstatuses(apikey, debug_dict, all_wireless, **kwargs):
    async with meraki.aio.AsyncDashboardAPI(
        api_key=apikey,
        base_url=debug_dict['base_url'],
        log_file_prefix=debug_dict['log_file_prefix'],
        log_path=debug_dict['log_path'],
        maximum_concurrent_requests=debug_dict['maximum_concurrent_requests'],
        maximum_retries=debug_dict['maximum_retries'],
        wait_on_rate_limit=debug_dict['wait_on_rate_limit'],
        output_log=debug_dict['output_log'],
        print_console=debug_dict['print_console'],
        suppress_logging=debug_dict['suppress_logging'],
        caller=debug_dict['caller'],
    ) as aiomeraki:

        wireless_tasks = [
            _call_getorganizationwirelessdevicesethernetstatuses(aiomeraki, wireless, **kwargs) for wireless in all_wireless
            ]
        all_wireless_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(wireless_tasks),
                total=len(wireless_tasks),
                colour='green',
        ):
            wireless_json = await task
            if wireless_json:
                all_wireless_json.extend(iter(wireless_json))
        return all_wireless_json

async def _call_getorganizationwirelessdevicespacketlossbyclient(aiomeraki, wireless, **kwargs):
    try:
        returned_json = await aiomeraki.wireless.getOrganizationWirelessDevicesPacketLossByClient(
            organizationId=wireless['organizationId'],
            total_pages='all',
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=wireless)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=wireless)
        print('Non Meraki API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    if returned_json:

        if isinstance(returned_json, (list)):
            updated_json = []
            for each_dict in returned_json:
                keys_added = add_keys(input_json=wireless, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=wireless, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getorganizationwirelessdevicespacketlossbyclient(apikey, debug_dict, all_wireless, **kwargs):
    async with meraki.aio.AsyncDashboardAPI(
        api_key=apikey,
        base_url=debug_dict['base_url'],
        log_file_prefix=debug_dict['log_file_prefix'],
        log_path=debug_dict['log_path'],
        maximum_concurrent_requests=debug_dict['maximum_concurrent_requests'],
        maximum_retries=debug_dict['maximum_retries'],
        wait_on_rate_limit=debug_dict['wait_on_rate_limit'],
        output_log=debug_dict['output_log'],
        print_console=debug_dict['print_console'],
        suppress_logging=debug_dict['suppress_logging'],
        caller=debug_dict['caller'],
    ) as aiomeraki:

        wireless_tasks = [
            _call_getorganizationwirelessdevicespacketlossbyclient(aiomeraki, wireless, **kwargs) for wireless in all_wireless
            ]
        all_wireless_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(wireless_tasks),
                total=len(wireless_tasks),
                colour='green',
        ):
            wireless_json = await task
            if wireless_json:
                all_wireless_json.extend(iter(wireless_json))
        return all_wireless_json

async def _call_getorganizationwirelessdevicespacketlossbydevice(aiomeraki, wireless, **kwargs):
    try:
        returned_json = await aiomeraki.wireless.getOrganizationWirelessDevicesPacketLossByDevice(
            organizationId=wireless['organizationId'],
            total_pages='all',
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=wireless)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=wireless)
        print('Non Meraki API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    if returned_json:

        if isinstance(returned_json, (list)):
            updated_json = []
            for each_dict in returned_json:
                keys_added = add_keys(input_json=wireless, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=wireless, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getorganizationwirelessdevicespacketlossbydevice(apikey, debug_dict, all_wireless, **kwargs):
    async with meraki.aio.AsyncDashboardAPI(
        api_key=apikey,
        base_url=debug_dict['base_url'],
        log_file_prefix=debug_dict['log_file_prefix'],
        log_path=debug_dict['log_path'],
        maximum_concurrent_requests=debug_dict['maximum_concurrent_requests'],
        maximum_retries=debug_dict['maximum_retries'],
        wait_on_rate_limit=debug_dict['wait_on_rate_limit'],
        output_log=debug_dict['output_log'],
        print_console=debug_dict['print_console'],
        suppress_logging=debug_dict['suppress_logging'],
        caller=debug_dict['caller'],
    ) as aiomeraki:

        wireless_tasks = [
            _call_getorganizationwirelessdevicespacketlossbydevice(aiomeraki, wireless, **kwargs) for wireless in all_wireless
            ]
        all_wireless_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(wireless_tasks),
                total=len(wireless_tasks),
                colour='green',
        ):
            wireless_json = await task
            if wireless_json:
                all_wireless_json.extend(iter(wireless_json))
        return all_wireless_json

async def _call_getorganizationwirelessdevicespacketlossbynetwork(aiomeraki, wireless, **kwargs):
    try:
        returned_json = await aiomeraki.wireless.getOrganizationWirelessDevicesPacketLossByNetwork(
            organizationId=wireless['organizationId'],
            total_pages='all',
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=wireless)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=wireless)
        print('Non Meraki API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    if returned_json:

        if isinstance(returned_json, (list)):
            updated_json = []
            for each_dict in returned_json:
                keys_added = add_keys(input_json=wireless, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=wireless, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getorganizationwirelessdevicespacketlossbynetwork(apikey, debug_dict, all_wireless, **kwargs):
    async with meraki.aio.AsyncDashboardAPI(
        api_key=apikey,
        base_url=debug_dict['base_url'],
        log_file_prefix=debug_dict['log_file_prefix'],
        log_path=debug_dict['log_path'],
        maximum_concurrent_requests=debug_dict['maximum_concurrent_requests'],
        maximum_retries=debug_dict['maximum_retries'],
        wait_on_rate_limit=debug_dict['wait_on_rate_limit'],
        output_log=debug_dict['output_log'],
        print_console=debug_dict['print_console'],
        suppress_logging=debug_dict['suppress_logging'],
        caller=debug_dict['caller'],
    ) as aiomeraki:

        wireless_tasks = [
            _call_getorganizationwirelessdevicespacketlossbynetwork(aiomeraki, wireless, **kwargs) for wireless in all_wireless
            ]
        all_wireless_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(wireless_tasks),
                total=len(wireless_tasks),
                colour='green',
        ):
            wireless_json = await task
            if wireless_json:
                all_wireless_json.extend(iter(wireless_json))
        return all_wireless_json
