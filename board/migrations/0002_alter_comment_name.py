# Generated by Django 3.2.4 on 2021-06-14 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(default='名無し', max_length=20, verbose_name='投稿者名'),
        ),
    ]
