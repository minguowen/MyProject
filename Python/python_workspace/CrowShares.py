# -------------------------------------------------------------------------------
# 任务：定向爬取股票数据
# 技术路线：requests-BeautifulSoup-re
# 股票列表获取：东方财富网
# 股票信息获取：雪球网
# 因为雪球网与百度股票的html是不一样的，因此只能通过搜索一个个属性中的数值来爬取
# 在这里仅爬取股票名称，股票价格，股票当前状态与交易时间
# 该代码的爬取结果：前小部分的股票仅能爬取到名字，后面大部分都能爬取到名称，价格，状态和时间，原因未知
# -------------------------------------------------------------------------------
import requests
from bs4 import BeautifulSoup
import traceback
import re


def getHTMLText(url, code='utf-8'):
    try:
        # 东方财富网的列表数据可以直接获取，但是爬取雪球网需要就行浏览器的伪装
        kv = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        r = requests.get(url, headers=kv, timeout=30)
        r.raise_for_status()
        r.encoding = code
        return r.text
    except:
        return "1?"


# 从东方财富网爬取股票代码，并存入到列表中
def getStockList(lst, stockURL):
    html = getHTMLText(stockURL)
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.findAll('a')
    print(a[:100])
    for i in a[:100]:
        try:
            href = i.attrs['href']
            lst_s = re.findall(r"[s][hz]\d{6}", href)[0]
            # 根据雪球网的网址，股票代码前面的字母均需要变为大写
            lst.append(lst_s.upper())
        except:
            continue
    for lists in lst:
        print(lists)


# 从雪球网获取每个股票代码对应的股票信息
def getStockInfo(lst, stockURL, fpath):
    count = 0
    for stock in lst:
        url = stockURL + stock
        html = getHTMLText(url)
        try:
            # 如果网页为空，则跳过这一次，继续循环
            if html == "":
                continue
            infoDict = {}
            soup = BeautifulSoup(html, 'html.parser')

            # stock_name_Info=soup.find('div',attrs={'class':'page-row'})
            # .find如果无法查找到该属性，会返回NoneType，其值为None
            # 字典的更新需要一对键值对
            name = soup.find('div', attrs={'class': 'stock-name'})
            if name is None:
                infoDict.update({'股票名称': '查询不到该股票'})
                # print("查询不到该股票")
            else:
                infoDict.update({'股票名称': name.text.split()[0]})

            # stockInfo=soup.find_all('div',attrs={'class':'stock-info'})[0]
            price = soup.find('div', attrs={'class': 'stock-current'})
            if price is None:
                infoDict.update({'当前价格': '查询不到当前价格'})
                # print("无当前价格")
            else:
                infoDict.update({'当前价格': price.text.split()[0]})

            # keyList=stockInfo.find_all('td')
            # valueList=stockInfo.find_all('span')

            # for i in range(len(keyList)):
            # key=keyList[i].text
            # val=valueList[i].text
            # infoDict[key]=val

            with open(fpath, 'a', encoding='utf-8') as f:
                f.write(str(infoDict) + '\n')
                count = count + 1
                print('\r当前速度：{:.2f}%'.format(count * 100 / len(lst)), end="")
                # print("文件已经保存")
        except:
            traceback.print_exc()
            count = count + 1
            print('\r当前速度：{:.2f}%'.format(count * 100 / len(lst)), end="")
            # print("2?")
            continue


def main():
    stock_list_url = 'http://quote.eastmoney.com/stock_list.html'
    stock_info_url = 'https://xueqiu.com/S/'
    output_file = 'E:\OneDrive - bit.edu.cn\GitHub\MyProject\Python\python_workspace/BaiduStockInfo.txt'
    slist = []
    getStockList(slist, stock_list_url)
    getStockInfo(slist, stock_info_url, output_file)


if __name__ == '__main__':
    main()
