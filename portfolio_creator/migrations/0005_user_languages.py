# Generated by Django 2.0.5 on 2020-05-01 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_creator', '0004_auto_20200501_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='languages',
            field=models.CharField(default='a', max_length=200),
            preserve_default=False,
        ),
    ]
