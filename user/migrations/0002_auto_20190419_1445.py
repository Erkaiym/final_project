# Generated by Django 2.1.5 on 2019-04-19 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='sex',
            field=models.CharField(choices=[('M', 'Мужчина'), ('W', 'Женщина')], default=None, max_length=1),
        ),
    ]
