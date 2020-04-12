# Generated by Django 3.0.5 on 2020-04-11 22:28

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('candidate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='name')),
                ('url', models.CharField(blank=True, max_length=256, null=True, verbose_name='url')),
                ('mail', models.EmailField(blank=True, max_length=256, null=True, verbose_name='email')),
                ('more_info', models.TextField(blank=True, null=True, verbose_name='info')),
            ],
        ),
        migrations.CreateModel(
            name='OpportunityExpertise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seniority', models.CharField(choices=[('JR', 'Junior'), ('SSR', 'Semisenior'), ('SR', 'Senior'), ('NJ', 'Ninja')], default='JR', max_length=3)),
                ('experience_years', models.PositiveIntegerField(blank=True, null=True)),
                ('opportunity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opportunity.Client', verbose_name='opportunity')),
                ('technology', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidate.Technology', verbose_name='technology')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Opportunity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode', models.CharField(choices=[('FP', 'Fixed-price'), ('SA', 'Staff-augmentation'), ('ND', 'Not-defined')], default='ND', max_length=2)),
                ('candidates_qty', models.PositiveIntegerField(blank=True, null=True)),
                ('mandatory_english', models.BooleanField(default=False)),
                ('more_info', models.TextField(blank=True, null=True, verbose_name='info')),
                ('rate', models.CharField(max_length=256, verbose_name='rate')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='date')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='opportunity.Client', verbose_name='client')),
            ],
        ),
    ]
