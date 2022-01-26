# Generated by Django 4.0.1 on 2022-01-26 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calemotion',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('emo_date', models.DateField()),
                ('emotion', models.CharField(max_length=30)),
                ('emoji', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'calemotion',
                'managed': False,
            },
        ),
    ]
