# Version: 1.1.2
# Author: 郑力中
# Without GUI


import time
import requests
from bs4 import BeautifulSoup

num = input("请输入基金代码：")
if num=='':
    print('错误：基金代码不能为空')
elif len(num)!=6:
    print('错误：请输入正确的基金代码，正确的基金代码为六位数')
else:
    url = 'http://fund.eastmoney.com/' + num + '.html'
    res = requests.get(url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text,features="html.parser")
    pre_QDII = soup.select('.infoOfFund a')
    QDII = pre_QDII[0].text
    pre_guzhi = soup.select('#gz_gszzl')
    guzhi = pre_guzhi[0].text
    pre_name = soup.select('.fundDetail-tit')
    name = pre_name[0].text

if QDII == 'QDII-指数':
    url_QDII = "http://jingzhi.funds.hexun.com/DataBase/jzzs.aspx?fundcode=" + num
    res_QDII = requests.get(url_QDII)
    res_QDII.encoding = 'utf-8'
    soup = BeautifulSoup(res_QDII.text,features="html.parser")
    pre_QDII_jingzhi = soup.select('#')
    print(pre_QDII_jingzhi)
else:
    pre_sum = soup.select('.RelatedInfo')
    sum_g = 10
    g = []
    while sum_g < 20:
        g.append(pre_sum[sum_g].text)
        sum_g = sum_g + 1
    sum_cou = 0
    final_count = 0
    cou = []
    while sum_cou < 10:
        cou.append(g[sum_cou].count('-'))
        final_count = final_count + cou[sum_cou]
        sum_cou = sum_cou + 1
    nowtime = time.strftime('%H:%M:%S',time.localtime(time.time()))
    print ('短期建议：')
    if nowtime[0:2] <= '14':
        if guzhi[0] == '+':
            print ('今日' + name + '估值为涨，预计涨幅'+ guzhi[1:6] + '，不需要任何操作。')
            print ('现在时间为' + nowtime + '还未即将收盘，建议等待14点后再运行决策系统。')
        else:
            print('今日' + name + '估值为跌，预计跌幅'+ guzhi[1:6] + '，可以进行适当加仓。')
            print('现在时间为' + nowtime + '还未即将收盘，建议等待14点后再运行决策系统。')
    else :
        if guzhi[0] == '+':
            print ('今日' + name + '估值为涨，预计涨幅'+ guzhi[1:6] + '，不需要任何操作。')
        else:
            print('今日' + name + '估值为跌，预计跌幅'+ guzhi[1:6] + '，可以进行适当加仓。')
    
    print ('')
    print ('长期建议：')
    print ('近10个交易日下跌' + str(final_count) + '次，建议：')
    if final_count >= 3:
        print ('加仓')
    else:
        print ('过高不买入')
    print ('')
    print ('！！！以上结果仅供参考！！！')
