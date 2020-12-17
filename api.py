import time

from flask import Flask, request, make_response

from application import Configuration

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

    #check if we need to update our api rules again
    if elapsed_time >= 120:
        json_data = []

        define_api_rules()
        time_obj = time.time()


def get_response_data(request_uri, request_method):
    if not json_data:
        Configuration.open_config_files(json_data)

    time_elapsed()

    for item in json_data:
        if str(item['uri']).__eq__(request_uri):
            operation = item['operation']
            response_file = item['response_file']

            if operation == request_method and response_file:
                return {'response': Configuration.open_response_file(response_file), 'status_code': item['status_code']}

    #If the system cannot find the URI or operation associated to URL it returns 404
    return {'response': 'NA', 'status_code': 404}


def define_api_rules():
    if not json_data:
        Configuration.open_config_files(json_data)

    for item in json_data:
        app.add_url_rule(str(item['uri']), endpoint='index', view_func=index, provide_automatic_options=False)


if __name__ == '__main__':
    define_api_rules()
    app.run()
