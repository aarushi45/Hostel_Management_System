# Generated by Django 4.2 on 2023-04-28 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='Candidate_Attendance',
            field=models.IntegerField(default=1),
        ),
    ]