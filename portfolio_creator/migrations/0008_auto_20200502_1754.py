# Generated by Django 2.0.5 on 2020-05-02 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_creator', '0007_auto_20200502_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(upload_to='portfolio_creator/images/'),
        ),
    ]