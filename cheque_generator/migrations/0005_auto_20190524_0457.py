# Generated by Django 2.2.1 on 2019-05-24 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cheque_generator', '0004_auto_20190524_0455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cheque',
            name='issue_date',
            field=models.DateField(),
        ),
    ]