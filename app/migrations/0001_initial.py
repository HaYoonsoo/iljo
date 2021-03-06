# Generated by Django 4.0.4 on 2022-05-28 08:50

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pig_name', models.CharField(max_length=20)),
                ('pig_description', models.TextField()),
                ('exchange_rate', models.FloatField(validators=[django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('where_to_meet', models.TextField()),
                ('when_to_meet', models.DateTimeField()),
                ('schedule_name', models.CharField(max_length=20)),
                ('schedule_description', models.TextField()),
                ('pig_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pig_info', to='app.pig')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=30)),
                ('account', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Participants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_late', models.IntegerField()),
                ('participant_profile', models.ManyToManyField(related_name='participants', to='app.profile')),
            ],
        ),
    ]
