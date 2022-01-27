from django.shortcuts import render
from django.core.paginator import Paginator
from EDuser.models import Eduser
from EDuser.decorator import login_required
from diary.models import Diary
import json
from django.http import JsonResponse


@login_required
def likepage(request):
    print(request.session['username'])

    now_page = int(request.GET.get('page', 1))
    user = (request.session['username'])
    expressions = Eduser.objects.get(username=request.session.get('username')).expression_set.all()
    datas = expressions.order_by('-id')

    p = Paginator(datas, 5)

    info = p.get_page(now_page)

    start_page = (now_page - 1) // 10 * 10 + 1
    end_page = start_page + 9
    if end_page > p.num_pages:
        end_page = p.num_pages

    return render(request, 'mypage/likepage.html', {'user': user, 'info': info, 'page_range': range(start_page, end_page + 1)})


@login_required
def mypage(request):
    user = (request.session['username'])
    expressions = Eduser.objects.get(
        username=request.session.get('username')).expression_set.all()
    ex_len = len(expressions)

    mydiary = Eduser.objects.get(
        username=request.session.get('username')).diary_set.all()
    my_len = len(mydiary)

    img = str(Eduser.objects.get(
        username=request.session.get('username')).profile_img)
    if img:
        img = "http://127.0.0.1:8000/media/" + img + "/"
    else:
        img = "http://127.0.0.1:8000/media/profile/default.png/"
    return render(request, 'mypage/mypage.html', {'user': user, 'img': img, 'ex_len': ex_len, 'my_len': my_len})


@login_required
def mydiary(request):

    # 삭제버튼 눌렀을때
    if request.method == 'POST':
        json_data = json.loads(request.body.decode("utf-8"))
        diary = Diary.objects.get(id=json_data['id_number'])
        diary.delete()
        return JsonResponse("good", safe=False)

    now_page = int(request.GET.get('page', 1))
    user = (request.session['username'])
    expressions = Eduser.objects.get(
        username=request.session.get('username')).diary_set.all()
    img = str(Eduser.objects.get(
        username=request.session.get('username')).profile_img)
    img = "http://127.0.0.1:8000/media/" + img + "/"
    # expressions = Eduser.Diary_set.all()
    datas = expressions.order_by('-register_date')

    p = Paginator(datas, 5)

    info = p.get_page(now_page)

    start_page = (now_page - 1) // 10 * 10 + 1
    end_page = start_page + 9
    if end_page > p.num_pages:
        end_page = p.num_pages
        end_page = p.num_pages

    return render(request, 'mypage/mydiary.html', {'user': user, 'img': img, 'info': info, 'page_range': range(start_page, end_page + 1)})