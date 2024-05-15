# Generated by Django 5.0.6 on 2024-05-15 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Criteria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parameter', models.CharField(max_length=100)),
                ('operator', models.CharField(choices=[('<', '<'), ('>', '>'), ('<=', '<='), ('>=', '>='), ('==', '==')], max_length=2)),
                ('threshold', models.FloatField()),
                ('frequency', models.CharField(choices=[('day', 'Day'), ('month', 'Month'), ('year', 'Year')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='WeatherData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parameter', models.CharField(max_length=100)),
                ('value', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]