# Generated by Django 2.1.5 on 2019-06-24 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Food', '0003_auto_20190624_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodstore',
            name='code',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
