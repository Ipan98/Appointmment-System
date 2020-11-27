# Generated by Django 3.1.1 on 2020-11-19 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0004_remove_visitor_hour'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='hour',
            field=models.CharField(choices=[('10AM', '10:00AM'), ('11AM', '11:00AM'), ('1PM', '1:00PM'), ('2PM', '2:00PM'), ('3PM', '3:00PM'), ('4PM', '4:00PM')], default='10AM', max_length=5),
        ),
    ]
