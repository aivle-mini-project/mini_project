from django.shortcuts import render
from django.core.paginator import Paginator
from EDuser.models import Eduser

def likepage(request):
    now_page =int(request.GET.get('page', 1))
    print(now_page)
    user=(request.session['username'])
    expressions = Eduser.objects.get(username=request.session.get('username')).expression_set.all()
    datas = expressions.order_by('-id')
    
    p = Paginator(datas, 5)
    
    info = p.get_page(now_page)
    
    start_page = (now_page - 1) // 10 * 10 + 1
    end_page = start_page + 9
    if end_page > p.num_pages:
        end_page = p.num_pages
    
    return render(request, 'mypage/likepage.html',{'user':user,'info' : info,'page_range' : range(start_page, end_page + 1)})

def mypage(request):
    now_page =int(request.GET.get('page', 1))
    print(now_page)
    user=(request.session['username'])
    expressions = Eduser.objects.get(username=request.session.get('username')).diary_set.all()
    # expressions = Eduser.Diary_set.all()
    datas = expressions.order_by('-register_date')
    
    p = Paginator(datas, 5)
    
    info = p.get_page(now_page)
    
    start_page = (now_page - 1) // 10 * 10 + 1
    end_page = start_page + 9
    if end_page > p.num_pages:
        end_page = p.num_pages
    
    return render(request, 'mypage/mypage.html',{'user':user,'info' : info,'page_range' : range(start_page, end_page + 1)})