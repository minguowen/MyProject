# CrowTaobaoPrice.py
import requests
import re


def getHTMLText(url):
    try:
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
            "cookie": "_uab_collina=157258226625083933457665; thw=cn; t=36d1cd24cf0143fb6accdf025534d197; enc=97GhrHhKkErSIlgzQuOf4gDv8yB1IDMrzS%2FqNp8OhQXosfA5%2Bpm6Vj4%2B%2FjCYIIsIglI%2FeakHaMTRg2bsOCGe%2Fg%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; cookie2=130c64bc2ccdc80f7d3858f7c4143707; _tb_token_=ede063be6e3ee; XSRF-TOKEN=a5e7e17c-f1d8-4ece-8f63-20dd0adc170c; mt=ci=0_0; cna=PpdBFupPaykCAbdAPqcqw59D; isg=BFlZdWsdY9ah6DznWNPShWvxaEwz5k2YGu7yC3sO5wD_gngUwTA4a72QgAZROuXQ; l=cBLufjhqqvUwqS6yBOCZhurza7799IRAguPzaNbMi_5CU6L65G7Oovk9xFp6cjWdOrYp4-ERe5p9-eteiNF7dhspXUJ1."
        }
        r = requests.get(url, timeout=30, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "搜索错误！"


def parsePage(ilt, html):
    try:
        plt = re.findall(r'"view_price":"[\d\.]*"', html)
        tlt = re.findall(r'"raw_title":".*?"', html)

        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price, title])
    except:
        print("查找异常！")


def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))


def main():
    goods = '书包'
    depth = 1
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44 * i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)


main()
