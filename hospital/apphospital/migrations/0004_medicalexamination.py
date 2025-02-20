# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-08-17 11:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apphospital', '0003_department_patient_people_worker'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalExamination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('examination_date', models.DateTimeField(verbose_name='exam date')),
                ('examination_result', models.CharField(choices=[('Healty', 'Healty'), ('CORONA', 'CORONA'), ('BOTISM', 'BOTISM'), ('DEAD', 'DEAD')], default='Healty', max_length=20)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apphospital.Patient')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apphospital.Worker')),
            ],
        ),
    ]
