# Generated by Django 3.2.4 on 2021-06-14 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_auto_20210614_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='作成日時'),
        ),
    ]
