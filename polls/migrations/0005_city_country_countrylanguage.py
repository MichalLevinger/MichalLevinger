# Generated by Django 3.2.7 on 2021-10-05 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_permission_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=35)),
                ('district', models.CharField(db_column='District', max_length=20)),
                ('population', models.IntegerField(db_column='Population')),
            ],
            options={
                'db_table': 'city',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('code', models.CharField(db_column='Code', max_length=3, primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=52)),
                ('continent', models.CharField(db_column='Continent', max_length=13)),
                ('region', models.CharField(db_column='Region', max_length=26)),
                ('surfacearea', models.FloatField(db_column='SurfaceArea')),
                ('indepyear', models.SmallIntegerField(blank=True, db_column='IndepYear', null=True)),
                ('population', models.IntegerField(db_column='Population')),
                ('lifeexpectancy', models.FloatField(blank=True, db_column='LifeExpectancy', null=True)),
                ('gnp', models.FloatField(blank=True, db_column='GNP', null=True)),
                ('gnpold', models.FloatField(blank=True, db_column='GNPOld', null=True)),
                ('localname', models.CharField(db_column='LocalName', max_length=45)),
                ('governmentform', models.CharField(db_column='GovernmentForm', max_length=45)),
                ('headofstate', models.CharField(blank=True, db_column='HeadOfState', max_length=60, null=True)),
                ('capital', models.IntegerField(blank=True, db_column='Capital', null=True)),
                ('code2', models.CharField(db_column='Code2', max_length=2)),
            ],
            options={
                'db_table': 'country',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Countrylanguage',
            fields=[
                ('countrycode', models.OneToOneField(db_column='CountryCode', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='polls.country')),
                ('language', models.CharField(db_column='Language', max_length=30)),
                ('isofficial', models.CharField(db_column='IsOfficial', max_length=1)),
                ('percentage', models.FloatField(db_column='Percentage')),
            ],
            options={
                'db_table': 'countrylanguage',
                'managed': False,
            },
        ),
    ]
