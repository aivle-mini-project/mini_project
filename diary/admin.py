from django.contrib import admin
from .models import Diary, DiaryDetail, DiaryDetailHighlight
# Register your models here.

admin.site.register(Diary)
admin.site.register(DiaryDetail)
admin.site.register(DiaryDetailHighlight)