import requests, execjs, json, sys
from GoogleFreeTrans.CalcTk import CalcTk
import time


class translator():
    headers = {
        'Host': 'translate.google.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/2010'
                      '0101 Firefox/50.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
        'Referer': 'https://translate.google.cn/',
        'Cookie': 'NID=101=pkAnwSBvDm2ACj2lEVnWO7YEPUoWCTges7B7z2jJNyrNwAZ2OL9F'
                   'FOQLpdethA_20gCVqukiHnVm1hUbMGZc_ItQFdP5AHoq5XoMeEORaeidU19'
                   '6NDVRsrAu_zT0Yfsd; _ga=GA1.3.1338395464.1492313906',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0'
    }
    support_lauguage = {'afrikaans': 'af',
                        'arabic': 'ar',
                        'belarusian': 'be',
                        'bulgarian': 'bg',
                        'catalan': 'ca',
                        'czech': 'cs',
                        'welsh': 'cy',
                        'danish': 'da',
                        'german': 'de',
                        'greek': 'el',
                        'english': 'en',
                        'esperanto': 'eo',
                        'spanish': 'es',
                        'estonian': 'et',
                        'persian': 'fa',
                        'finnish': 'fi',
                        'french': 'fr',
                        'irish': 'ga',
                        'galician': 'gl',
                        'hindi': 'hi',
                        'croatian': 'hr',
                        'hungarian': 'hu',
                        'indonesian': 'id',
                        'icelandic': 'is',
                        'italian': 'it',
                        'hebrew': 'iw',
                        'japanese': 'ja',
                        'korean': 'ko',
                        'latin': 'la',
                        'lithuanian': 'lt',
                        'latvian': 'lv',
                        'macedonian': 'mk',
                        'malay': 'ms',
                        'maltese': 'mt',
                        'dutch': 'nl',
                        'norwegian': 'no',
                        'polish': 'pl',
                        'portuguese': 'pt',
                        'romanian': 'ro',
                        'russian': 'ru',
                        'slovak': 'sk',
                        'slovenian': 'sl',
                        'albanian': 'sq',
                        'serbian': 'sr',
                        'swedish': 'sv',
                        'swahili': 'sw',
                        'thai': 'th',
                        'filipino': 'tl',
                        'turkish': 'tr',
                        'ukrainian': 'uk',
                        'vietnamese': 'vi',
                        'yiddish': 'yi',
                        'chinese_simplified': 'zh-CN',
                        'chinese_traditional': 'zh-TW'}

    def __init__(self, src='en', dest='fr', updata_time=600):
        if src not in self.support_lauguage and src not in self.support_lauguage.values():
            raise ValueError('source language not support')
        if dest not in self.support_lauguage and dest not in self.support_lauguage.values():
            raise ValueError('destination language not support')
        self.url = 'https://translate.google.cn/translate_a/single'
        self.params = {
            'client': 't',
            'sl': src,
            'tl': dest,
            'hl': 'zh-CN',
            'dt': 'at', 'dt': 'bd',
            'dt': 'ex', 'dt': 'ld', 'dt': 'md',
            'dt': 'qca', 'dt': 'rw', 'dt': 'rm', 'dt': 'ss', 'dt': 't',
            'ie': 'UTF-8', 'oe': 'UTF-8', 'source': 'bh', 'ssel': '0',
            'tsel': '0', 'kc': '1', 'tk': '376032.257956'
        }
        self.updata_time = updata_time
        self.__updata_tk()

    def translate(self, text, multi=False):
        if time.time() > self.__next_up_time:
            self.__updata_tk()
        data = {'q': text}
        self.params['tk'] = self.__TK.get_tk(text)
        res = self.__get_res(data)
        ret_list = json.loads(res.text)
        if multi:
            return ret_list
        return ret_list[0][0][0]

    def __updata_tk(self):
        self.__TK = CalcTk()
        self.__next_up_time = time.time() + self.updata_time

    def __get_res(self, data):
        res = requests.post(self.url,
                            headers=self.headers,
                            data=data,
                            params=self.params,
                            timeout=6)
        res.raise_for_status()
        return res
