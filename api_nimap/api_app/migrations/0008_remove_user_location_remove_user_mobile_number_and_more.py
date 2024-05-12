# Generated by Django 5.0 on 2024-05-12 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0007_alter_user_options_alter_user_managers_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='location',
        ),
        migrations.RemoveField(
            model_name='user',
            name='mobile_number',
        ),
        migrations.RemoveField(
            model_name='user',
            name='organization',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
    ]