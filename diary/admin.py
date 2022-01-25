from django.contrib import admin
from .models import Diary, DiaryDetail, DiaryDetailHighlight, Expression
# Register your models here.

admin.site.register(Diary)
admin.site.register(DiaryDetail)
admin.site.register(DiaryDetailHighlight)
admin.site.register(Expression)
