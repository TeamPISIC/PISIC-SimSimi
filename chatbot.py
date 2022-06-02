import requests
import asyncio
from dotenv import load_dotenv
import os
import csv
import pandas as pd

load_dotenv()

headers = {
    'x-api-key': os.environ.get('API_KEY'),
}

# 질문 데이터 가져오기
f = open('sampleData.csv', 'r', encoding='utf-8-sig')
rdr = csv.reader(f)

result = []


async def getData():
    for str_text in rdr:
        json_data = {
            'utext': str_text[0],
            'lang': 'ko',
            # 'lang': 'en',
        }

        response = requests.post(
            'https://wsapi.simsimi.com/190410/talk', headers=headers, json=json_data)
        result.append([str_text[0], response.json().get('atext')])

asyncio.run(getData())

f.close()

df = pd.DataFrame(result, columns=['Question', 'Answer'])
df.to_excel('result.xlsx', index=False)

print("심심이 API 질문-답변 작업 완료!")
