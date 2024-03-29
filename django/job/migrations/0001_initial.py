# Generated by Django 3.1.2 on 2020-10-11 16:45

import ckeditor.fields
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=240, verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=240, verbose_name='Job')),
                ('identified_at', models.DateTimeField(auto_now_add=True, verbose_name='Identified')),
                ('kind', models.CharField(choices=[('FULLTIME', 'Full-Time'), ('PARTTIME', 'Part-Time')], default='FULLTIME', max_length=8)),
                ('position', models.CharField(max_length=240, verbose_name='Position')),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=240), blank=True, size=None)),
                ('link', models.URLField(blank=True, null=True, verbose_name='Link')),
                ('content', ckeditor.fields.RichTextField()),
                ('restrict_country', django_countries.fields.CountryField(max_length=2)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='job.category', verbose_name='Category')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='company.company', verbose_name='Company')),
            ],
            options={
                'verbose_name': 'Job',
                'verbose_name_plural': 'Jobs',
            },
        ),
    ]
