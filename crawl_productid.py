import requests 
import time
import random
import pandas as pd


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi-VN,vi;q=0.8,en-US;q=0.5,en;q=0.3',
    'Referer': 'https://tiki.vn/?src=header_tiki',
    'x-guest-token': '8jWSuIDBb2NGVzr6hsUZXpkP1FRin7lY',
    'Connection': 'keep-alive',
    'TE': 'Trailers',
}

params = {
    'limit': '48',
    'include': 'sale-attrs,badges,product_links,brand,category,stock_item,advertisement',
    'aggregations': '1',
    'trackity_id': '70e316b0-96f2-dbe1-a2ed-43ff60419991',
    'category': '1883',
    'page': '1',
    'src': 'c1883',
    'urlKey':  'nha-cua-doi-song',
}
#link chứng ta thấy các thay đổi là header và params
product_id = [] #tạo 1 list rõng để chứa
for i in range(1, 11): #vòng lặp chạy lấy 10page
    params['page'] = i
    response = requests.get('https://tiki.vn/api/v2/products', headers=headers, params=params)
    if response.status_code == 200:#respone 200 thi web chạy
        print('request success!!!')
        for record in response.json().get('data'):#respose sẽ trỏ tới thằng data v
            product_id.append({'id': record.get('id')})#à sau đó lấy ra id của nó và thêm vào list product_id
    time.sleep(random.randrange(3, 10))#cho nó tgian chờ 3-10s
#và sau đó chúng ta sẻ cho nó vào dataframe và lưu nó
df = pd.DataFrame(product_id)
df.to_csv('product_id.csv', index=False)