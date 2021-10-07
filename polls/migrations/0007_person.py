# Generated by Django 3.2.7 on 2021-10-06 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_alter_address_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='polls.address')),
                ('permission', models.ManyToManyField(blank=True, null=True, to='polls.Permission')),
            ],
        ),
    ]
