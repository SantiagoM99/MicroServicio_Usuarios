# Generated by Django 3.2.6 on 2023-03-17 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especialidad', models.TextField(max_length=50)),
                ('consultorio', models.TextField(max_length=50)),
            ],
        ),
    ]
