# Generated by Django 3.0.4 on 2020-03-25 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bizzfuzz', '0003_auto_20200325_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(help_text='Maximum 20 characters', max_length=160, unique=True),
        ),
    ]
