# Generated by Django 2.2.10 on 2020-03-17 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0003_auto_20200317_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commody',
            name='floorNum',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='主楼数'),
        ),
        migrations.AlterField(
            model_name='commody',
            name='replyNum',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='留言数'),
        ),
    ]