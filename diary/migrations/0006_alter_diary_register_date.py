# Generated by Django 4.0.1 on 2022-01-26 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0005_alter_expression_diary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='register_date',
            field=models.DateTimeField(unique=True, verbose_name='등록날짜'),
        ),
    ]