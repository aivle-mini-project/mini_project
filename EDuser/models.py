from django.db import models

# Create your models here.

import os
def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.id, ext)
    return os.path.join('profile', filename)


class Eduser(models.Model):
    username = models.CharField(max_length=20, verbose_name="아이디")
    password = models.CharField(max_length=100, verbose_name="비밀번호")
    email = models.EmailField(verbose_name="이메일", null=True)
    profile_img = models.ImageField(null=True, upload_to=content_file_name, blank=True)
    register_date = models.DateTimeField(auto_now_add=True, verbose_name="등록날짜")

    def __str__(self):
        return self.username

    class Meta:
        db_table = "Emotics_user"
        verbose_name = "사용자"
        verbose_name_plural = "사용자"
