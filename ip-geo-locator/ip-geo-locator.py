import argparse
import requests

from bs4 import BeautifulSoup



def geo_locate(ip):
    try:
        r = requests.get("https://tools.keycdn.com/geo.json?host={}".format(ip))
        # r = requests.get()
    except Exception:
        return "Failed to establish connection"

    if r.status_code != requests.codes.ok:
        return "not available"
    
    return r.json()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("ip", help="ip address you wish to locate", type=str)
    args = parser.parse_args()

    location = geo_locate(args.ip)

    print(location['data']['geo']['country_name'])

    print(" IP Location finder by KeyCDN https://tools.keycdn.com/geo")

    # print(" City: ", location['city'])
