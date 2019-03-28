import requests
import re
import execjs
import time


def get_res(url):
    """get raw html from 'https://translate.google.cn/' """
    try:
        res = requests.get(url, timeout = 1.5)
        res.raise_for_status()
        #res.encoding = 'utf-8'
        return res
    except Exception as ex:
        print('[-]ERROR: ' + str(ex))
        return res


def get_tkk():
    """get the tkk"""
    url = 'https://translate.google.cn/'
    retry = 3
    time_interval = 3
    while retry > 0:
        try:
            res = get_res(url)
            tkk = re.search(r'tkk\:\'(\d+\.\d+)?\'', res.text).group(1)
            return tkk
        except requests.exceptions.ReadTimeout as ex:
            time.sleep(time_interval)
            time_interval += 1
            retry -= 1
    raise requests.exceptions.ReadTimeout("can't visit https://translate.google.cn/")
