# Generated by Django 2.2.7 on 2019-11-19 22:43

import app.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Un-named', max_length=150)),
                ('dog_pfp', models.FileField(blank=True, null=True, upload_to=app.models.get_image_path)),
                ('breed', models.CharField(max_length=150, null=True)),
                ('dog_size', models.CharField(max_length=140, null=True)),
                ('temperament', models.PositiveIntegerField(blank=True, default=5)),
                ('activity_level', models.PositiveIntegerField(blank=True, default=5)),
                ('volume', models.PositiveIntegerField(blank=True, default=5)),
                ('notes', models.CharField(max_length=512, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=512, null=True)),
                ('dogs', models.ManyToManyField(blank=True, to='app.Dog')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('t_start', models.DurationField()),
                ('t_end', models.DurationField()),
                ('dog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Dog')),
            ],
        ),
        migrations.CreateModel(
            name='ParkReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(blank=True, max_length=1024, null=True)),
                ('star_rating', models.PositiveIntegerField(blank=True, default=0)),
                ('timeposted', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Park',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, null=True)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('info', models.CharField(max_length=512, null=True)),
                ('address', models.CharField(max_length=512, null=True)),
                ('fenced_in', models.BooleanField(default=False)),
                ('off_leash', models.BooleanField(default=False)),
                ('reviews', models.ManyToManyField(blank=True, to='app.ParkReview')),
                ('schedules', models.ManyToManyField(blank=True, to='app.Schedule')),
            ],
        ),
    ]
