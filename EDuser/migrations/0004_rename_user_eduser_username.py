# Generated by Django 4.0.1 on 2022-01-20 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EDuser', '0003_rename_username_eduser_user_alter_eduser_profile_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eduser',
            old_name='user',
            new_name='username',
        ),
    ]
