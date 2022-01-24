from django.shortcuts import render
from otherpage.models import Statistics
from datetime import date, datetime
from django.forms.models import model_to_dict
import json
from django.http import JsonResponse

# Create your views here.


def load_statistics(request):
    today = date.today()

    # 날짜 선택 시
    if request.method == 'POST':
        select_date = json.loads(request.body.decode("utf-8"))
        strpdate = datetime.strptime(select_date['select_data'], "%Y-%m-%d")
        data = Statistics.objects.filter(
            emo_date__year=strpdate.year, emo_date__month=strpdate.month, emo_date__day=strpdate.day)
        json_data = []
        for item in data:
            json_data.append(model_to_dict(item))

        return JsonResponse(json_data, safe=False)
    else:
        data = Statistics.objects.filter(
            emo_date__year=today.year, emo_date__month=today.month, emo_date__day=today.day)
    return render(
        request, 'otherpage/show.html',
        {'data': data,
         'today': today}
    )
