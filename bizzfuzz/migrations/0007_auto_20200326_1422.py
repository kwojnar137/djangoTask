# Generated by Django 3.0.4 on 2020-03-26 13:22

import bizzfuzz.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bizzfuzz', '0006_auto_20200326_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='birth_date',
            field=models.DateField(help_text='Required. Format: YYYY-MM-DD', validators=[bizzfuzz.validators.date_max]),
        ),
    ]
