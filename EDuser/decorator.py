from django.shortcuts import redirect
from EDuser.models import Eduser
def login_required(function):
  def wrap(request, *args, **kwargs):
    user = request.session.get('username')
    if user is None or not user:
      return redirect('/login')
    return function(request, *args, **kwargs)
  return wrap

