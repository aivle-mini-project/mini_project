# Generated by Django 4.0.1 on 2022-01-25 03:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0004_alter_diary_write_alter_diarydetail_diary_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expression',
            name='diary',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expressions', to='diary.diary'),
        ),
    ]
