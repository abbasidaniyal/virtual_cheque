# Generated by Django 2.2.1 on 2019-05-24 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cheque_generator', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cheque',
            name='issuer',
        ),
        migrations.AddField(
            model_name='cheque',
            name='bearer',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
