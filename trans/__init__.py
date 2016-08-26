# coding: utf-8
import requests
import sys

__API__ = "http://fanyi.youdao.com/openapi.do"
__KEYFROM__ = "readdaily"
__KEY__ = "1109388733"
__TYPE__ = "data"
__DOCTYPE__ = "json"
__VERSION__ = "1.1"

def get_params(key, value):
    base_params = dict({
        "keyfrom": __KEYFROM__,
        "key": __KEY__,
        "type": __TYPE__,
        "doctype": __DOCTYPE__,
        "version" : __VERSION__
    })
    if not base_params.get(key):
        base_params[key] = value
    return base_params

def request(url, q):
    try:
        r = requests.get(url, params=get_params("q", q))
        return get_value(r.json())
    except:
        print "Sorry, something wrong!"
        sys.exit()

def get_value(json):
    value_list = json["web"][0]["value"]
    value = "; ".join(map(lambda s : s.encode("utf-8"), value_list))
    return value

def get_input():
    length = len(sys.argv)
    if length == 2:
        return sys.argv[1]
    else:
        return raw_input("待翻译：")

def main():
    q = get_input()
    value = request(__API__, q)
    print q, value
    sys.exit()

if __name__ == '__main__':
    main()