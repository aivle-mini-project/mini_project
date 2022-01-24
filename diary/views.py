from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.forms.models import model_to_dict
from django.utils import timezone
from .models import Diary
from .forms import DiaryForm
import requests,json
from django.core.exceptions import ValidationError

# Create your views here.
def create(request):
    if "username" in request.session:
        return render(request, 'diary/create_diary.html')

def detail(request):
    if request.method == 'POST':
        form = DiaryForm(request.POST)
        if form.is_valid():
            try:
                text = form.cleaned_data['write']
                print(text,"valid")
            #text = request.POST.get('input1') 
                url = "https://naveropenapi.apigw.ntruss.com/sentiment-analysis/v1/analyze"
                data = {
                "content": text
                }
                id ="j7n6px1uvx"
                pw ="jRa6fHWYxG5qwQC9VqtjpFrXOA4GhsQQoXEEnVEf"
                headers = {"Content-Type":"application/json",
                        "X-NCP-APIGW-API-KEY-ID":id,
                        "X-NCP-APIGW-API-KEY":pw, }
                #print(headers)
                res = requests.post(url ,data = json.dumps(data) , headers= headers)
                res.encoding ='UTF-8'
                #result = json.loads(res.text)
                ####실험용 dictionary############
                result = {
                        "document": {
                            "sentiment": "negative",
                            "confidence": {
                                "neutral": 0.14525136640572725,
                                "positive": 0.00186876227013191,
                                "negative": 0.8528798713241407
                            }
                        },
                        "sentences": [
                            {
                                "content": "싸늘하다.",
                                "offset": 0,
                                "length": 5,
                                "sentiment": "negative",
                                "confidence": {
                                    "negative": 0.9961358904838562,
                                    "positive": 0.0036366574931889772,
                                    "neutral": 0.0002274021098855883
                                },
                                "highlights": [
                                    {
                                        "offset": 0,
                                        "length": 4
                                    }
                                ]
                            },
                            {
                                "content": " 가슴에 비수가 날아와 꽂힌다.",
                                "offset": 5,
                                "length": 17,
                                "sentiment": "negative",
                                "confidence": {
                                    "negative": 0.927976131439209,
                                    "positive": 0.07131962478160858,
                                    "neutral": 0.0007042606011964381
                                },
                                "highlights": [
                                    {
                                        "offset": 1,
                                        "length": 15
                                    }
                                ]
                            }
                        ]
                    }
                #####제거 부분 (DB저장)

                return render(request,'diary/diary_detail.html',result)
                print(res.status_code)
                if res.status_code == 200:
                    #Diary 모델에 넣기
                    return render(request,'diary/diary_detail.html',result)
                else:
                    print("Error"+res.text)
            except ValidationError as e:
                print("eeeeeerrrrrrrrrrrrrorrrrrrrrrrrrrrrrrrrrr")
        else:
            print("invalid", form.errors)
        
    else:
        form =DiaryForm()

    return render(request, 'diary/create_diary.html',{'form':form})


