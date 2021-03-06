# Generated by Django 3.0.5 on 2020-04-12 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cooperative', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='name')),
                ('english_level', models.CharField(choices=[('JR', 'Junior'), ('AD', 'Advanced'), ('NT', 'Native')], default='JR', max_length=2)),
                ('availability', models.CharField(choices=[('BS', 'Busy'), ('FR', 'Free'), ('CBF', 'Could be free')], default='FR', max_length=3)),
                ('cooperative', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cooperative.Cooperative', verbose_name='cooperative')),
            ],
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='CandidateExpertise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seniority', models.CharField(choices=[('JR', 'Junior'), ('SSR', 'Semisenior'), ('SR', 'Senior'), ('NJ', 'Ninja')], default='JR', max_length=3)),
                ('experience_years', models.PositiveIntegerField(blank=True, null=True)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidate.Candidate', verbose_name='candidate')),
                ('technology', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidate.Technology', verbose_name='technology')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
