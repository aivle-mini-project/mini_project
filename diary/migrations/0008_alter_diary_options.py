# Generated by Django 4.0.1 on 2022-01-26 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0007_alter_diary_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='diary',
            options={'ordering': ['-id'], 'verbose_name': '일기', 'verbose_name_plural': '일기'},
        ),
    ]