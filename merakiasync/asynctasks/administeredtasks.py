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

async def _call_getadministeredidentitiesme(aiomeraki, **kwargs):
    try:
        returned_json = await aiomeraki.administered.getAdministeredIdentitiesMe(
            **kwargs)

    except meraki.exceptions.AsyncAPIError as e:
        print('Meraki AIO API Error:\n')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    except Exception as e:
        print('Non Meraki API Error:\n')
        print(f'\tError: \n \t{ e }')
        returned_json = None

    if returned_json:
        if isinstance(returned_json, (dict)):
            return [returned_json]

        if isinstance(returned_json, (list)):
            return returned_json

    
    else:
        return None

async def _async_getadministeredidentitiesme(apikey, debug_dict, **kwargs):
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

        administered_tasks = [_call_getadministeredidentitiesme(aiomeraki=aiomeraki, **kwargs)]
        all_administered_json = []

        for task in tqdm.tqdm(
                asyncio.as_completed(administered_tasks),
                total=len(administered_tasks),
                colour='green',
        ):
            administered_json = await task
            if administered_json:
                all_administered_json = administered_json
        return all_administered_json
