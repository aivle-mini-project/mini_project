from django.shortcuts import render
from sqlalchemy import true
from otherpage.models import Statistics
from diary.models import Diary, DiaryDetail, DiaryDetailHighlight
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
        json_data = []
        if(len(data) == 0):
            json_data.append({
                'emo_date': today.strftime("%Y-%m-%d"),
                'positive': 0,
                'neutral': 0,
                'negative': 0,
            })
        for item in data:
            json_data.append(model_to_dict(item))

    return render(
        request, 'otherpage/show_date.html',
        {'data': json_data,
         'today': today}
    )


def show_date_keyword(request):
    # today = date.today()
    today = datetime.strptime('2022-01-25', "%Y-%m-%d")

    # 날짜 선택 시
    if request.method == 'POST':
        select_date = json.loads(request.body.decode("utf-8"))
        strpdate = datetime.strptime(select_date['select_data'], "%Y-%m-%d")
        temp_data = Diary.objects.filter(
            register_date__year=strpdate.year, register_date__month=strpdate.month, register_date__day=strpdate.day)
        pushdata = {}
        pushdata['select_date'] = select_date['select_data']
        pushdata['result_data'] = []
        for diary_data in temp_data:
            diary_d_datas = diary_data.diarydetail_set.all()
            for diary_d_data in diary_d_datas:
                tempdict = {}
                diary_d_dict = model_to_dict(diary_d_data)
                tempdict['sentence'] = diary_d_dict['write']
                diary_d_h_datas = diary_d_data.diarydetailhighlight_set.all()
                for diary_d_h_data in diary_d_h_datas:
                    diary_d_h_dict = model_to_dict(diary_d_h_data)
                    tempdict['offset'] = []
                    tempdict['length'] = []
                    tempdict['emotion'] = []
                    tempdict['offset'].append(
                        diary_d_h_dict['offset'])
                    tempdict['length'].append(
                        diary_d_h_dict['length'])
                    tempdict['emotion'].append(
                        diary_d_dict['emotion'])
                pushdata['result_data'].append(tempdict)

        return JsonResponse(pushdata, safe=False)
    else:
        temp_data = Diary.objects.filter(
            register_date__year=today.year, register_date__month=today.month, register_date__day=today.day)
        pushdata = []
        for diary_data in temp_data:
            diary_d_datas = diary_data.diarydetail_set.all()
            for diary_d_data in diary_d_datas:
                tempdict = {}
                diary_d_dict = model_to_dict(diary_d_data)
                tempdict['sentence'] = diary_d_dict['write']
                diary_d_h_datas = diary_d_data.diarydetailhighlight_set.all()
                for diary_d_h_data in diary_d_h_datas:
                    diary_d_h_dict = model_to_dict(diary_d_h_data)
                    tempdict['highlight'] = {
                        'offset': [], 'length': [], 'emotion': []}
                    tempdict['highlight']['offset'].append(
                        diary_d_h_dict['offset'])
                    tempdict['highlight']['length'].append(
                        diary_d_h_dict['length'])
                    tempdict['highlight']['emotion'].append(
                        diary_d_dict['emotion'])
                pushdata.append(tempdict)

    return render(
        request, 'otherpage/show_date_keyword.html',
        {'data': pushdata,
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
