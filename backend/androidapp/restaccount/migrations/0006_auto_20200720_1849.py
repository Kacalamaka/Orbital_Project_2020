# Generated by Django 3.0.7 on 2020-07-20 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaccount', '0005_auto_20200717_1647'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='contact',
            unique_together={('current_user_id', 'contact')},
        ),
    ]
