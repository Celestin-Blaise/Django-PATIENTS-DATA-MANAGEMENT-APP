# Generated by Django 2.2.1 on 2019-06-04 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20190604_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
