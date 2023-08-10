import requests

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