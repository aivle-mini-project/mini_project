from django.shortcuts import render
from sqlalchemy import true
from otherpage.models import Statistics
from datetime import date, datetime, timedelta
from django.forms.models import model_to_dict
import json
from django.http import JsonResponse

# Create your views here.


def show_date(request):
    today = date.today()

    # 날짜 선택 시
    if request.method == 'POST':
        select_date = json.loads(request.body.decode("utf-8"))
        strpdate = datetime.strptime(select_date['select_data'], "%Y-%m-%d")
        data = Statistics.objects.filter(
            emo_date__year=strpdate.year, emo_date__month=strpdate.month, emo_date__day=strpdate.day)
        json_data = []
        # 해당 날짜에 DB값이 없을 때,
        if(len(data) == 0):
            json_data.append({
                'emo_date': select_date['select_data'],
                'positive': 0,
                'neutral': 0,
                'negative': 0,
            })
        for item in data:
            json_data.append(model_to_dict(item))

        return JsonResponse(json_data, safe=False)
    else:
        data = Statistics.objects.filter(
            emo_date__year=today.year, emo_date__month=today.month, emo_date__day=today.day)
    return render(
        request, 'otherpage/show_date.html',
        {'data': data,
         'today': today}
    )


def show_week(request):
    today = date.today()
    # 날짜 선택 시
    if request.method == 'POST':
        select_date = json.loads(request.body.decode("utf-8"))
        strpdate = datetime.strptime(select_date['select_data'], "%Y-%m-%d")
        data = Statistics.objects.filter(
            emo_date__range=["2000-01-01", strpdate]).order_by('-emo_date')[:7]
        week_data = []
        for item in data:
            week_data.append(model_to_dict(item))
        while(True):
            if(len(week_data) == 7):
                break
            else:
                temp_date = (strpdate + timedelta(days=-len(week_data)))

                week_data.append({
                    'emo_date': temp_date.strftime("%Y-%m-%d"),
                    'positive': 0,
                    'neutral': 0,
                    'negative': 0,
                })
        return JsonResponse(week_data, safe=False)
    else:
        # 오늘 날짜로부터 7일간의 데이터 꺼내옴
        data = Statistics.objects.order_by('-emo_date')[:7]
        week_data = []
        for item in data:
            week_data.append(model_to_dict(item))

    return render(
        request, 'otherpage/show_week.html',
        {'data': week_data,
         'today': today}
    )
