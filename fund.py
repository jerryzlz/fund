# Version: 1.1.1
# Author: 郑力中
# Without GUI



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
    soup = BeautifulSoup(res.text,features="lxml")
    pre_QDII = soup.select('.infoOfFund a')
    QDII = pre_QDII[0].text
    pre_guzhi = soup.select('#gz_gszzl')
    guzhi = pre_guzhi[0].text
    pre_name = soup.select('.fundDetail-tit')
    name = pre_name[0].text

pre_sum = soup.select('.RelatedInfo')
g = [str(pre_sum[10].text),str(pre_sum[11].text),str(pre_sum[12].text),str(pre_sum[13].text),str(pre_sum[14].text),
    str(pre_sum[15].text),str(pre_sum[16].text),str(pre_sum[17].text),str(pre_sum[18].text),str(pre_sum[19].text)]
cou = [g[0].count('-'),g[1].count('-'),g[2].count('-'),g[3].count('-'),g[4].count('-'),
    g[5].count('-'),g[6].count('-'),g[7].count('-'),g[8].count('-'),g[9].count('-')]
final_count = cou[0] + cou[1] + cou [2] + cou [3] + cou[4] + cou[5] + cou[6] + cou[7] + cou [8] + cou [9]
if guzhi[0] == '+':
        print ('今日' + name + '估值为涨，预计涨幅'+ guzhi[1:6] + '，不需要任何操作')
else:
        print('今日' + name + '估值为跌，预计跌幅'+ guzhi[1:6] + '，可以进行适当加仓')

print ('')
print ('长期建议：')
print ('近10个交易日下跌' + str(final_count) + '次，建议：')
if final_count >= 3:
    print ("加仓")
else:
    print ('过高不买入')
print ('')
print ('！！！以上结果仅供参考！！！')
