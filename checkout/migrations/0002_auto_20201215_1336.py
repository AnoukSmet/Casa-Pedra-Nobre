# Generated by Django 3.1.4 on 2020-12-15 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='eta',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
