import unicodecsv as ucsv

data = [['感兴趣的领域','票数'],['金融',172],['医疗保健',136],['市场业',135],['零售业',101],['制造业',80]
        ,['司法',68],['工程与科学',50],['保险业',29],['其他',41]]
with open('..\\csv\\result.csv','wb') as f:
    w = ucsv.writer(f,encoding='gbk')
    w.writerows(data)