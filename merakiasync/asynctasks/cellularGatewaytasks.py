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

async def _call_getdevicecellulargatewaylan(aiomeraki, cellularGateway, **kwargs):
    try:
        returned_json = await aiomeraki.cellularGateway.getDeviceCellularGatewayLan(
            serial=cellularGateway['serial'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=cellularGateway)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=cellularGateway)
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
                keys_added = add_keys(input_json=cellularGateway, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=cellularGateway, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getdevicecellulargatewaylan(apikey, debug_dict, cellularGateways, **kwargs):
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

        cellularGateway_tasks = [
            _call_getdevicecellulargatewaylan(aiomeraki, cellularGateway, **kwargs) for cellularGateway in cellularGateways
            ]
        all_cellularGateway_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(cellularGateway_tasks),
                total=len(cellularGateway_tasks),
                colour='green',
        ):
            cellularGateway_json = await task
            if cellularGateway_json:
                all_cellularGateway_json.extend(iter(cellularGateway_json))
        return all_cellularGateway_json

async def _call_getdevicecellulargatewayportforwardingrules(aiomeraki, cellularGateway, **kwargs):
    try:
        returned_json = await aiomeraki.cellularGateway.getDeviceCellularGatewayPortForwardingRules(
            serial=cellularGateway['serial'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=cellularGateway)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=cellularGateway)
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
                keys_added = add_keys(input_json=cellularGateway, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=cellularGateway, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getdevicecellulargatewayportforwardingrules(apikey, debug_dict, cellularGateways, **kwargs):
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

        cellularGateway_tasks = [
            _call_getdevicecellulargatewayportforwardingrules(aiomeraki, cellularGateway, **kwargs) for cellularGateway in cellularGateways
            ]
        all_cellularGateway_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(cellularGateway_tasks),
                total=len(cellularGateway_tasks),
                colour='green',
        ):
            cellularGateway_json = await task
            if cellularGateway_json:
                all_cellularGateway_json.extend(iter(cellularGateway_json))
        return all_cellularGateway_json

async def _call_getnetworkcellulargatewayconnectivitymonitoringdestinations(aiomeraki, cellularGateway, **kwargs):
    try:
        returned_json = await aiomeraki.cellularGateway.getNetworkCellularGatewayConnectivityMonitoringDestinations(
            networkId=cellularGateway['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=cellularGateway)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=cellularGateway)
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
                keys_added = add_keys(input_json=cellularGateway, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=cellularGateway, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkcellulargatewayconnectivitymonitoringdestinations(apikey, debug_dict, cellularGateways, **kwargs):
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

        cellularGateway_tasks = [
            _call_getnetworkcellulargatewayconnectivitymonitoringdestinations(aiomeraki, cellularGateway, **kwargs) for cellularGateway in cellularGateways
            ]
        all_cellularGateway_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(cellularGateway_tasks),
                total=len(cellularGateway_tasks),
                colour='green',
        ):
            cellularGateway_json = await task
            if cellularGateway_json:
                all_cellularGateway_json.extend(iter(cellularGateway_json))
        return all_cellularGateway_json

async def _call_getnetworkcellulargatewaydhcp(aiomeraki, cellularGateway, **kwargs):
    try:
        returned_json = await aiomeraki.cellularGateway.getNetworkCellularGatewayDhcp(
            networkId=cellularGateway['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=cellularGateway)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=cellularGateway)
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
                keys_added = add_keys(input_json=cellularGateway, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=cellularGateway, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkcellulargatewaydhcp(apikey, debug_dict, cellularGateways, **kwargs):
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

        cellularGateway_tasks = [
            _call_getnetworkcellulargatewaydhcp(aiomeraki, cellularGateway, **kwargs) for cellularGateway in cellularGateways
            ]
        all_cellularGateway_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(cellularGateway_tasks),
                total=len(cellularGateway_tasks),
                colour='green',
        ):
            cellularGateway_json = await task
            if cellularGateway_json:
                all_cellularGateway_json.extend(iter(cellularGateway_json))
        return all_cellularGateway_json

async def _call_getnetworkcellulargatewaysubnetpool(aiomeraki, cellularGateway, **kwargs):
    try:
        returned_json = await aiomeraki.cellularGateway.getNetworkCellularGatewaySubnetPool(
            networkId=cellularGateway['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=cellularGateway)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=cellularGateway)
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
                keys_added = add_keys(input_json=cellularGateway, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=cellularGateway, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkcellulargatewaysubnetpool(apikey, debug_dict, cellularGateways, **kwargs):
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

        cellularGateway_tasks = [
            _call_getnetworkcellulargatewaysubnetpool(aiomeraki, cellularGateway, **kwargs) for cellularGateway in cellularGateways
            ]
        all_cellularGateway_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(cellularGateway_tasks),
                total=len(cellularGateway_tasks),
                colour='green',
        ):
            cellularGateway_json = await task
            if cellularGateway_json:
                all_cellularGateway_json.extend(iter(cellularGateway_json))
        return all_cellularGateway_json

async def _call_getnetworkcellulargatewayuplink(aiomeraki, cellularGateway, **kwargs):
    try:
        returned_json = await aiomeraki.cellularGateway.getNetworkCellularGatewayUplink(
            networkId=cellularGateway['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=cellularGateway)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=cellularGateway)
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
                keys_added = add_keys(input_json=cellularGateway, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=cellularGateway, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkcellulargatewayuplink(apikey, debug_dict, cellularGateways, **kwargs):
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

        cellularGateway_tasks = [
            _call_getnetworkcellulargatewayuplink(aiomeraki, cellularGateway, **kwargs) for cellularGateway in cellularGateways
            ]
        all_cellularGateway_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(cellularGateway_tasks),
                total=len(cellularGateway_tasks),
                colour='green',
        ):
            cellularGateway_json = await task
            if cellularGateway_json:
                all_cellularGateway_json.extend(iter(cellularGateway_json))
        return all_cellularGateway_json

async def _call_getorganizationcellulargatewayuplinkstatuses(aiomeraki, cellularGateway, **kwargs):
    try:
        returned_json = await aiomeraki.cellularGateway.getOrganizationCellularGatewayUplinkStatuses(
            organizationId=cellularGateway['organizationId'],
            total_pages='all',
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=cellularGateway)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=cellularGateway)
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
                keys_added = add_keys(input_json=cellularGateway, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=cellularGateway, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getorganizationcellulargatewayuplinkstatuses(apikey, debug_dict, cellularGateways, **kwargs):
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

        cellularGateway_tasks = [
            _call_getorganizationcellulargatewayuplinkstatuses(aiomeraki, cellularGateway, **kwargs) for cellularGateway in cellularGateways
            ]
        all_cellularGateway_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(cellularGateway_tasks),
                total=len(cellularGateway_tasks),
                colour='green',
        ):
            cellularGateway_json = await task
            if cellularGateway_json:
                all_cellularGateway_json.extend(iter(cellularGateway_json))
        return all_cellularGateway_json
