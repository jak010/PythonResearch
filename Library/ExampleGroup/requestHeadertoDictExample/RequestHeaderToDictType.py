"""
 Rquest Header 정보를 가진 text 파일을 사전형 타입으로 바꿔주는 코드
"""

dict_header = dict()

with open("RequestHeaderExample.txt", "r", encoding="utf-8") as f:

    # for x in f.readlines():
    #     print(bytes(x,"utf-8"))

    value_data_parsing = ""
    for x in f.readlines():

        key,val = x.split(" ")[0], x.split(" ")[1::]
        if ":" in key:
            key = key.replace(":","")
        elif ("post" in key) or ("get" in key):
            continue

        for y in val:
            value_data_parsing += y
        dict_header[key] = value_data_parsing

        value_data_parsing = ""

from pprint import pprint
pprint(dict_header)