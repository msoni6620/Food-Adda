# Generated by Django 5.0.5 on 2024-08-29 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_student_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=500)),
                ('speed', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='product',
        ),
    ]
