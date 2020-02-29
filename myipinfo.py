import ipinfo
import pprint, requests, sys


def get_ip_info(ip_address: str, token: str):
    """get full ip address info from the ipinfo.io api"""

    handler = ipinfo.getHandler(token)
    details = handler.getDetails(ip_address)
    return details.all


if __name__ == "__main__":
    if len(sys.argv) == 1:
        ip = "" # empty string represents the user's ip
    else:
        ip = sys.argv[1]

    access_token = "3e99795f099a0a" # get your access token from ipinfo.io
    try:
        pprint.pprint(get_ip_info(ip, access_token), indent=3)
    except requests.exceptions.HTTPError:
        print("Can't reach ipinfo.io, Check your access token!")
    except requests.exceptions.ConnectionError:
        print("Can't connect, Check your internet connection!")
