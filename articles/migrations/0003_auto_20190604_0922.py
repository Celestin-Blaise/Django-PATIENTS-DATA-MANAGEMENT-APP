# Generated by Django 2.2.1 on 2019-06-04 06:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20190604_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date created'),
        ),
    ]
