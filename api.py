from flask import Flask, request, make_response
import os, json, time

app = Flask(__name__)
json_data = []
time_obj = time.time()


def index():
    response_dict = get_response_data(request.__dict__['environ']['REQUEST_URI'],
                                      request.__dict__['environ']['REQUEST_METHOD'])
    print(response_dict)
    return make_response(response_dict['response'], response_dict['status_code'])


index.provide_automatic_options = False
index.methods = ['GET', 'POST', 'PUT']


def time_elapsed():
    global time_obj
    global json_data
    elapsed_time = time.time() - time_obj

    if elapsed_time >= 60:
        json_data = []

        define_api_rules()
        time_obj = time.time()


def get_response_data(request_uri, request_method):
    if not json_data:
        open_config_files()

    time_elapsed()

    for item in json_data:
        if str(item['uri']).__eq__(request_uri):
            operation = item['operation']
            response_file = item['response_file']

            if operation == request_method and response_file:
                return {'response': open_response_file(response_file), 'status_code': item['status_code']}

    return {'response': 'NA', 'status_code': 404}


def define_api_rules():
    if not json_data:
        open_config_files()

    for item in json_data:
        app.add_url_rule(str(item['uri']), endpoint='index', view_func=index, provide_automatic_options=False)


def open_config_files():
    path_to_json_files = 'config/'
    json_files = [pos_json for pos_json in os.listdir(path_to_json_files) if pos_json.endswith('json')]

    for dex, js in enumerate(json_files):
        with open(os.path.join(path_to_json_files, js)) as json_file:
            json_array = json.load(json_file)
            for item in json_array:
                json_details = {'uri': item['uri'], 'status_code': item['status_code'],
                                'response_file': item['response_file'], 'operation': item['operation']}
                json_data.append(json_details)


def open_response_file(filename):
    path_to_resp_files = 'response_files/'

    with open(os.path.join(path_to_resp_files, filename)) as json_file:
        json_resp_data = json.load(json_file)
        return json_resp_data


if __name__ == '__main__':
    define_api_rules()
    app.run()
