# Generated by Django 3.1.4 on 2020-12-19 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_auto_20201219_1436'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservationlineitem',
            name='original_reservation',
        ),
        migrations.RemoveField(
            model_name='reservationlineitem',
            name='stripe_pid',
        ),
        migrations.AddField(
            model_name='reservation',
            name='original_reservation',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='reservation',
            name='stripe_pid',
            field=models.CharField(blank=True, default='', max_length=254, null=True),
        ),
    ]