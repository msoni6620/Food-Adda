# Generated by Django 5.0.5 on 2024-08-28 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='hobbies',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
