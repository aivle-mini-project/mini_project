from django.shortcuts import render

# Create your views here.

def boardView(request):
  return render(request, 'board/board.html')

def boardTestView(request):
  return render(request, 'board/board_test.html')