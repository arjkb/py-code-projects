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

    # soup = BeautifulSoup(r.text, 'html.parser')
    # td = soup.find_all("td")

    # d = dict()
    # d['ip'] = td[0].string
    # d['country'] = td[1].string
    # d['region'] = td[2].string
    # d['city'] = td[3].string
    # d['isp'] = td[4].string
    # d['organization'] = td[5].string


    # print(td[0].string) # ip
    # print(td[1].string) # Country
    # print(td[2].string) # Region
    # print(td[3].string) # City
    # print(td[4].string) # ISP
    # print(td[5].string) # Organization
    # # return d
    # return ""
    return r.json()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("ip", help="ip address you wish to locate", type=str)
    args = parser.parse_args()

    location = geo_locate(args.ip)

    print(location['data']['geo']['country_name'])

    print(" IP Location finder by KeyCDN https://tools.keycdn.com/geo")

    # print(" City: ", location['city'])
