from django.shortcuts import render

# Create your views here.

def showIndex(request):
  if "username" in request.session:
    return render(request, 'base/home.html', {'username': request.session['username']})
  return render(request, 'base/home.html')