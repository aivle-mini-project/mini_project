import requests,json

url = "https://naveropenapi.apigw.ntruss.com/sentiment-analysis/v1/analyze"
data = {
  "content": "싸늘하다. 가슴에 비수가 날아와 꽂힌다."
}

id ="o1s9i33mtw"
pw ="viL65VriHfxF79DM5t0cFyzQ5rMGEJYGgfFDe1zQ"
headers = {"Content-Type":"application/json",
        "X-NCP-APIGW-API-KEY-ID":id,
        "X-NCP-APIGW-API-KEY":pw, }

res = requests.post(url ,data = json.dumps(data) , headers= headers)
res.encoding ='UTF-8'
print(res.status_code)



if res.status_code == 200:
  json_data = (json.loads(res.text))
  sentiment = json_data["document"]["sentiment"]
  print(sentiment)
else:
    print("Error"+res.text)