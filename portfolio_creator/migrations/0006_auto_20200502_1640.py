# Generated by Django 2.0.5 on 2020-05-02 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_creator', '0005_user_languages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
