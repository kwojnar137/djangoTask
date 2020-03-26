# Generated by Django 3.0.4 on 2020-03-25 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bizzfuzz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='birth_date',
            field=models.DateField(blank=True, help_text='Required. Format: YYYY-MM-DD', null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='random_number',
            field=models.DecimalField(decimal_places=0, default=-1, max_digits=3),
        ),
    ]