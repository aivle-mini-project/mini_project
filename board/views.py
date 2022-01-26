from django.shortcuts import render
from EDuser.models import Eduser

# Create your views here.

def boardView(request):
  try :
    user = Eduser.objects.get(username = request.session['username'])
    liked = user.expression_set.all()
    context = {'username': request.session['username'], 'liked':liked, 'user': user}
    return render(request, 'board/board.html', context)
  except:
    return render(request, 'board/board.html')

