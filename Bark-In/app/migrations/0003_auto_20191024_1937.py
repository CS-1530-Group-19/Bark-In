# Generated by Django 2.2.6 on 2019-10-24 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20191024_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dogs',
            field=models.ManyToManyField(blank=True, to='app.Dog'),
        ),
    ]