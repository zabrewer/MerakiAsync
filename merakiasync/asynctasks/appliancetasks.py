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

async def _call_getdeviceappliancedhcpsubnets(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getDeviceApplianceDhcpSubnets(
            serial=appliance['serial'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getdeviceappliancedhcpsubnets(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getdeviceappliancedhcpsubnets(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getdeviceapplianceperformance(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getDeviceAppliancePerformance(
            serial=appliance['serial'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getdeviceapplianceperformance(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getdeviceapplianceperformance(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getdeviceapplianceprefixesdelegated(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getDeviceAppliancePrefixesDelegated(
            serial=appliance['serial'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getdeviceapplianceprefixesdelegated(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getdeviceapplianceprefixesdelegated(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getdeviceapplianceprefixesdelegatedvlanassignments(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getDeviceAppliancePrefixesDelegatedVlanAssignments(
            serial=appliance['serial'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getdeviceapplianceprefixesdelegatedvlanassignments(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getdeviceapplianceprefixesdelegatedvlanassignments(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getdeviceapplianceradiosettings(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getDeviceApplianceRadioSettings(
            serial=appliance['serial'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getdeviceapplianceradiosettings(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getdeviceapplianceradiosettings(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getdeviceapplianceuplinkssettings(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getDeviceApplianceUplinksSettings(
            serial=appliance['serial'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getdeviceapplianceuplinkssettings(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getdeviceapplianceuplinkssettings(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getnetworkapplianceclientsecurityevents(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getNetworkApplianceClientSecurityEvents(
            networkId=appliance['networkId'],
            clientId=appliance['clientId'],
            total_pages='all',
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkapplianceclientsecurityevents(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getnetworkapplianceclientsecurityevents(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getnetworkapplianceconnectivitymonitoringdestinations(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getNetworkApplianceConnectivityMonitoringDestinations(
            networkId=appliance['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkapplianceconnectivitymonitoringdestinations(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getnetworkapplianceconnectivitymonitoringdestinations(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getnetworkappliancecontentfiltering(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getNetworkApplianceContentFiltering(
            networkId=appliance['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkappliancecontentfiltering(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getnetworkappliancecontentfiltering(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getnetworkappliancecontentfilteringcategories(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getNetworkApplianceContentFilteringCategories(
            networkId=appliance['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkappliancecontentfilteringcategories(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getnetworkappliancecontentfilteringcategories(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getnetworkappliancefirewallcellularfirewallrules(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getNetworkApplianceFirewallCellularFirewallRules(
            networkId=appliance['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkappliancefirewallcellularfirewallrules(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getnetworkappliancefirewallcellularfirewallrules(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getnetworkappliancefirewallfirewalledservices(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getNetworkApplianceFirewallFirewalledServices(
            networkId=appliance['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkappliancefirewallfirewalledservices(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getnetworkappliancefirewallfirewalledservices(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getnetworkappliancefirewallfirewalledservice(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getNetworkApplianceFirewallFirewalledService(
            networkId=appliance['networkId'],
            service=appliance['service'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkappliancefirewallfirewalledservice(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getnetworkappliancefirewallfirewalledservice(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getnetworkappliancefirewallinboundcellularfirewallrules(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getNetworkApplianceFirewallInboundCellularFirewallRules(
            networkId=appliance['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkappliancefirewallinboundcellularfirewallrules(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getnetworkappliancefirewallinboundcellularfirewallrules(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getnetworkappliancefirewallinboundfirewallrules(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getNetworkApplianceFirewallInboundFirewallRules(
            networkId=appliance['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkappliancefirewallinboundfirewallrules(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getnetworkappliancefirewallinboundfirewallrules(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getnetworkappliancefirewalll3firewallrules(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getNetworkApplianceFirewallL3FirewallRules(
            networkId=appliance['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkappliancefirewalll3firewallrules(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getnetworkappliancefirewalll3firewallrules(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getnetworkappliancefirewalll7firewallrules(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getNetworkApplianceFirewallL7FirewallRules(
            networkId=appliance['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkappliancefirewalll7firewallrules(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getnetworkappliancefirewalll7firewallrules(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getnetworkappliancefirewalll7firewallrulesapplicationcategories(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getNetworkApplianceFirewallL7FirewallRulesApplicationCategories(
            networkId=appliance['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkappliancefirewalll7firewallrulesapplicationcategories(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getnetworkappliancefirewalll7firewallrulesapplicationcategories(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getnetworkappliancefirewallonetomanynatrules(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getNetworkApplianceFirewallOneToManyNatRules(
            networkId=appliance['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkappliancefirewallonetomanynatrules(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getnetworkappliancefirewallonetomanynatrules(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getnetworkappliancefirewallonetoonenatrules(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getNetworkApplianceFirewallOneToOneNatRules(
            networkId=appliance['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkappliancefirewallonetoonenatrules(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getnetworkappliancefirewallonetoonenatrules(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getnetworkappliancefirewallportforwardingrules(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getNetworkApplianceFirewallPortForwardingRules(
            networkId=appliance['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkappliancefirewallportforwardingrules(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getnetworkappliancefirewallportforwardingrules(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getnetworkappliancefirewallsettings(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getNetworkApplianceFirewallSettings(
            networkId=appliance['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkappliancefirewallsettings(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getnetworkappliancefirewallsettings(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getnetworkapplianceports(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getNetworkAppliancePorts(
            networkId=appliance['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkapplianceports(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getnetworkapplianceports(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getnetworkapplianceport(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getNetworkAppliancePort(
            networkId=appliance['networkId'],
            portId=appliance['portId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkapplianceport(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getnetworkapplianceport(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getnetworkapplianceprefixesdelegatedstatics(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getNetworkAppliancePrefixesDelegatedStatics(
            networkId=appliance['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkapplianceprefixesdelegatedstatics(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getnetworkapplianceprefixesdelegatedstatics(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getnetworkapplianceprefixesdelegatedstatic(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getNetworkAppliancePrefixesDelegatedStatic(
            networkId=appliance['networkId'],
            staticDelegatedPrefixId=appliance['staticDelegatedPrefixId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkapplianceprefixesdelegatedstatic(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getnetworkapplianceprefixesdelegatedstatic(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getnetworkappliancerfprofiles(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getNetworkApplianceRfProfiles(
            networkId=appliance['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkappliancerfprofiles(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getnetworkappliancerfprofiles(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getnetworkappliancerfprofile(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getNetworkApplianceRfProfile(
            networkId=appliance['networkId'],
            rfProfileId=appliance['rfProfileId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkappliancerfprofile(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getnetworkappliancerfprofile(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getnetworkappliancesecurityevents(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getNetworkApplianceSecurityEvents(
            networkId=appliance['networkId'],
            total_pages='all',
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkappliancesecurityevents(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getnetworkappliancesecurityevents(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getnetworkappliancesecurityintrusion(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getNetworkApplianceSecurityIntrusion(
            networkId=appliance['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkappliancesecurityintrusion(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getnetworkappliancesecurityintrusion(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getnetworkappliancesecuritymalware(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getNetworkApplianceSecurityMalware(
            networkId=appliance['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkappliancesecuritymalware(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getnetworkappliancesecuritymalware(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getnetworkappliancesettings(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getNetworkApplianceSettings(
            networkId=appliance['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkappliancesettings(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getnetworkappliancesettings(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getnetworkappliancesinglelan(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getNetworkApplianceSingleLan(
            networkId=appliance['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkappliancesinglelan(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getnetworkappliancesinglelan(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getnetworkappliancessids(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getNetworkApplianceSsids(
            networkId=appliance['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkappliancessids(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getnetworkappliancessids(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getnetworkappliancessid(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getNetworkApplianceSsid(
            networkId=appliance['networkId'],
            number=appliance['number'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkappliancessid(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getnetworkappliancessid(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getnetworkappliancestaticroutes(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getNetworkApplianceStaticRoutes(
            networkId=appliance['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkappliancestaticroutes(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getnetworkappliancestaticroutes(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getnetworkappliancestaticroute(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getNetworkApplianceStaticRoute(
            networkId=appliance['networkId'],
            staticRouteId=appliance['staticRouteId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkappliancestaticroute(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getnetworkappliancestaticroute(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getnetworkappliancetrafficshaping(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getNetworkApplianceTrafficShaping(
            networkId=appliance['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkappliancetrafficshaping(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getnetworkappliancetrafficshaping(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getnetworkappliancetrafficshapingcustomperformanceclasses(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getNetworkApplianceTrafficShapingCustomPerformanceClasses(
            networkId=appliance['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkappliancetrafficshapingcustomperformanceclasses(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getnetworkappliancetrafficshapingcustomperformanceclasses(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getnetworkappliancetrafficshapingcustomperformanceclass(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getNetworkApplianceTrafficShapingCustomPerformanceClass(
            networkId=appliance['networkId'],
            customPerformanceClassId=appliance['customPerformanceClassId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkappliancetrafficshapingcustomperformanceclass(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getnetworkappliancetrafficshapingcustomperformanceclass(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getnetworkappliancetrafficshapingrules(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getNetworkApplianceTrafficShapingRules(
            networkId=appliance['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkappliancetrafficshapingrules(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getnetworkappliancetrafficshapingrules(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getnetworkappliancetrafficshapinguplinkbandwidth(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getNetworkApplianceTrafficShapingUplinkBandwidth(
            networkId=appliance['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkappliancetrafficshapinguplinkbandwidth(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getnetworkappliancetrafficshapinguplinkbandwidth(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getnetworkappliancetrafficshapinguplinkselection(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getNetworkApplianceTrafficShapingUplinkSelection(
            networkId=appliance['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkappliancetrafficshapinguplinkselection(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getnetworkappliancetrafficshapinguplinkselection(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getnetworkapplianceuplinksusagehistory(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getNetworkApplianceUplinksUsageHistory(
            networkId=appliance['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkapplianceuplinksusagehistory(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getnetworkapplianceuplinksusagehistory(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getnetworkappliancevlans(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getNetworkApplianceVlans(
            networkId=appliance['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkappliancevlans(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getnetworkappliancevlans(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getnetworkappliancevlanssettings(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getNetworkApplianceVlansSettings(
            networkId=appliance['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkappliancevlanssettings(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getnetworkappliancevlanssettings(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getnetworkappliancevlan(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getNetworkApplianceVlan(
            networkId=appliance['networkId'],
            vlanId=appliance['vlanId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkappliancevlan(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getnetworkappliancevlan(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getnetworkappliancevpnbgp(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getNetworkApplianceVpnBgp(
            networkId=appliance['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkappliancevpnbgp(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getnetworkappliancevpnbgp(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getnetworkappliancevpnsitetositevpn(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getNetworkApplianceVpnSiteToSiteVpn(
            networkId=appliance['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkappliancevpnsitetositevpn(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getnetworkappliancevpnsitetositevpn(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getnetworkappliancewarmspare(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getNetworkApplianceWarmSpare(
            networkId=appliance['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkappliancewarmspare(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getnetworkappliancewarmspare(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getorganizationappliancesecurityevents(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getOrganizationApplianceSecurityEvents(
            organizationId=appliance['organizationId'],
            total_pages='all',
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getorganizationappliancesecurityevents(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getorganizationappliancesecurityevents(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getorganizationappliancesecurityintrusion(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getOrganizationApplianceSecurityIntrusion(
            organizationId=appliance['organizationId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getorganizationappliancesecurityintrusion(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getorganizationappliancesecurityintrusion(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getorganizationappliancetrafficshapingvpnexclusionsbynetwork(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getOrganizationApplianceTrafficShapingVpnExclusionsByNetwork(
            organizationId=appliance['organizationId'],
            total_pages='all',
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getorganizationappliancetrafficshapingvpnexclusionsbynetwork(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getorganizationappliancetrafficshapingvpnexclusionsbynetwork(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getorganizationapplianceuplinkstatuses(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getOrganizationApplianceUplinkStatuses(
            organizationId=appliance['organizationId'],
            total_pages='all',
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getorganizationapplianceuplinkstatuses(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getorganizationapplianceuplinkstatuses(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getorganizationapplianceuplinksstatusesoverview(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getOrganizationApplianceUplinksStatusesOverview(
            organizationId=appliance['organizationId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getorganizationapplianceuplinksstatusesoverview(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getorganizationapplianceuplinksstatusesoverview(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getorganizationapplianceuplinksusagebynetwork(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getOrganizationApplianceUplinksUsageByNetwork(
            organizationId=appliance['organizationId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getorganizationapplianceuplinksusagebynetwork(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getorganizationapplianceuplinksusagebynetwork(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getorganizationappliancevpnstats(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getOrganizationApplianceVpnStats(
            organizationId=appliance['organizationId'],
            total_pages='all',
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getorganizationappliancevpnstats(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getorganizationappliancevpnstats(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getorganizationappliancevpnstatuses(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getOrganizationApplianceVpnStatuses(
            organizationId=appliance['organizationId'],
            total_pages='all',
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getorganizationappliancevpnstatuses(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getorganizationappliancevpnstatuses(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getorganizationappliancevpnthirdpartyvpnpeers(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getOrganizationApplianceVpnThirdPartyVPNPeers(
            organizationId=appliance['organizationId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getorganizationappliancevpnthirdpartyvpnpeers(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getorganizationappliancevpnthirdpartyvpnpeers(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json

async def _call_getorganizationappliancevpnvpnfirewallrules(aiomeraki, appliance, **kwargs):
    try:
        returned_json = await aiomeraki.appliance.getOrganizationApplianceVpnVpnFirewallRules(
            organizationId=appliance['organizationId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=appliance)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=appliance)
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
                keys_added = add_keys(input_json=appliance, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=appliance, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getorganizationappliancevpnvpnfirewallrules(apikey, debug_dict, appliances, **kwargs):
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

        appliance_tasks = [
            _call_getorganizationappliancevpnvpnfirewallrules(aiomeraki, appliance, **kwargs) for appliance in appliances
            ]
        all_appliance_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(appliance_tasks),
                total=len(appliance_tasks),
                colour='green',
        ):
            appliance_json = await task
            if appliance_json:
                all_appliance_json.extend(iter(appliance_json))
        return all_appliance_json
