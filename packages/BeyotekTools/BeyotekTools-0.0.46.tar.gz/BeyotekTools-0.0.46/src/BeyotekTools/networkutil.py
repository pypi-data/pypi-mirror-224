import requests
import smtplib


def check_proxy(proxy):
    proxies = {
        "http": f"http://{proxy}",
        "https": f"http://{proxy}"
    }

    try:
        requests.get("https://google.com/", proxies=proxies)
        return True

    except:
        return False


def get_public_ip():
    ip = requests.get('https://api.ipify.org').content.decode('utf8')
    return ip


