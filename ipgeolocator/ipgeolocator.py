# program to find the geographical location of an ip address
# IP Location finder by KeyCDN https://tools.keycdn.com/geo

import argparse
import requests

def geo_locate(ip):
    if not is_valid(ip):
        print("Invalid IP address")
        return None

    try:
        r = requests.get("https://tools.keycdn.com/geo.json?host={}".format(ip))
    except Exception:
        print("Failed to establish connection")
        return None

    if r.status_code != requests.codes.ok:
        print("not available")
        return None

    return r.json()

def is_valid(ip):
    try:
        octets = list(map(int, ip.split('.')))
    except Exception as e:
        return False
    else:
        return (len(octets) == 4) and all(map(lambda x: 0 <= x <= 255, octets))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("ip", help="ip address you wish to locate", type=str)
    args = parser.parse_args()

    location = geo_locate(args.ip)
    if location == None or location['status'] == 'error':
        print("Lookup failed!")
        exit(1)

    geo = location['data']['geo']
    isp = geo['isp'].strip()
    city = geo['city'].strip()
    region = geo['region'].strip()
    country = geo['country_name'].strip()

    print(" {}, {}, {}, {}".format(isp, city, region, country))
    print(" IP Location finder by KeyCDN https://tools.keycdn.com/geo")
