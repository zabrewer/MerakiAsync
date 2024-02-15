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

async def _call_getdeviceswitchports(aiomeraki, switch, **kwargs):
    try:
        returned_json = await aiomeraki.switch.getDeviceSwitchPorts(
            serial=switch['serial'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=switch)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=switch)
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
                keys_added = add_keys(input_json=switch, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=switch, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getdeviceswitchports(apikey, debug_dict, switches, **kwargs):
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

        switch_tasks = [
            _call_getdeviceswitchports(aiomeraki, switch, **kwargs) for switch in switches
            ]
        all_switch_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(switch_tasks),
                total=len(switch_tasks),
                colour='green',
        ):
            switch_json = await task
            if switch_json:
                all_switch_json.extend(iter(switch_json))
        return all_switch_json

async def _call_getdeviceswitchportsstatuses(aiomeraki, switch, **kwargs):
    try:
        returned_json = await aiomeraki.switch.getDeviceSwitchPortsStatuses(
            serial=switch['serial'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=switch)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=switch)
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
                keys_added = add_keys(input_json=switch, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=switch, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getdeviceswitchportsstatuses(apikey, debug_dict, switches, **kwargs):
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

        switch_tasks = [
            _call_getdeviceswitchportsstatuses(aiomeraki, switch, **kwargs) for switch in switches
            ]
        all_switch_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(switch_tasks),
                total=len(switch_tasks),
                colour='green',
        ):
            switch_json = await task
            if switch_json:
                all_switch_json.extend(iter(switch_json))
        return all_switch_json

async def _call_getdeviceswitchportsstatusespackets(aiomeraki, switch, **kwargs):
    try:
        returned_json = await aiomeraki.switch.getDeviceSwitchPortsStatusesPackets(
            serial=switch['serial'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=switch)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=switch)
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
                keys_added = add_keys(input_json=switch, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=switch, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getdeviceswitchportsstatusespackets(apikey, debug_dict, switches, **kwargs):
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

        switch_tasks = [
            _call_getdeviceswitchportsstatusespackets(aiomeraki, switch, **kwargs) for switch in switches
            ]
        all_switch_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(switch_tasks),
                total=len(switch_tasks),
                colour='green',
        ):
            switch_json = await task
            if switch_json:
                all_switch_json.extend(iter(switch_json))
        return all_switch_json

async def _call_getdeviceswitchport(aiomeraki, switch, **kwargs):
    try:
        returned_json = await aiomeraki.switch.getDeviceSwitchPort(
            serial=switch['serial'],
            portId=switch['portId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=switch)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=switch)
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
                keys_added = add_keys(input_json=switch, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=switch, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getdeviceswitchport(apikey, debug_dict, switches, **kwargs):
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

        switch_tasks = [
            _call_getdeviceswitchport(aiomeraki, switch, **kwargs) for switch in switches
            ]
        all_switch_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(switch_tasks),
                total=len(switch_tasks),
                colour='green',
        ):
            switch_json = await task
            if switch_json:
                all_switch_json.extend(iter(switch_json))
        return all_switch_json

async def _call_getdeviceswitchroutinginterfaces(aiomeraki, switch, **kwargs):
    try:
        returned_json = await aiomeraki.switch.getDeviceSwitchRoutingInterfaces(
            serial=switch['serial'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=switch)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=switch)
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
                keys_added = add_keys(input_json=switch, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=switch, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getdeviceswitchroutinginterfaces(apikey, debug_dict, switches, **kwargs):
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

        switch_tasks = [
            _call_getdeviceswitchroutinginterfaces(aiomeraki, switch, **kwargs) for switch in switches
            ]
        all_switch_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(switch_tasks),
                total=len(switch_tasks),
                colour='green',
        ):
            switch_json = await task
            if switch_json:
                all_switch_json.extend(iter(switch_json))
        return all_switch_json

async def _call_getdeviceswitchroutinginterface(aiomeraki, switch, **kwargs):
    try:
        returned_json = await aiomeraki.switch.getDeviceSwitchRoutingInterface(
            serial=switch['serial'],
            interfaceId=switch['interfaceId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=switch)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=switch)
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
                keys_added = add_keys(input_json=switch, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=switch, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getdeviceswitchroutinginterface(apikey, debug_dict, switches, **kwargs):
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

        switch_tasks = [
            _call_getdeviceswitchroutinginterface(aiomeraki, switch, **kwargs) for switch in switches
            ]
        all_switch_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(switch_tasks),
                total=len(switch_tasks),
                colour='green',
        ):
            switch_json = await task
            if switch_json:
                all_switch_json.extend(iter(switch_json))
        return all_switch_json

async def _call_getdeviceswitchroutinginterfacedhcp(aiomeraki, switch, **kwargs):
    try:
        returned_json = await aiomeraki.switch.getDeviceSwitchRoutingInterfaceDhcp(
            serial=switch['serial'],
            interfaceId=switch['interfaceId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=switch)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=switch)
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
                keys_added = add_keys(input_json=switch, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=switch, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getdeviceswitchroutinginterfacedhcp(apikey, debug_dict, switches, **kwargs):
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

        switch_tasks = [
            _call_getdeviceswitchroutinginterfacedhcp(aiomeraki, switch, **kwargs) for switch in switches
            ]
        all_switch_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(switch_tasks),
                total=len(switch_tasks),
                colour='green',
        ):
            switch_json = await task
            if switch_json:
                all_switch_json.extend(iter(switch_json))
        return all_switch_json

async def _call_getdeviceswitchroutingstaticroutes(aiomeraki, switch, **kwargs):
    try:
        returned_json = await aiomeraki.switch.getDeviceSwitchRoutingStaticRoutes(
            serial=switch['serial'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=switch)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=switch)
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
                keys_added = add_keys(input_json=switch, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=switch, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getdeviceswitchroutingstaticroutes(apikey, debug_dict, switches, **kwargs):
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

        switch_tasks = [
            _call_getdeviceswitchroutingstaticroutes(aiomeraki, switch, **kwargs) for switch in switches
            ]
        all_switch_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(switch_tasks),
                total=len(switch_tasks),
                colour='green',
        ):
            switch_json = await task
            if switch_json:
                all_switch_json.extend(iter(switch_json))
        return all_switch_json

async def _call_getdeviceswitchroutingstaticroute(aiomeraki, switch, **kwargs):
    try:
        returned_json = await aiomeraki.switch.getDeviceSwitchRoutingStaticRoute(
            serial=switch['serial'],
            staticRouteId=switch['staticRouteId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=switch)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=switch)
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
                keys_added = add_keys(input_json=switch, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=switch, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getdeviceswitchroutingstaticroute(apikey, debug_dict, switches, **kwargs):
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

        switch_tasks = [
            _call_getdeviceswitchroutingstaticroute(aiomeraki, switch, **kwargs) for switch in switches
            ]
        all_switch_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(switch_tasks),
                total=len(switch_tasks),
                colour='green',
        ):
            switch_json = await task
            if switch_json:
                all_switch_json.extend(iter(switch_json))
        return all_switch_json

async def _call_getdeviceswitchwarmspare(aiomeraki, switch, **kwargs):
    try:
        returned_json = await aiomeraki.switch.getDeviceSwitchWarmSpare(
            serial=switch['serial'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=switch)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=switch)
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
                keys_added = add_keys(input_json=switch, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=switch, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getdeviceswitchwarmspare(apikey, debug_dict, switches, **kwargs):
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

        switch_tasks = [
            _call_getdeviceswitchwarmspare(aiomeraki, switch, **kwargs) for switch in switches
            ]
        all_switch_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(switch_tasks),
                total=len(switch_tasks),
                colour='green',
        ):
            switch_json = await task
            if switch_json:
                all_switch_json.extend(iter(switch_json))
        return all_switch_json

async def _call_getnetworkswitchaccesscontrollists(aiomeraki, switch, **kwargs):
    try:
        returned_json = await aiomeraki.switch.getNetworkSwitchAccessControlLists(
            networkId=switch['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=switch)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=switch)
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
                keys_added = add_keys(input_json=switch, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=switch, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkswitchaccesscontrollists(apikey, debug_dict, switches, **kwargs):
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

        switch_tasks = [
            _call_getnetworkswitchaccesscontrollists(aiomeraki, switch, **kwargs) for switch in switches
            ]
        all_switch_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(switch_tasks),
                total=len(switch_tasks),
                colour='green',
        ):
            switch_json = await task
            if switch_json:
                all_switch_json.extend(iter(switch_json))
        return all_switch_json

async def _call_getnetworkswitchaccesspolicies(aiomeraki, switch, **kwargs):
    try:
        returned_json = await aiomeraki.switch.getNetworkSwitchAccessPolicies(
            networkId=switch['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=switch)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=switch)
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
                keys_added = add_keys(input_json=switch, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=switch, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkswitchaccesspolicies(apikey, debug_dict, switches, **kwargs):
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

        switch_tasks = [
            _call_getnetworkswitchaccesspolicies(aiomeraki, switch, **kwargs) for switch in switches
            ]
        all_switch_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(switch_tasks),
                total=len(switch_tasks),
                colour='green',
        ):
            switch_json = await task
            if switch_json:
                all_switch_json.extend(iter(switch_json))
        return all_switch_json

async def _call_getnetworkswitchaccesspolicy(aiomeraki, switch, **kwargs):
    try:
        returned_json = await aiomeraki.switch.getNetworkSwitchAccessPolicy(
            networkId=switch['networkId'],
            accessPolicyNumber=switch['accessPolicyNumber'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=switch)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=switch)
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
                keys_added = add_keys(input_json=switch, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=switch, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkswitchaccesspolicy(apikey, debug_dict, switches, **kwargs):
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

        switch_tasks = [
            _call_getnetworkswitchaccesspolicy(aiomeraki, switch, **kwargs) for switch in switches
            ]
        all_switch_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(switch_tasks),
                total=len(switch_tasks),
                colour='green',
        ):
            switch_json = await task
            if switch_json:
                all_switch_json.extend(iter(switch_json))
        return all_switch_json

async def _call_getnetworkswitchalternatemanagementinterface(aiomeraki, switch, **kwargs):
    try:
        returned_json = await aiomeraki.switch.getNetworkSwitchAlternateManagementInterface(
            networkId=switch['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=switch)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=switch)
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
                keys_added = add_keys(input_json=switch, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=switch, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkswitchalternatemanagementinterface(apikey, debug_dict, switches, **kwargs):
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

        switch_tasks = [
            _call_getnetworkswitchalternatemanagementinterface(aiomeraki, switch, **kwargs) for switch in switches
            ]
        all_switch_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(switch_tasks),
                total=len(switch_tasks),
                colour='green',
        ):
            switch_json = await task
            if switch_json:
                all_switch_json.extend(iter(switch_json))
        return all_switch_json

async def _call_getnetworkswitchdhcpv4serversseen(aiomeraki, switch, **kwargs):
    try:
        returned_json = await aiomeraki.switch.getNetworkSwitchDhcpV4ServersSeen(
            networkId=switch['networkId'],
            total_pages='all',
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=switch)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=switch)
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
                keys_added = add_keys(input_json=switch, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=switch, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkswitchdhcpv4serversseen(apikey, debug_dict, switches, **kwargs):
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

        switch_tasks = [
            _call_getnetworkswitchdhcpv4serversseen(aiomeraki, switch, **kwargs) for switch in switches
            ]
        all_switch_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(switch_tasks),
                total=len(switch_tasks),
                colour='green',
        ):
            switch_json = await task
            if switch_json:
                all_switch_json.extend(iter(switch_json))
        return all_switch_json

async def _call_getnetworkswitchdhcpserverpolicy(aiomeraki, switch, **kwargs):
    try:
        returned_json = await aiomeraki.switch.getNetworkSwitchDhcpServerPolicy(
            networkId=switch['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=switch)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=switch)
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
                keys_added = add_keys(input_json=switch, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=switch, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkswitchdhcpserverpolicy(apikey, debug_dict, switches, **kwargs):
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

        switch_tasks = [
            _call_getnetworkswitchdhcpserverpolicy(aiomeraki, switch, **kwargs) for switch in switches
            ]
        all_switch_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(switch_tasks),
                total=len(switch_tasks),
                colour='green',
        ):
            switch_json = await task
            if switch_json:
                all_switch_json.extend(iter(switch_json))
        return all_switch_json

async def _call_getnetworkswitchdhcpserverpolicyarpinspectiontrustedservers(aiomeraki, switch, **kwargs):
    try:
        returned_json = await aiomeraki.switch.getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers(
            networkId=switch['networkId'],
            total_pages='all',
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=switch)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=switch)
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
                keys_added = add_keys(input_json=switch, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=switch, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkswitchdhcpserverpolicyarpinspectiontrustedservers(apikey, debug_dict, switches, **kwargs):
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

        switch_tasks = [
            _call_getnetworkswitchdhcpserverpolicyarpinspectiontrustedservers(aiomeraki, switch, **kwargs) for switch in switches
            ]
        all_switch_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(switch_tasks),
                total=len(switch_tasks),
                colour='green',
        ):
            switch_json = await task
            if switch_json:
                all_switch_json.extend(iter(switch_json))
        return all_switch_json

async def _call_getnetworkswitchdhcpserverpolicyarpinspectionwarningsbydevice(aiomeraki, switch, **kwargs):
    try:
        returned_json = await aiomeraki.switch.getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice(
            networkId=switch['networkId'],
            total_pages='all',
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=switch)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=switch)
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
                keys_added = add_keys(input_json=switch, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=switch, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkswitchdhcpserverpolicyarpinspectionwarningsbydevice(apikey, debug_dict, switches, **kwargs):
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

        switch_tasks = [
            _call_getnetworkswitchdhcpserverpolicyarpinspectionwarningsbydevice(aiomeraki, switch, **kwargs) for switch in switches
            ]
        all_switch_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(switch_tasks),
                total=len(switch_tasks),
                colour='green',
        ):
            switch_json = await task
            if switch_json:
                all_switch_json.extend(iter(switch_json))
        return all_switch_json

async def _call_getnetworkswitchdscptocosmappings(aiomeraki, switch, **kwargs):
    try:
        returned_json = await aiomeraki.switch.getNetworkSwitchDscpToCosMappings(
            networkId=switch['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=switch)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=switch)
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
                keys_added = add_keys(input_json=switch, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=switch, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkswitchdscptocosmappings(apikey, debug_dict, switches, **kwargs):
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

        switch_tasks = [
            _call_getnetworkswitchdscptocosmappings(aiomeraki, switch, **kwargs) for switch in switches
            ]
        all_switch_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(switch_tasks),
                total=len(switch_tasks),
                colour='green',
        ):
            switch_json = await task
            if switch_json:
                all_switch_json.extend(iter(switch_json))
        return all_switch_json

async def _call_getnetworkswitchlinkaggregations(aiomeraki, switch, **kwargs):
    try:
        returned_json = await aiomeraki.switch.getNetworkSwitchLinkAggregations(
            networkId=switch['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=switch)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=switch)
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
                keys_added = add_keys(input_json=switch, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=switch, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkswitchlinkaggregations(apikey, debug_dict, switches, **kwargs):
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

        switch_tasks = [
            _call_getnetworkswitchlinkaggregations(aiomeraki, switch, **kwargs) for switch in switches
            ]
        all_switch_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(switch_tasks),
                total=len(switch_tasks),
                colour='green',
        ):
            switch_json = await task
            if switch_json:
                all_switch_json.extend(iter(switch_json))
        return all_switch_json

async def _call_getnetworkswitchmtu(aiomeraki, switch, **kwargs):
    try:
        returned_json = await aiomeraki.switch.getNetworkSwitchMtu(
            networkId=switch['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=switch)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=switch)
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
                keys_added = add_keys(input_json=switch, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=switch, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkswitchmtu(apikey, debug_dict, switches, **kwargs):
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

        switch_tasks = [
            _call_getnetworkswitchmtu(aiomeraki, switch, **kwargs) for switch in switches
            ]
        all_switch_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(switch_tasks),
                total=len(switch_tasks),
                colour='green',
        ):
            switch_json = await task
            if switch_json:
                all_switch_json.extend(iter(switch_json))
        return all_switch_json

async def _call_getnetworkswitchportschedules(aiomeraki, switch, **kwargs):
    try:
        returned_json = await aiomeraki.switch.getNetworkSwitchPortSchedules(
            networkId=switch['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=switch)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=switch)
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
                keys_added = add_keys(input_json=switch, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=switch, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkswitchportschedules(apikey, debug_dict, switches, **kwargs):
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

        switch_tasks = [
            _call_getnetworkswitchportschedules(aiomeraki, switch, **kwargs) for switch in switches
            ]
        all_switch_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(switch_tasks),
                total=len(switch_tasks),
                colour='green',
        ):
            switch_json = await task
            if switch_json:
                all_switch_json.extend(iter(switch_json))
        return all_switch_json

async def _call_getnetworkswitchqosrules(aiomeraki, switch, **kwargs):
    try:
        returned_json = await aiomeraki.switch.getNetworkSwitchQosRules(
            networkId=switch['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=switch)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=switch)
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
                keys_added = add_keys(input_json=switch, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=switch, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkswitchqosrules(apikey, debug_dict, switches, **kwargs):
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

        switch_tasks = [
            _call_getnetworkswitchqosrules(aiomeraki, switch, **kwargs) for switch in switches
            ]
        all_switch_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(switch_tasks),
                total=len(switch_tasks),
                colour='green',
        ):
            switch_json = await task
            if switch_json:
                all_switch_json.extend(iter(switch_json))
        return all_switch_json

async def _call_getnetworkswitchqosrulesorder(aiomeraki, switch, **kwargs):
    try:
        returned_json = await aiomeraki.switch.getNetworkSwitchQosRulesOrder(
            networkId=switch['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=switch)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=switch)
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
                keys_added = add_keys(input_json=switch, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=switch, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkswitchqosrulesorder(apikey, debug_dict, switches, **kwargs):
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

        switch_tasks = [
            _call_getnetworkswitchqosrulesorder(aiomeraki, switch, **kwargs) for switch in switches
            ]
        all_switch_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(switch_tasks),
                total=len(switch_tasks),
                colour='green',
        ):
            switch_json = await task
            if switch_json:
                all_switch_json.extend(iter(switch_json))
        return all_switch_json

async def _call_getnetworkswitchqosrule(aiomeraki, switch, **kwargs):
    try:
        returned_json = await aiomeraki.switch.getNetworkSwitchQosRule(
            networkId=switch['networkId'],
            qosRuleId=switch['qosRuleId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=switch)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=switch)
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
                keys_added = add_keys(input_json=switch, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=switch, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkswitchqosrule(apikey, debug_dict, switches, **kwargs):
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

        switch_tasks = [
            _call_getnetworkswitchqosrule(aiomeraki, switch, **kwargs) for switch in switches
            ]
        all_switch_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(switch_tasks),
                total=len(switch_tasks),
                colour='green',
        ):
            switch_json = await task
            if switch_json:
                all_switch_json.extend(iter(switch_json))
        return all_switch_json

async def _call_getnetworkswitchroutingmulticast(aiomeraki, switch, **kwargs):
    try:
        returned_json = await aiomeraki.switch.getNetworkSwitchRoutingMulticast(
            networkId=switch['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=switch)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=switch)
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
                keys_added = add_keys(input_json=switch, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=switch, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkswitchroutingmulticast(apikey, debug_dict, switches, **kwargs):
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

        switch_tasks = [
            _call_getnetworkswitchroutingmulticast(aiomeraki, switch, **kwargs) for switch in switches
            ]
        all_switch_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(switch_tasks),
                total=len(switch_tasks),
                colour='green',
        ):
            switch_json = await task
            if switch_json:
                all_switch_json.extend(iter(switch_json))
        return all_switch_json

async def _call_getnetworkswitchroutingmulticastrendezvouspoints(aiomeraki, switch, **kwargs):
    try:
        returned_json = await aiomeraki.switch.getNetworkSwitchRoutingMulticastRendezvousPoints(
            networkId=switch['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=switch)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=switch)
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
                keys_added = add_keys(input_json=switch, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=switch, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkswitchroutingmulticastrendezvouspoints(apikey, debug_dict, switches, **kwargs):
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

        switch_tasks = [
            _call_getnetworkswitchroutingmulticastrendezvouspoints(aiomeraki, switch, **kwargs) for switch in switches
            ]
        all_switch_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(switch_tasks),
                total=len(switch_tasks),
                colour='green',
        ):
            switch_json = await task
            if switch_json:
                all_switch_json.extend(iter(switch_json))
        return all_switch_json

async def _call_getnetworkswitchroutingmulticastrendezvouspoint(aiomeraki, switch, **kwargs):
    try:
        returned_json = await aiomeraki.switch.getNetworkSwitchRoutingMulticastRendezvousPoint(
            networkId=switch['networkId'],
            rendezvousPointId=switch['rendezvousPointId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=switch)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=switch)
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
                keys_added = add_keys(input_json=switch, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=switch, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkswitchroutingmulticastrendezvouspoint(apikey, debug_dict, switches, **kwargs):
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

        switch_tasks = [
            _call_getnetworkswitchroutingmulticastrendezvouspoint(aiomeraki, switch, **kwargs) for switch in switches
            ]
        all_switch_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(switch_tasks),
                total=len(switch_tasks),
                colour='green',
        ):
            switch_json = await task
            if switch_json:
                all_switch_json.extend(iter(switch_json))
        return all_switch_json

async def _call_getnetworkswitchroutingospf(aiomeraki, switch, **kwargs):
    try:
        returned_json = await aiomeraki.switch.getNetworkSwitchRoutingOspf(
            networkId=switch['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=switch)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=switch)
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
                keys_added = add_keys(input_json=switch, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=switch, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkswitchroutingospf(apikey, debug_dict, switches, **kwargs):
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

        switch_tasks = [
            _call_getnetworkswitchroutingospf(aiomeraki, switch, **kwargs) for switch in switches
            ]
        all_switch_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(switch_tasks),
                total=len(switch_tasks),
                colour='green',
        ):
            switch_json = await task
            if switch_json:
                all_switch_json.extend(iter(switch_json))
        return all_switch_json

async def _call_getnetworkswitchsettings(aiomeraki, switch, **kwargs):
    try:
        returned_json = await aiomeraki.switch.getNetworkSwitchSettings(
            networkId=switch['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=switch)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=switch)
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
                keys_added = add_keys(input_json=switch, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=switch, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkswitchsettings(apikey, debug_dict, switches, **kwargs):
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

        switch_tasks = [
            _call_getnetworkswitchsettings(aiomeraki, switch, **kwargs) for switch in switches
            ]
        all_switch_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(switch_tasks),
                total=len(switch_tasks),
                colour='green',
        ):
            switch_json = await task
            if switch_json:
                all_switch_json.extend(iter(switch_json))
        return all_switch_json

async def _call_getnetworkswitchstacks(aiomeraki, switch, **kwargs):
    try:
        returned_json = await aiomeraki.switch.getNetworkSwitchStacks(
            networkId=switch['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=switch)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=switch)
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
                keys_added = add_keys(input_json=switch, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=switch, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkswitchstacks(apikey, debug_dict, switches, **kwargs):
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

        switch_tasks = [
            _call_getnetworkswitchstacks(aiomeraki, switch, **kwargs) for switch in switches
            ]
        all_switch_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(switch_tasks),
                total=len(switch_tasks),
                colour='green',
        ):
            switch_json = await task
            if switch_json:
                all_switch_json.extend(iter(switch_json))
        return all_switch_json

async def _call_getnetworkswitchstack(aiomeraki, switch, **kwargs):
    try:
        returned_json = await aiomeraki.switch.getNetworkSwitchStack(
            networkId=switch['networkId'],
            switchStackId=switch['switchStackId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=switch)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=switch)
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
                keys_added = add_keys(input_json=switch, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=switch, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkswitchstack(apikey, debug_dict, switches, **kwargs):
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

        switch_tasks = [
            _call_getnetworkswitchstack(aiomeraki, switch, **kwargs) for switch in switches
            ]
        all_switch_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(switch_tasks),
                total=len(switch_tasks),
                colour='green',
        ):
            switch_json = await task
            if switch_json:
                all_switch_json.extend(iter(switch_json))
        return all_switch_json

async def _call_getnetworkswitchstackroutinginterfaces(aiomeraki, switch, **kwargs):
    try:
        returned_json = await aiomeraki.switch.getNetworkSwitchStackRoutingInterfaces(
            networkId=switch['networkId'],
            switchStackId=switch['switchStackId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=switch)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=switch)
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
                keys_added = add_keys(input_json=switch, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=switch, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkswitchstackroutinginterfaces(apikey, debug_dict, switches, **kwargs):
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

        switch_tasks = [
            _call_getnetworkswitchstackroutinginterfaces(aiomeraki, switch, **kwargs) for switch in switches
            ]
        all_switch_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(switch_tasks),
                total=len(switch_tasks),
                colour='green',
        ):
            switch_json = await task
            if switch_json:
                all_switch_json.extend(iter(switch_json))
        return all_switch_json

async def _call_getnetworkswitchstackroutinginterface(aiomeraki, switch, **kwargs):
    try:
        returned_json = await aiomeraki.switch.getNetworkSwitchStackRoutingInterface(
            networkId=switch['networkId'],
            switchStackId=switch['switchStackId'],
            interfaceId=switch['interfaceId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=switch)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=switch)
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
                keys_added = add_keys(input_json=switch, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=switch, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkswitchstackroutinginterface(apikey, debug_dict, switches, **kwargs):
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

        switch_tasks = [
            _call_getnetworkswitchstackroutinginterface(aiomeraki, switch, **kwargs) for switch in switches
            ]
        all_switch_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(switch_tasks),
                total=len(switch_tasks),
                colour='green',
        ):
            switch_json = await task
            if switch_json:
                all_switch_json.extend(iter(switch_json))
        return all_switch_json

async def _call_getnetworkswitchstackroutinginterfacedhcp(aiomeraki, switch, **kwargs):
    try:
        returned_json = await aiomeraki.switch.getNetworkSwitchStackRoutingInterfaceDhcp(
            networkId=switch['networkId'],
            switchStackId=switch['switchStackId'],
            interfaceId=switch['interfaceId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=switch)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=switch)
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
                keys_added = add_keys(input_json=switch, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=switch, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkswitchstackroutinginterfacedhcp(apikey, debug_dict, switches, **kwargs):
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

        switch_tasks = [
            _call_getnetworkswitchstackroutinginterfacedhcp(aiomeraki, switch, **kwargs) for switch in switches
            ]
        all_switch_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(switch_tasks),
                total=len(switch_tasks),
                colour='green',
        ):
            switch_json = await task
            if switch_json:
                all_switch_json.extend(iter(switch_json))
        return all_switch_json

async def _call_getnetworkswitchstackroutingstaticroutes(aiomeraki, switch, **kwargs):
    try:
        returned_json = await aiomeraki.switch.getNetworkSwitchStackRoutingStaticRoutes(
            networkId=switch['networkId'],
            switchStackId=switch['switchStackId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=switch)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=switch)
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
                keys_added = add_keys(input_json=switch, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=switch, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkswitchstackroutingstaticroutes(apikey, debug_dict, switches, **kwargs):
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

        switch_tasks = [
            _call_getnetworkswitchstackroutingstaticroutes(aiomeraki, switch, **kwargs) for switch in switches
            ]
        all_switch_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(switch_tasks),
                total=len(switch_tasks),
                colour='green',
        ):
            switch_json = await task
            if switch_json:
                all_switch_json.extend(iter(switch_json))
        return all_switch_json

async def _call_getnetworkswitchstackroutingstaticroute(aiomeraki, switch, **kwargs):
    try:
        returned_json = await aiomeraki.switch.getNetworkSwitchStackRoutingStaticRoute(
            networkId=switch['networkId'],
            switchStackId=switch['switchStackId'],
            staticRouteId=switch['staticRouteId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=switch)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=switch)
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
                keys_added = add_keys(input_json=switch, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=switch, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkswitchstackroutingstaticroute(apikey, debug_dict, switches, **kwargs):
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

        switch_tasks = [
            _call_getnetworkswitchstackroutingstaticroute(aiomeraki, switch, **kwargs) for switch in switches
            ]
        all_switch_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(switch_tasks),
                total=len(switch_tasks),
                colour='green',
        ):
            switch_json = await task
            if switch_json:
                all_switch_json.extend(iter(switch_json))
        return all_switch_json

async def _call_getnetworkswitchstormcontrol(aiomeraki, switch, **kwargs):
    try:
        returned_json = await aiomeraki.switch.getNetworkSwitchStormControl(
            networkId=switch['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=switch)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=switch)
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
                keys_added = add_keys(input_json=switch, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=switch, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkswitchstormcontrol(apikey, debug_dict, switches, **kwargs):
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

        switch_tasks = [
            _call_getnetworkswitchstormcontrol(aiomeraki, switch, **kwargs) for switch in switches
            ]
        all_switch_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(switch_tasks),
                total=len(switch_tasks),
                colour='green',
        ):
            switch_json = await task
            if switch_json:
                all_switch_json.extend(iter(switch_json))
        return all_switch_json

async def _call_getnetworkswitchstp(aiomeraki, switch, **kwargs):
    try:
        returned_json = await aiomeraki.switch.getNetworkSwitchStp(
            networkId=switch['networkId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=switch)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=switch)
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
                keys_added = add_keys(input_json=switch, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=switch, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getnetworkswitchstp(apikey, debug_dict, switches, **kwargs):
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

        switch_tasks = [
            _call_getnetworkswitchstp(aiomeraki, switch, **kwargs) for switch in switches
            ]
        all_switch_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(switch_tasks),
                total=len(switch_tasks),
                colour='green',
        ):
            switch_json = await task
            if switch_json:
                all_switch_json.extend(iter(switch_json))
        return all_switch_json

async def _call_getorganizationconfigtemplateswitchprofiles(aiomeraki, switch, **kwargs):
    try:
        returned_json = await aiomeraki.switch.getOrganizationConfigTemplateSwitchProfiles(
            organizationId=switch['organizationId'],
            configTemplateId=switch['configTemplateId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=switch)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=switch)
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
                keys_added = add_keys(input_json=switch, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=switch, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getorganizationconfigtemplateswitchprofiles(apikey, debug_dict, switches, **kwargs):
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

        switch_tasks = [
            _call_getorganizationconfigtemplateswitchprofiles(aiomeraki, switch, **kwargs) for switch in switches
            ]
        all_switch_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(switch_tasks),
                total=len(switch_tasks),
                colour='green',
        ):
            switch_json = await task
            if switch_json:
                all_switch_json.extend(iter(switch_json))
        return all_switch_json

async def _call_getorganizationconfigtemplateswitchprofileports(aiomeraki, switch, **kwargs):
    try:
        returned_json = await aiomeraki.switch.getOrganizationConfigTemplateSwitchProfilePorts(
            organizationId=switch['organizationId'],
            configTemplateId=switch['configTemplateId'],
            profileId=switch['profileId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=switch)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=switch)
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
                keys_added = add_keys(input_json=switch, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=switch, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getorganizationconfigtemplateswitchprofileports(apikey, debug_dict, switches, **kwargs):
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

        switch_tasks = [
            _call_getorganizationconfigtemplateswitchprofileports(aiomeraki, switch, **kwargs) for switch in switches
            ]
        all_switch_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(switch_tasks),
                total=len(switch_tasks),
                colour='green',
        ):
            switch_json = await task
            if switch_json:
                all_switch_json.extend(iter(switch_json))
        return all_switch_json

async def _call_getorganizationconfigtemplateswitchprofileport(aiomeraki, switch, **kwargs):
    try:
        returned_json = await aiomeraki.switch.getOrganizationConfigTemplateSwitchProfilePort(
            organizationId=switch['organizationId'],
            configTemplateId=switch['configTemplateId'],
            profileId=switch['profileId'],
            portId=switch['portId'],
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=switch)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=switch)
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
                keys_added = add_keys(input_json=switch, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=switch, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getorganizationconfigtemplateswitchprofileport(apikey, debug_dict, switches, **kwargs):
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

        switch_tasks = [
            _call_getorganizationconfigtemplateswitchprofileport(aiomeraki, switch, **kwargs) for switch in switches
            ]
        all_switch_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(switch_tasks),
                total=len(switch_tasks),
                colour='green',
        ):
            switch_json = await task
            if switch_json:
                all_switch_json.extend(iter(switch_json))
        return all_switch_json

async def _call_getorganizationswitchportsbyswitch(aiomeraki, switch, **kwargs):
    try:
        returned_json = await aiomeraki.switch.getOrganizationSwitchPortsBySwitch(
            organizationId=switch['organizationId'],
            total_pages='all',
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        error_data = return_message(data=switch)
        print('Meraki AIO API Error:\n')
        if error_data:
            for key, value in error_data.items():
                print(f'\t{ key }: { value }')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        error_data = return_message(data=switch)
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
                keys_added = add_keys(input_json=switch, output_json=each_dict)
                updated_json.append(keys_added)

        elif isinstance(returned_json, (dict)):
            updated_json = []
            keys_added = add_keys(input_json=switch, output_json=returned_json)
            updated_json.append(keys_added)        
        else:
            print('returned_json does not match type dict or list')

        return updated_json
    
    else:
        return None

async def _async_getorganizationswitchportsbyswitch(apikey, debug_dict, switches, **kwargs):
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

        switch_tasks = [
            _call_getorganizationswitchportsbyswitch(aiomeraki, switch, **kwargs) for switch in switches
            ]
        all_switch_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(switch_tasks),
                total=len(switch_tasks),
                colour='green',
        ):
            switch_json = await task
            if switch_json:
                all_switch_json.extend(iter(switch_json))
        return all_switch_json
