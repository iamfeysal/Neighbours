# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-21 19:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=30, null=True)),
                ('email_address', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=600)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Neighbourhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, null=True)),
                ('location', models.CharField(choices=[('Nairobi', 'Nairobi'), ('Machakos', 'Machakos'), ('KItui', 'KItui'), ('Garissa', 'Garissa'), ('Mombasa', 'Mombasa'), ('Malindi', 'Malindi'), ('Kisumu', 'Kisumu'), ('Migori', 'Migori'), ('Kakamega', 'Kakamega'), ('Uasingishu', 'Uasingishu')], max_length=100)),
                ('population', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NewsLetterRecipients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profilePic', models.ImageField(blank=True, null=True, upload_to='profile/')),
                ('contact', tinymce.models.HTMLField(max_length=60, null=True)),
                ('bio', models.CharField(blank=True, max_length=60)),
                ('email', models.TextField(blank=True, default=0, max_length=200, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('body', models.TextField()),
                ('neighbourhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Neighbourhood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='business',
            name='neighbourhood',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='neighbourhoodbusiness', to='app.Neighbourhood'),
        ),
        migrations.AddField(
            model_name='business',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='business', to=settings.AUTH_USER_MODEL),
        ),
    ]
