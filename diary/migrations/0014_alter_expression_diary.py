# Generated by Django 4.0.1 on 2022-01-28 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0013_merge_20220128_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expression',
            name='diary',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expressions', to='diary.diary'),
        ),
    ]
