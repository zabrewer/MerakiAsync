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

async def _call_getnetwork(aiomeraki, network, **kwargs):
    try:
        returned_json = await aiomeraki.networks.getNetwork(
            networkId=network['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=network)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=network)
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
                keys_added = add_keys(input_json=network, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=network, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetwork(apikey, debug_dict, networks, **kwargs):
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

        network_tasks = [
            _call_getnetwork(aiomeraki, network, **kwargs) for network in networks
            ]
        all_network_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(network_tasks),
                total=len(network_tasks),
                colour='green',
        ):
            network_json = await task
            if network_json:
                all_network_json.extend(iter(network_json))
        return all_network_json

async def _call_getnetworkalertshistory(aiomeraki, network, **kwargs):
    try:
        returned_json = await aiomeraki.networks.getNetworkAlertsHistory(
            networkId=network['networkId'],
            total_pages='all',
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=network)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=network)
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
                keys_added = add_keys(input_json=network, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=network, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkalertshistory(apikey, debug_dict, networks, **kwargs):
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

        network_tasks = [
            _call_getnetworkalertshistory(aiomeraki, network, **kwargs) for network in networks
            ]
        all_network_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(network_tasks),
                total=len(network_tasks),
                colour='green',
        ):
            network_json = await task
            if network_json:
                all_network_json.extend(iter(network_json))
        return all_network_json

async def _call_getnetworkalertssettings(aiomeraki, network, **kwargs):
    try:
        returned_json = await aiomeraki.networks.getNetworkAlertsSettings(
            networkId=network['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=network)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=network)
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
                keys_added = add_keys(input_json=network, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=network, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkalertssettings(apikey, debug_dict, networks, **kwargs):
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

        network_tasks = [
            _call_getnetworkalertssettings(aiomeraki, network, **kwargs) for network in networks
            ]
        all_network_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(network_tasks),
                total=len(network_tasks),
                colour='green',
        ):
            network_json = await task
            if network_json:
                all_network_json.extend(iter(network_json))
        return all_network_json

async def _call_getnetworkbluetoothclients(aiomeraki, network, **kwargs):
    try:
        returned_json = await aiomeraki.networks.getNetworkBluetoothClients(
            networkId=network['networkId'],
            total_pages='all',
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=network)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=network)
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
                keys_added = add_keys(input_json=network, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=network, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkbluetoothclients(apikey, debug_dict, networks, **kwargs):
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

        network_tasks = [
            _call_getnetworkbluetoothclients(aiomeraki, network, **kwargs) for network in networks
            ]
        all_network_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(network_tasks),
                total=len(network_tasks),
                colour='green',
        ):
            network_json = await task
            if network_json:
                all_network_json.extend(iter(network_json))
        return all_network_json

async def _call_getnetworkbluetoothclient(aiomeraki, network, **kwargs):
    try:
        returned_json = await aiomeraki.networks.getNetworkBluetoothClient(
            networkId=network['networkId'],
            bluetoothClientId=network['bluetoothClientId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=network)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=network)
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
                keys_added = add_keys(input_json=network, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=network, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkbluetoothclient(apikey, debug_dict, networks, **kwargs):
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

        network_tasks = [
            _call_getnetworkbluetoothclient(aiomeraki, network, **kwargs) for network in networks
            ]
        all_network_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(network_tasks),
                total=len(network_tasks),
                colour='green',
        ):
            network_json = await task
            if network_json:
                all_network_json.extend(iter(network_json))
        return all_network_json

async def _call_getnetworkclients(aiomeraki, network, **kwargs):
    try:
        returned_json = await aiomeraki.networks.getNetworkClients(
            networkId=network['networkId'],
            total_pages='all',
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=network)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=network)
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
                keys_added = add_keys(input_json=network, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=network, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkclients(apikey, debug_dict, networks, **kwargs):
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

        network_tasks = [
            _call_getnetworkclients(aiomeraki, network, **kwargs) for network in networks
            ]
        all_network_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(network_tasks),
                total=len(network_tasks),
                colour='green',
        ):
            network_json = await task
            if network_json:
                all_network_json.extend(iter(network_json))
        return all_network_json

async def _call_getnetworkclientsapplicationusage(aiomeraki, network, **kwargs):
    try:
        returned_json = await aiomeraki.networks.getNetworkClientsApplicationUsage(
            networkId=network['networkId'],
            clients=network['clients'],
            total_pages='all',
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=network)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=network)
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
                keys_added = add_keys(input_json=network, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=network, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkclientsapplicationusage(apikey, debug_dict, networks, **kwargs):
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

        network_tasks = [
            _call_getnetworkclientsapplicationusage(aiomeraki, network, **kwargs) for network in networks
            ]
        all_network_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(network_tasks),
                total=len(network_tasks),
                colour='green',
        ):
            network_json = await task
            if network_json:
                all_network_json.extend(iter(network_json))
        return all_network_json

async def _call_getnetworkclientsbandwidthusagehistory(aiomeraki, network, **kwargs):
    try:
        returned_json = await aiomeraki.networks.getNetworkClientsBandwidthUsageHistory(
            networkId=network['networkId'],
            total_pages='all',
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=network)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=network)
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
                keys_added = add_keys(input_json=network, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=network, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkclientsbandwidthusagehistory(apikey, debug_dict, networks, **kwargs):
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

        network_tasks = [
            _call_getnetworkclientsbandwidthusagehistory(aiomeraki, network, **kwargs) for network in networks
            ]
        all_network_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(network_tasks),
                total=len(network_tasks),
                colour='green',
        ):
            network_json = await task
            if network_json:
                all_network_json.extend(iter(network_json))
        return all_network_json

async def _call_getnetworkclientsoverview(aiomeraki, network, **kwargs):
    try:
        returned_json = await aiomeraki.networks.getNetworkClientsOverview(
            networkId=network['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=network)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=network)
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
                keys_added = add_keys(input_json=network, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=network, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkclientsoverview(apikey, debug_dict, networks, **kwargs):
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

        network_tasks = [
            _call_getnetworkclientsoverview(aiomeraki, network, **kwargs) for network in networks
            ]
        all_network_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(network_tasks),
                total=len(network_tasks),
                colour='green',
        ):
            network_json = await task
            if network_json:
                all_network_json.extend(iter(network_json))
        return all_network_json

async def _call_getnetworkclientsusagehistories(aiomeraki, network, **kwargs):
    try:
        returned_json = await aiomeraki.networks.getNetworkClientsUsageHistories(
            networkId=network['networkId'],
            clients=network['clients'],
            total_pages='all',
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=network)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=network)
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
                keys_added = add_keys(input_json=network, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=network, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkclientsusagehistories(apikey, debug_dict, networks, **kwargs):
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

        network_tasks = [
            _call_getnetworkclientsusagehistories(aiomeraki, network, **kwargs) for network in networks
            ]
        all_network_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(network_tasks),
                total=len(network_tasks),
                colour='green',
        ):
            network_json = await task
            if network_json:
                all_network_json.extend(iter(network_json))
        return all_network_json

async def _call_getnetworkclient(aiomeraki, network, **kwargs):
    try:
        returned_json = await aiomeraki.networks.getNetworkClient(
            networkId=network['networkId'],
            clientId=network['clientId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=network)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=network)
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
                keys_added = add_keys(input_json=network, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=network, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkclient(apikey, debug_dict, networks, **kwargs):
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

        network_tasks = [
            _call_getnetworkclient(aiomeraki, network, **kwargs) for network in networks
            ]
        all_network_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(network_tasks),
                total=len(network_tasks),
                colour='green',
        ):
            network_json = await task
            if network_json:
                all_network_json.extend(iter(network_json))
        return all_network_json

async def _call_getnetworkclientpolicy(aiomeraki, network, **kwargs):
    try:
        returned_json = await aiomeraki.networks.getNetworkClientPolicy(
            networkId=network['networkId'],
            clientId=network['clientId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=network)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=network)
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
                keys_added = add_keys(input_json=network, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=network, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkclientpolicy(apikey, debug_dict, networks, **kwargs):
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

        network_tasks = [
            _call_getnetworkclientpolicy(aiomeraki, network, **kwargs) for network in networks
            ]
        all_network_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(network_tasks),
                total=len(network_tasks),
                colour='green',
        ):
            network_json = await task
            if network_json:
                all_network_json.extend(iter(network_json))
        return all_network_json

async def _call_getnetworkclientsplashauthorizationstatus(aiomeraki, network, **kwargs):
    try:
        returned_json = await aiomeraki.networks.getNetworkClientSplashAuthorizationStatus(
            networkId=network['networkId'],
            clientId=network['clientId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=network)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=network)
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
                keys_added = add_keys(input_json=network, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=network, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkclientsplashauthorizationstatus(apikey, debug_dict, networks, **kwargs):
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

        network_tasks = [
            _call_getnetworkclientsplashauthorizationstatus(aiomeraki, network, **kwargs) for network in networks
            ]
        all_network_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(network_tasks),
                total=len(network_tasks),
                colour='green',
        ):
            network_json = await task
            if network_json:
                all_network_json.extend(iter(network_json))
        return all_network_json

async def _call_getnetworkclienttraffichistory(aiomeraki, network, **kwargs):
    try:
        returned_json = await aiomeraki.networks.getNetworkClientTrafficHistory(
            networkId=network['networkId'],
            clientId=network['clientId'],
            total_pages='all',
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=network)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=network)
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
                keys_added = add_keys(input_json=network, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=network, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkclienttraffichistory(apikey, debug_dict, networks, **kwargs):
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

        network_tasks = [
            _call_getnetworkclienttraffichistory(aiomeraki, network, **kwargs) for network in networks
            ]
        all_network_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(network_tasks),
                total=len(network_tasks),
                colour='green',
        ):
            network_json = await task
            if network_json:
                all_network_json.extend(iter(network_json))
        return all_network_json

async def _call_getnetworkclientusagehistory(aiomeraki, network, **kwargs):
    try:
        returned_json = await aiomeraki.networks.getNetworkClientUsageHistory(
            networkId=network['networkId'],
            clientId=network['clientId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=network)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=network)
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
                keys_added = add_keys(input_json=network, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=network, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkclientusagehistory(apikey, debug_dict, networks, **kwargs):
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

        network_tasks = [
            _call_getnetworkclientusagehistory(aiomeraki, network, **kwargs) for network in networks
            ]
        all_network_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(network_tasks),
                total=len(network_tasks),
                colour='green',
        ):
            network_json = await task
            if network_json:
                all_network_json.extend(iter(network_json))
        return all_network_json

async def _call_getnetworkdevices(aiomeraki, network, **kwargs):
    try:
        returned_json = await aiomeraki.networks.getNetworkDevices(
            networkId=network['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=network)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=network)
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
                keys_added = add_keys(input_json=network, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=network, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkdevices(apikey, debug_dict, networks, **kwargs):
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

        network_tasks = [
            _call_getnetworkdevices(aiomeraki, network, **kwargs) for network in networks
            ]
        all_network_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(network_tasks),
                total=len(network_tasks),
                colour='green',
        ):
            network_json = await task
            if network_json:
                all_network_json.extend(iter(network_json))
        return all_network_json

async def _call_getnetworkevents(aiomeraki, network, **kwargs):
    try:
        returned_json = await aiomeraki.networks.getNetworkEvents(
            networkId=network['networkId'],
            total_pages='all',
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=network)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=network)
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
                keys_added = add_keys(input_json=network, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=network, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkevents(apikey, debug_dict, networks, **kwargs):
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

        network_tasks = [
            _call_getnetworkevents(aiomeraki, network, **kwargs) for network in networks
            ]
        all_network_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(network_tasks),
                total=len(network_tasks),
                colour='green',
        ):
            network_json = await task
            if network_json:
                all_network_json.extend(iter(network_json))
        return all_network_json

async def _call_getnetworkeventseventtypes(aiomeraki, network, **kwargs):
    try:
        returned_json = await aiomeraki.networks.getNetworkEventsEventTypes(
            networkId=network['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=network)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=network)
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
                keys_added = add_keys(input_json=network, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=network, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkeventseventtypes(apikey, debug_dict, networks, **kwargs):
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

        network_tasks = [
            _call_getnetworkeventseventtypes(aiomeraki, network, **kwargs) for network in networks
            ]
        all_network_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(network_tasks),
                total=len(network_tasks),
                colour='green',
        ):
            network_json = await task
            if network_json:
                all_network_json.extend(iter(network_json))
        return all_network_json

async def _call_getnetworkfirmwareupgrades(aiomeraki, network, **kwargs):
    try:
        returned_json = await aiomeraki.networks.getNetworkFirmwareUpgrades(
            networkId=network['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=network)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=network)
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
                keys_added = add_keys(input_json=network, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=network, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkfirmwareupgrades(apikey, debug_dict, networks, **kwargs):
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

        network_tasks = [
            _call_getnetworkfirmwareupgrades(aiomeraki, network, **kwargs) for network in networks
            ]
        all_network_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(network_tasks),
                total=len(network_tasks),
                colour='green',
        ):
            network_json = await task
            if network_json:
                all_network_json.extend(iter(network_json))
        return all_network_json

async def _call_getnetworkfirmwareupgradesstagedevents(aiomeraki, network, **kwargs):
    try:
        returned_json = await aiomeraki.networks.getNetworkFirmwareUpgradesStagedEvents(
            networkId=network['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=network)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=network)
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
                keys_added = add_keys(input_json=network, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=network, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkfirmwareupgradesstagedevents(apikey, debug_dict, networks, **kwargs):
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

        network_tasks = [
            _call_getnetworkfirmwareupgradesstagedevents(aiomeraki, network, **kwargs) for network in networks
            ]
        all_network_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(network_tasks),
                total=len(network_tasks),
                colour='green',
        ):
            network_json = await task
            if network_json:
                all_network_json.extend(iter(network_json))
        return all_network_json

async def _call_getnetworkfirmwareupgradesstagedgroups(aiomeraki, network, **kwargs):
    try:
        returned_json = await aiomeraki.networks.getNetworkFirmwareUpgradesStagedGroups(
            networkId=network['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=network)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=network)
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
                keys_added = add_keys(input_json=network, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=network, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkfirmwareupgradesstagedgroups(apikey, debug_dict, networks, **kwargs):
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

        network_tasks = [
            _call_getnetworkfirmwareupgradesstagedgroups(aiomeraki, network, **kwargs) for network in networks
            ]
        all_network_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(network_tasks),
                total=len(network_tasks),
                colour='green',
        ):
            network_json = await task
            if network_json:
                all_network_json.extend(iter(network_json))
        return all_network_json

async def _call_getnetworkfirmwareupgradesstagedgroup(aiomeraki, network, **kwargs):
    try:
        returned_json = await aiomeraki.networks.getNetworkFirmwareUpgradesStagedGroup(
            networkId=network['networkId'],
            groupId=network['groupId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=network)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=network)
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
                keys_added = add_keys(input_json=network, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=network, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkfirmwareupgradesstagedgroup(apikey, debug_dict, networks, **kwargs):
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

        network_tasks = [
            _call_getnetworkfirmwareupgradesstagedgroup(aiomeraki, network, **kwargs) for network in networks
            ]
        all_network_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(network_tasks),
                total=len(network_tasks),
                colour='green',
        ):
            network_json = await task
            if network_json:
                all_network_json.extend(iter(network_json))
        return all_network_json

async def _call_getnetworkfirmwareupgradesstagedstages(aiomeraki, network, **kwargs):
    try:
        returned_json = await aiomeraki.networks.getNetworkFirmwareUpgradesStagedStages(
            networkId=network['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=network)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=network)
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
                keys_added = add_keys(input_json=network, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=network, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkfirmwareupgradesstagedstages(apikey, debug_dict, networks, **kwargs):
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

        network_tasks = [
            _call_getnetworkfirmwareupgradesstagedstages(aiomeraki, network, **kwargs) for network in networks
            ]
        all_network_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(network_tasks),
                total=len(network_tasks),
                colour='green',
        ):
            network_json = await task
            if network_json:
                all_network_json.extend(iter(network_json))
        return all_network_json

async def _call_getnetworkfloorplans(aiomeraki, network, **kwargs):
    try:
        returned_json = await aiomeraki.networks.getNetworkFloorPlans(
            networkId=network['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=network)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=network)
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
                keys_added = add_keys(input_json=network, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=network, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkfloorplans(apikey, debug_dict, networks, **kwargs):
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

        network_tasks = [
            _call_getnetworkfloorplans(aiomeraki, network, **kwargs) for network in networks
            ]
        all_network_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(network_tasks),
                total=len(network_tasks),
                colour='green',
        ):
            network_json = await task
            if network_json:
                all_network_json.extend(iter(network_json))
        return all_network_json

async def _call_getnetworkfloorplan(aiomeraki, network, **kwargs):
    try:
        returned_json = await aiomeraki.networks.getNetworkFloorPlan(
            networkId=network['networkId'],
            floorPlanId=network['floorPlanId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=network)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=network)
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
                keys_added = add_keys(input_json=network, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=network, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkfloorplan(apikey, debug_dict, networks, **kwargs):
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

        network_tasks = [
            _call_getnetworkfloorplan(aiomeraki, network, **kwargs) for network in networks
            ]
        all_network_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(network_tasks),
                total=len(network_tasks),
                colour='green',
        ):
            network_json = await task
            if network_json:
                all_network_json.extend(iter(network_json))
        return all_network_json

async def _call_getnetworkgrouppolicies(aiomeraki, network, **kwargs):
    try:
        returned_json = await aiomeraki.networks.getNetworkGroupPolicies(
            networkId=network['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=network)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=network)
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
                keys_added = add_keys(input_json=network, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=network, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkgrouppolicies(apikey, debug_dict, networks, **kwargs):
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

        network_tasks = [
            _call_getnetworkgrouppolicies(aiomeraki, network, **kwargs) for network in networks
            ]
        all_network_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(network_tasks),
                total=len(network_tasks),
                colour='green',
        ):
            network_json = await task
            if network_json:
                all_network_json.extend(iter(network_json))
        return all_network_json

async def _call_getnetworkgrouppolicy(aiomeraki, network, **kwargs):
    try:
        returned_json = await aiomeraki.networks.getNetworkGroupPolicy(
            networkId=network['networkId'],
            groupPolicyId=network['groupPolicyId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=network)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=network)
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
                keys_added = add_keys(input_json=network, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=network, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkgrouppolicy(apikey, debug_dict, networks, **kwargs):
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

        network_tasks = [
            _call_getnetworkgrouppolicy(aiomeraki, network, **kwargs) for network in networks
            ]
        all_network_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(network_tasks),
                total=len(network_tasks),
                colour='green',
        ):
            network_json = await task
            if network_json:
                all_network_json.extend(iter(network_json))
        return all_network_json

async def _call_getnetworkhealthalerts(aiomeraki, network, **kwargs):
    try:
        returned_json = await aiomeraki.networks.getNetworkHealthAlerts(
            networkId=network['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=network)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=network)
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
                keys_added = add_keys(input_json=network, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=network, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkhealthalerts(apikey, debug_dict, networks, **kwargs):
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

        network_tasks = [
            _call_getnetworkhealthalerts(aiomeraki, network, **kwargs) for network in networks
            ]
        all_network_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(network_tasks),
                total=len(network_tasks),
                colour='green',
        ):
            network_json = await task
            if network_json:
                all_network_json.extend(iter(network_json))
        return all_network_json

async def _call_getnetworkmerakiauthusers(aiomeraki, network, **kwargs):
    try:
        returned_json = await aiomeraki.networks.getNetworkMerakiAuthUsers(
            networkId=network['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=network)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=network)
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
                keys_added = add_keys(input_json=network, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=network, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkmerakiauthusers(apikey, debug_dict, networks, **kwargs):
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

        network_tasks = [
            _call_getnetworkmerakiauthusers(aiomeraki, network, **kwargs) for network in networks
            ]
        all_network_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(network_tasks),
                total=len(network_tasks),
                colour='green',
        ):
            network_json = await task
            if network_json:
                all_network_json.extend(iter(network_json))
        return all_network_json

async def _call_getnetworkmerakiauthuser(aiomeraki, network, **kwargs):
    try:
        returned_json = await aiomeraki.networks.getNetworkMerakiAuthUser(
            networkId=network['networkId'],
            merakiAuthUserId=network['merakiAuthUserId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=network)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=network)
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
                keys_added = add_keys(input_json=network, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=network, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkmerakiauthuser(apikey, debug_dict, networks, **kwargs):
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

        network_tasks = [
            _call_getnetworkmerakiauthuser(aiomeraki, network, **kwargs) for network in networks
            ]
        all_network_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(network_tasks),
                total=len(network_tasks),
                colour='green',
        ):
            network_json = await task
            if network_json:
                all_network_json.extend(iter(network_json))
        return all_network_json

async def _call_getnetworkmqttbrokers(aiomeraki, network, **kwargs):
    try:
        returned_json = await aiomeraki.networks.getNetworkMqttBrokers(
            networkId=network['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=network)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=network)
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
                keys_added = add_keys(input_json=network, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=network, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkmqttbrokers(apikey, debug_dict, networks, **kwargs):
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

        network_tasks = [
            _call_getnetworkmqttbrokers(aiomeraki, network, **kwargs) for network in networks
            ]
        all_network_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(network_tasks),
                total=len(network_tasks),
                colour='green',
        ):
            network_json = await task
            if network_json:
                all_network_json.extend(iter(network_json))
        return all_network_json

async def _call_getnetworkmqttbroker(aiomeraki, network, **kwargs):
    try:
        returned_json = await aiomeraki.networks.getNetworkMqttBroker(
            networkId=network['networkId'],
            mqttBrokerId=network['mqttBrokerId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=network)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=network)
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
                keys_added = add_keys(input_json=network, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=network, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkmqttbroker(apikey, debug_dict, networks, **kwargs):
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

        network_tasks = [
            _call_getnetworkmqttbroker(aiomeraki, network, **kwargs) for network in networks
            ]
        all_network_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(network_tasks),
                total=len(network_tasks),
                colour='green',
        ):
            network_json = await task
            if network_json:
                all_network_json.extend(iter(network_json))
        return all_network_json

async def _call_getnetworknetflow(aiomeraki, network, **kwargs):
    try:
        returned_json = await aiomeraki.networks.getNetworkNetflow(
            networkId=network['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=network)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=network)
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
                keys_added = add_keys(input_json=network, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=network, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworknetflow(apikey, debug_dict, networks, **kwargs):
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

        network_tasks = [
            _call_getnetworknetflow(aiomeraki, network, **kwargs) for network in networks
            ]
        all_network_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(network_tasks),
                total=len(network_tasks),
                colour='green',
        ):
            network_json = await task
            if network_json:
                all_network_json.extend(iter(network_json))
        return all_network_json

async def _call_getnetworknetworkhealthchannelutilization(aiomeraki, network, **kwargs):
    try:
        returned_json = await aiomeraki.networks.getNetworkNetworkHealthChannelUtilization(
            networkId=network['networkId'],
            total_pages='all',
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=network)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=network)
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
                keys_added = add_keys(input_json=network, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=network, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworknetworkhealthchannelutilization(apikey, debug_dict, networks, **kwargs):
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

        network_tasks = [
            _call_getnetworknetworkhealthchannelutilization(aiomeraki, network, **kwargs) for network in networks
            ]
        all_network_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(network_tasks),
                total=len(network_tasks),
                colour='green',
        ):
            network_json = await task
            if network_json:
                all_network_json.extend(iter(network_json))
        return all_network_json

async def _call_getnetworkpiipiikeys(aiomeraki, network, **kwargs):
    try:
        returned_json = await aiomeraki.networks.getNetworkPiiPiiKeys(
            networkId=network['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=network)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=network)
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
                keys_added = add_keys(input_json=network, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=network, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkpiipiikeys(apikey, debug_dict, networks, **kwargs):
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

        network_tasks = [
            _call_getnetworkpiipiikeys(aiomeraki, network, **kwargs) for network in networks
            ]
        all_network_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(network_tasks),
                total=len(network_tasks),
                colour='green',
        ):
            network_json = await task
            if network_json:
                all_network_json.extend(iter(network_json))
        return all_network_json

async def _call_getnetworkpiirequests(aiomeraki, network, **kwargs):
    try:
        returned_json = await aiomeraki.networks.getNetworkPiiRequests(
            networkId=network['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=network)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=network)
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
                keys_added = add_keys(input_json=network, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=network, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkpiirequests(apikey, debug_dict, networks, **kwargs):
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

        network_tasks = [
            _call_getnetworkpiirequests(aiomeraki, network, **kwargs) for network in networks
            ]
        all_network_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(network_tasks),
                total=len(network_tasks),
                colour='green',
        ):
            network_json = await task
            if network_json:
                all_network_json.extend(iter(network_json))
        return all_network_json

async def _call_getnetworkpiirequest(aiomeraki, network, **kwargs):
    try:
        returned_json = await aiomeraki.networks.getNetworkPiiRequest(
            networkId=network['networkId'],
            requestId=network['requestId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=network)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=network)
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
                keys_added = add_keys(input_json=network, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=network, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkpiirequest(apikey, debug_dict, networks, **kwargs):
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

        network_tasks = [
            _call_getnetworkpiirequest(aiomeraki, network, **kwargs) for network in networks
            ]
        all_network_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(network_tasks),
                total=len(network_tasks),
                colour='green',
        ):
            network_json = await task
            if network_json:
                all_network_json.extend(iter(network_json))
        return all_network_json

async def _call_getnetworkpiismdevicesforkey(aiomeraki, network, **kwargs):
    try:
        returned_json = await aiomeraki.networks.getNetworkPiiSmDevicesForKey(
            networkId=network['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=network)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=network)
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
                keys_added = add_keys(input_json=network, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=network, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkpiismdevicesforkey(apikey, debug_dict, networks, **kwargs):
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

        network_tasks = [
            _call_getnetworkpiismdevicesforkey(aiomeraki, network, **kwargs) for network in networks
            ]
        all_network_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(network_tasks),
                total=len(network_tasks),
                colour='green',
        ):
            network_json = await task
            if network_json:
                all_network_json.extend(iter(network_json))
        return all_network_json

async def _call_getnetworkpiismownersforkey(aiomeraki, network, **kwargs):
    try:
        returned_json = await aiomeraki.networks.getNetworkPiiSmOwnersForKey(
            networkId=network['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=network)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=network)
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
                keys_added = add_keys(input_json=network, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=network, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkpiismownersforkey(apikey, debug_dict, networks, **kwargs):
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

        network_tasks = [
            _call_getnetworkpiismownersforkey(aiomeraki, network, **kwargs) for network in networks
            ]
        all_network_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(network_tasks),
                total=len(network_tasks),
                colour='green',
        ):
            network_json = await task
            if network_json:
                all_network_json.extend(iter(network_json))
        return all_network_json

async def _call_getnetworkpoliciesbyclient(aiomeraki, network, **kwargs):
    try:
        returned_json = await aiomeraki.networks.getNetworkPoliciesByClient(
            networkId=network['networkId'],
            total_pages='all',
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=network)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=network)
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
                keys_added = add_keys(input_json=network, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=network, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkpoliciesbyclient(apikey, debug_dict, networks, **kwargs):
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

        network_tasks = [
            _call_getnetworkpoliciesbyclient(aiomeraki, network, **kwargs) for network in networks
            ]
        all_network_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(network_tasks),
                total=len(network_tasks),
                colour='green',
        ):
            network_json = await task
            if network_json:
                all_network_json.extend(iter(network_json))
        return all_network_json

async def _call_getnetworksettings(aiomeraki, network, **kwargs):
    try:
        returned_json = await aiomeraki.networks.getNetworkSettings(
            networkId=network['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=network)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=network)
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
                keys_added = add_keys(input_json=network, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=network, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworksettings(apikey, debug_dict, networks, **kwargs):
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

        network_tasks = [
            _call_getnetworksettings(aiomeraki, network, **kwargs) for network in networks
            ]
        all_network_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(network_tasks),
                total=len(network_tasks),
                colour='green',
        ):
            network_json = await task
            if network_json:
                all_network_json.extend(iter(network_json))
        return all_network_json

async def _call_getnetworksnmp(aiomeraki, network, **kwargs):
    try:
        returned_json = await aiomeraki.networks.getNetworkSnmp(
            networkId=network['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=network)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=network)
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
                keys_added = add_keys(input_json=network, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=network, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworksnmp(apikey, debug_dict, networks, **kwargs):
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

        network_tasks = [
            _call_getnetworksnmp(aiomeraki, network, **kwargs) for network in networks
            ]
        all_network_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(network_tasks),
                total=len(network_tasks),
                colour='green',
        ):
            network_json = await task
            if network_json:
                all_network_json.extend(iter(network_json))
        return all_network_json

async def _call_getnetworksplashloginattempts(aiomeraki, network, **kwargs):
    try:
        returned_json = await aiomeraki.networks.getNetworkSplashLoginAttempts(
            networkId=network['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=network)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=network)
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
                keys_added = add_keys(input_json=network, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=network, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworksplashloginattempts(apikey, debug_dict, networks, **kwargs):
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

        network_tasks = [
            _call_getnetworksplashloginattempts(aiomeraki, network, **kwargs) for network in networks
            ]
        all_network_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(network_tasks),
                total=len(network_tasks),
                colour='green',
        ):
            network_json = await task
            if network_json:
                all_network_json.extend(iter(network_json))
        return all_network_json

async def _call_getnetworksyslogservers(aiomeraki, network, **kwargs):
    try:
        returned_json = await aiomeraki.networks.getNetworkSyslogServers(
            networkId=network['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=network)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=network)
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
                keys_added = add_keys(input_json=network, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=network, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworksyslogservers(apikey, debug_dict, networks, **kwargs):
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

        network_tasks = [
            _call_getnetworksyslogservers(aiomeraki, network, **kwargs) for network in networks
            ]
        all_network_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(network_tasks),
                total=len(network_tasks),
                colour='green',
        ):
            network_json = await task
            if network_json:
                all_network_json.extend(iter(network_json))
        return all_network_json

async def _call_getnetworktopologylinklayer(aiomeraki, network, **kwargs):
    try:
        returned_json = await aiomeraki.networks.getNetworkTopologyLinkLayer(
            networkId=network['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=network)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=network)
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
                keys_added = add_keys(input_json=network, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=network, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworktopologylinklayer(apikey, debug_dict, networks, **kwargs):
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

        network_tasks = [
            _call_getnetworktopologylinklayer(aiomeraki, network, **kwargs) for network in networks
            ]
        all_network_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(network_tasks),
                total=len(network_tasks),
                colour='green',
        ):
            network_json = await task
            if network_json:
                all_network_json.extend(iter(network_json))
        return all_network_json

async def _call_getnetworktraffic(aiomeraki, network, **kwargs):
    try:
        returned_json = await aiomeraki.networks.getNetworkTraffic(
            networkId=network['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=network)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=network)
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
                keys_added = add_keys(input_json=network, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=network, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworktraffic(apikey, debug_dict, networks, **kwargs):
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

        network_tasks = [
            _call_getnetworktraffic(aiomeraki, network, **kwargs) for network in networks
            ]
        all_network_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(network_tasks),
                total=len(network_tasks),
                colour='green',
        ):
            network_json = await task
            if network_json:
                all_network_json.extend(iter(network_json))
        return all_network_json

async def _call_getnetworktrafficanalysis(aiomeraki, network, **kwargs):
    try:
        returned_json = await aiomeraki.networks.getNetworkTrafficAnalysis(
            networkId=network['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=network)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=network)
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
                keys_added = add_keys(input_json=network, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=network, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworktrafficanalysis(apikey, debug_dict, networks, **kwargs):
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

        network_tasks = [
            _call_getnetworktrafficanalysis(aiomeraki, network, **kwargs) for network in networks
            ]
        all_network_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(network_tasks),
                total=len(network_tasks),
                colour='green',
        ):
            network_json = await task
            if network_json:
                all_network_json.extend(iter(network_json))
        return all_network_json

async def _call_getnetworktrafficshapingapplicationcategories(aiomeraki, network, **kwargs):
    try:
        returned_json = await aiomeraki.networks.getNetworkTrafficShapingApplicationCategories(
            networkId=network['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=network)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=network)
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
                keys_added = add_keys(input_json=network, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=network, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworktrafficshapingapplicationcategories(apikey, debug_dict, networks, **kwargs):
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

        network_tasks = [
            _call_getnetworktrafficshapingapplicationcategories(aiomeraki, network, **kwargs) for network in networks
            ]
        all_network_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(network_tasks),
                total=len(network_tasks),
                colour='green',
        ):
            network_json = await task
            if network_json:
                all_network_json.extend(iter(network_json))
        return all_network_json

async def _call_getnetworktrafficshapingdscptaggingoptions(aiomeraki, network, **kwargs):
    try:
        returned_json = await aiomeraki.networks.getNetworkTrafficShapingDscpTaggingOptions(
            networkId=network['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=network)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=network)
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
                keys_added = add_keys(input_json=network, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=network, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworktrafficshapingdscptaggingoptions(apikey, debug_dict, networks, **kwargs):
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

        network_tasks = [
            _call_getnetworktrafficshapingdscptaggingoptions(aiomeraki, network, **kwargs) for network in networks
            ]
        all_network_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(network_tasks),
                total=len(network_tasks),
                colour='green',
        ):
            network_json = await task
            if network_json:
                all_network_json.extend(iter(network_json))
        return all_network_json

async def _call_getnetworkvlanprofiles(aiomeraki, network, **kwargs):
    try:
        returned_json = await aiomeraki.networks.getNetworkVlanProfiles(
            networkId=network['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=network)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=network)
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
                keys_added = add_keys(input_json=network, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=network, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkvlanprofiles(apikey, debug_dict, networks, **kwargs):
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

        network_tasks = [
            _call_getnetworkvlanprofiles(aiomeraki, network, **kwargs) for network in networks
            ]
        all_network_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(network_tasks),
                total=len(network_tasks),
                colour='green',
        ):
            network_json = await task
            if network_json:
                all_network_json.extend(iter(network_json))
        return all_network_json

async def _call_getnetworkvlanprofilesassignmentsbydevice(aiomeraki, network, **kwargs):
    try:
        returned_json = await aiomeraki.networks.getNetworkVlanProfilesAssignmentsByDevice(
            networkId=network['networkId'],
            total_pages='all',
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=network)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=network)
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
                keys_added = add_keys(input_json=network, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=network, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkvlanprofilesassignmentsbydevice(apikey, debug_dict, networks, **kwargs):
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

        network_tasks = [
            _call_getnetworkvlanprofilesassignmentsbydevice(aiomeraki, network, **kwargs) for network in networks
            ]
        all_network_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(network_tasks),
                total=len(network_tasks),
                colour='green',
        ):
            network_json = await task
            if network_json:
                all_network_json.extend(iter(network_json))
        return all_network_json

async def _call_getnetworkvlanprofile(aiomeraki, network, **kwargs):
    try:
        returned_json = await aiomeraki.networks.getNetworkVlanProfile(
            networkId=network['networkId'],
            iname=network['iname'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=network)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=network)
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
                keys_added = add_keys(input_json=network, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=network, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkvlanprofile(apikey, debug_dict, networks, **kwargs):
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

        network_tasks = [
            _call_getnetworkvlanprofile(aiomeraki, network, **kwargs) for network in networks
            ]
        all_network_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(network_tasks),
                total=len(network_tasks),
                colour='green',
        ):
            network_json = await task
            if network_json:
                all_network_json.extend(iter(network_json))
        return all_network_json

async def _call_getnetworkwebhookshttpservers(aiomeraki, network, **kwargs):
    try:
        returned_json = await aiomeraki.networks.getNetworkWebhooksHttpServers(
            networkId=network['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=network)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=network)
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
                keys_added = add_keys(input_json=network, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=network, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkwebhookshttpservers(apikey, debug_dict, networks, **kwargs):
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

        network_tasks = [
            _call_getnetworkwebhookshttpservers(aiomeraki, network, **kwargs) for network in networks
            ]
        all_network_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(network_tasks),
                total=len(network_tasks),
                colour='green',
        ):
            network_json = await task
            if network_json:
                all_network_json.extend(iter(network_json))
        return all_network_json

async def _call_getnetworkwebhookshttpserver(aiomeraki, network, **kwargs):
    try:
        returned_json = await aiomeraki.networks.getNetworkWebhooksHttpServer(
            networkId=network['networkId'],
            httpServerId=network['httpServerId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=network)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=network)
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
                keys_added = add_keys(input_json=network, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=network, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkwebhookshttpserver(apikey, debug_dict, networks, **kwargs):
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

        network_tasks = [
            _call_getnetworkwebhookshttpserver(aiomeraki, network, **kwargs) for network in networks
            ]
        all_network_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(network_tasks),
                total=len(network_tasks),
                colour='green',
        ):
            network_json = await task
            if network_json:
                all_network_json.extend(iter(network_json))
        return all_network_json

async def _call_getnetworkwebhookspayloadtemplates(aiomeraki, network, **kwargs):
    try:
        returned_json = await aiomeraki.networks.getNetworkWebhooksPayloadTemplates(
            networkId=network['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=network)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=network)
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
                keys_added = add_keys(input_json=network, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=network, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkwebhookspayloadtemplates(apikey, debug_dict, networks, **kwargs):
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

        network_tasks = [
            _call_getnetworkwebhookspayloadtemplates(aiomeraki, network, **kwargs) for network in networks
            ]
        all_network_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(network_tasks),
                total=len(network_tasks),
                colour='green',
        ):
            network_json = await task
            if network_json:
                all_network_json.extend(iter(network_json))
        return all_network_json

async def _call_getnetworkwebhookspayloadtemplate(aiomeraki, network, **kwargs):
    try:
        returned_json = await aiomeraki.networks.getNetworkWebhooksPayloadTemplate(
            networkId=network['networkId'],
            payloadTemplateId=network['payloadTemplateId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=network)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=network)
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
                keys_added = add_keys(input_json=network, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=network, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkwebhookspayloadtemplate(apikey, debug_dict, networks, **kwargs):
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

        network_tasks = [
            _call_getnetworkwebhookspayloadtemplate(aiomeraki, network, **kwargs) for network in networks
            ]
        all_network_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(network_tasks),
                total=len(network_tasks),
                colour='green',
        ):
            network_json = await task
            if network_json:
                all_network_json.extend(iter(network_json))
        return all_network_json

async def _call_getnetworkwebhookswebhooktest(aiomeraki, network, **kwargs):
    try:
        returned_json = await aiomeraki.networks.getNetworkWebhooksWebhookTest(
            networkId=network['networkId'],
            webhookTestId=network['webhookTestId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=network)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=network)
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
                keys_added = add_keys(input_json=network, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=network, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkwebhookswebhooktest(apikey, debug_dict, networks, **kwargs):
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

        network_tasks = [
            _call_getnetworkwebhookswebhooktest(aiomeraki, network, **kwargs) for network in networks
            ]
        all_network_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(network_tasks),
                total=len(network_tasks),
                colour='green',
        ):
            network_json = await task
            if network_json:
                all_network_json.extend(iter(network_json))
        return all_network_json
