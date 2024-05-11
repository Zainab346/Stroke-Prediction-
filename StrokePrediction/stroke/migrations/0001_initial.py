# Generated by Django 5.0.1 on 2024-01-17 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('marital_status', models.CharField(max_length=50)),
                ('work_type', models.CharField(max_length=50)),
                ('residence', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('bmi', models.FloatField()),
                ('gluc_level', models.FloatField()),
                ('smoke', models.CharField(max_length=50)),
                ('hypertension', models.CharField(max_length=50)),
                ('heart_disease', models.CharField(max_length=50)),
            ],
        ),
    ]
