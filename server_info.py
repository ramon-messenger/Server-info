import datetime
import json
import requests
import sys
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)  # pylint: disable=no-member

# apikey = 'a806335f8a074179bc6c93814592afb1'  # Temp key, expires 2024-04-18 12:00:26
# apiurl = 'https://yodalab.savvis.net/api'
apikey = '0d788c64f5b04d119e52b20e3079af99' # permenent Key : No expire Date
apiurl = 'https://yoda.savvis.net/api'
session = requests.session()
session.proxies.update('')
session.headers['x-api-key'] = apikey

def search(param: str) -> None:
    """ Query Yoda API for server details """
    url = f"{apiurl}/server01?search={param}"
    try:
        print(f"{str(datetime.datetime.now())[:-3]} - Searching for '{param}': ", end='')
        response = session.get(url, verify=False)
        if response.status_code == 404:
            print("Not found")
        else:
            response.raise_for_status()
            result: dict = json.loads(response.content.decode("utf-8"))
            print(f"{len(result)} found")
            # Do whatever you want with it, printing for now
            for count in result:
                print(f"{str(datetime.datetime.now())[:-3]} - Result {count}")
                for k, v in result[count].items():
                    print(f"\t{k}: {v}")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP ERROR occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"CONNECTION ERROR occurred: {conn_err}")
    except requests.exceptions.ReadTimeout as time_err:
        print(f"TIMEOUT ERROR occurred: {time_err}")
    except json.decoder.JSONDecodeError as jd_err:
        print(f"JSONDecodeError ERROR occurred: {jd_err}")
    except TypeError as type_err:
        print(f"TypeError occurred: {type_err}")
    except Exception as err:  # pylint: disable=broad-except
        print(f"ERROR occurred: {err}")



def main(argv: list) -> str:
    """ Iterate through search arguments """
    if len(argv) > 1:
        print(f"{str(datetime.datetime.now())[:-3]} - {len(argv) - 1} search arguments supplied")
        for i in range(1, len(argv)):
            search(argv[i])
        print(f"{str(datetime.datetime.now())[:-3]} - Search complete")
    else:
        print("Search argument required")
        exit(1)



if __name__ == '__main__':
    main(sys.argv)
