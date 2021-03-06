# Generated by Django 4.0.1 on 2022-01-25 02:12

import diary.validation
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0003_expression'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='write',
            field=models.TextField(max_length=100, validators=[diary.validation.validate_sentence], verbose_name='일기'),
        ),
        migrations.AlterField(
            model_name='diarydetail',
            name='diary',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diary.diary', verbose_name='writer'),
        ),
        migrations.AlterField(
            model_name='diarydetailhighlight',
            name='diary_detail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diary.diarydetail', verbose_name='writer'),
        ),
    ]
