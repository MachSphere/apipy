import json
import os


def open_config_files(json_data):
    path_to_json_files = 'config/'
    json_files = [pos_json for pos_json in os.listdir(path_to_json_files) if pos_json.endswith('json')]

    for dex, js in enumerate(json_files):
        with open(os.path.join(path_to_json_files, js)) as json_file:
            json_array = json.load(json_file)
            for item in json_array:
                json_details = {'uri': item['uri'], 'status_code': item['status_code'],
                                'response_file': item['response_file'], 'operation': item['operation']}
                json_data.append(json_details)

    return json_data


def open_response_file(filename):
    path_to_resp_files = 'response_files/'

    with open(os.path.join(path_to_resp_files, filename)) as json_file:
        json_resp_data = json.load(json_file)
        return json_resp_data
