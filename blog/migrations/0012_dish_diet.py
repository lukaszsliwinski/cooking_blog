# Generated by Django 3.1.7 on 2021-05-12 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20210508_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='diet',
            field=models.BooleanField(default=True),
        ),
    ]
