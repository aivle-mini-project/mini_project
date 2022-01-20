# Generated by Django 4.0.1 on 2022-01-19 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eduser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=12, verbose_name='아이디')),
                ('password', models.CharField(max_length=100, verbose_name='비밀번호')),
                ('email', models.EmailField(max_length=254, verbose_name='이메일')),
                ('profile_img', models.ImageField(null=True, upload_to='')),
                ('register_date', models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')),
            ],
            options={
                'verbose_name': '사용자',
                'verbose_name_plural': '사용자',
                'db_table': 'Emotics_user',
            },
        ),
    ]
