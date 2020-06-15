# apipy 0.0.1

A small project to test API calls and responses on your local machine

## Getting Started

Clone this repo to your development machine, have the prerequisites installed and follow the installation steps.


#### Prerequisites
- Python 3.6+
- Pip
- Flask

#### Installing
Head to the [Python website](https://www.python.org/downloads/), download and install Python by following the installation instructions relevant to you operating system.

Next install pip by following the instructions [here](https://pip.pypa.io/en/stable/installing/).

Finally install Flask via pip by running the following command in command prompt or terminal window:

```
pip install flask
```

With a command prompt or terminal window, navigate to the directory where the repository is downloaded and run the following command:

```
python api.py
```

Open a browser window and type into the URL bar

```
localhost:5000/api/test
```

If all goes well and the code is running as it should be you should see a JSON response as defined in the test.json file found under
the 'response_files' directory. You can add more entries into the api_entries.json to use different API URIs.
Each API URI can be configured to return a different response file under a different operation (GET, POST, PUT) and status code.

This should allow you to test your API consumer for different operations and response code status returns.

The api_entries.json is read by the system every 5 minutes, so there is no reason other than impatience to restart the application.

## Authors
**Calum Ludwig**

## License
This project is licensed under GNU Public License - see the License.md file for details