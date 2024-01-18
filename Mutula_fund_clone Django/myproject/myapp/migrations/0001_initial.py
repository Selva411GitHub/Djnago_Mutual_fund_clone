# Generated by Django 5.0.1 on 2024-01-14 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('fund_house', models.CharField(max_length=255)),
                ('fund_number', models.CharField(max_length=10)),
                ('unit_held', models.FloatField()),
                ('invested', models.FloatField()),
                ('currentvalue', models.FloatField(default=0.0)),
                ('nav', models.FloatField()),
                ('growth', models.FloatField()),
            ],
        ),
    ]
