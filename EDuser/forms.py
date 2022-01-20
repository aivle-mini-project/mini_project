from django.forms import CharField, forms
from .models import Eduser
from django.contrib.auth.hashers import check_password, make_password


class RegisterForm(forms.Form):
  user_id = CharField(
    error_messages= {
      'required': '아이디를 입력해주세요.'
    },
    max_length=20, label='아이디'
  )
  email = forms.EmailField(
      error_messages={
          'required': '이메일을 입력해주세요.'
      },
      max_length=64, label='이메일'
  )
  password = forms.CharField(
      error_messages={
          'required': '비밀번호를 입력해주세요.'
      },
      widget=forms.PasswordInput, label='비밀번호'
  )
  re_password = forms.CharField(
      error_messages={
          'required': '비밀번호를 입력해주세요.'
      },
      widget=forms.PasswordInput, label='비밀번호 확인'
  )
  profile_img = forms.ImageField( required=False)



  def clean(self):
      cleaned_data = super().clean()
      email = cleaned_data.get('email')
      password = cleaned_data.get('password')
      re_password = cleaned_data.get('re_password')

      if email and password and re_password:
          if Eduser.objects.filter(email=email).exists():
              self.add_error('email', '해당 이메일로 이미 가입하였습니다.')
          else:    
              if password != re_password:
                  self.add_error('re_password', '비밀번호가 서로 다릅니다.')



class LoginForm(forms.Form):
  user_id = forms.EmailField(
      error_messages={
          'required': '이메일을 입력해주세요.'
      },
      max_length=64, label='이메일'
  )
  password = forms.CharField(
      error_messages={
          'required': '비밀번호를 입력해주세요.'
      },
      widget=forms.PasswordInput, label='비밀번호'
  )


  def clean(self):
      cleaned_data = super().clean()
      email = cleaned_data.get('email')
      password = cleaned_data.get('password')

      if email and password:
          try:
              fcuser = Eduser.objects.get(email=email)
          except Eduser.DoesNotExist:
              self.add_error('email', '아이디가 없습니다.')
              return
          if not check_password(password, fcuser.password):
              self.add_error('password', '비밀번호를 틀렸습니다.') # 특정 필드에 에러를 넣는 함수

