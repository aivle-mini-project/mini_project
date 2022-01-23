# Generated by Django 4.0.1 on 2022-01-23 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('EDuser', '0005_alter_eduser_profile_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('write', models.TextField(verbose_name='일기')),
                ('emotion', models.IntegerField(verbose_name='감정')),
                ('register_date', models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')),
                ('writer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='EDuser.eduser')),
            ],
            options={
                'verbose_name': '일기',
                'verbose_name_plural': '일기',
                'db_table': 'diary',
            },
        ),
    ]
