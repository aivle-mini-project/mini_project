# Generated by Django 4.0.1 on 2022-01-27 17:38

import diary.validation
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('EDuser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('write', models.TextField(max_length=100, validators=[diary.validation.validate_sentence], verbose_name='일기')),
                ('emotion', models.CharField(max_length=30, verbose_name='감정')),
                ('neutral', models.FloatField(verbose_name='평온')),
                ('positive', models.FloatField(verbose_name='긍정')),
                ('negative', models.FloatField(verbose_name='부정')),
                ('register_date', models.DateTimeField(unique=True, verbose_name='등록날짜')),
                ('writer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='EDuser.eduser')),
            ],
            options={
                'verbose_name': '일기',
                'verbose_name_plural': '일기',
                'db_table': 'diary',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='DiaryDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('write', models.TextField(verbose_name='일기')),
                ('emotion', models.CharField(max_length=30, verbose_name='감정')),
                ('neutral', models.FloatField(verbose_name='평온')),
                ('positive', models.FloatField(verbose_name='긍정')),
                ('negative', models.FloatField(verbose_name='부정')),
                ('diary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diary.diary', verbose_name='writer')),
            ],
            options={
                'verbose_name': '일기상세',
                'verbose_name_plural': '일기상세',
                'db_table': 'diary_detail',
            },
        ),
        migrations.CreateModel(
            name='Expression',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expressions', to='diary.diary')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EDuser.eduser')),
            ],
            options={
                'verbose_name': '좋아요',
                'verbose_name_plural': '좋아요',
                'db_table': 'expression',
            },
        ),
        migrations.CreateModel(
            name='DiaryDetailHighlight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offset', models.IntegerField(verbose_name='시작점')),
                ('length', models.IntegerField(verbose_name='길이')),
                ('diary_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diary.diarydetail', verbose_name='writer')),
            ],
            options={
                'verbose_name': '일기상세효과',
                'verbose_name_plural': '일기상세효과',
                'db_table': 'diary_detail_highlight',
            },
        ),
    ]
