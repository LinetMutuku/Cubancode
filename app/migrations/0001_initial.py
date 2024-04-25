# Generated by Django 5.0.2 on 2024-03-31 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('dob', models.DateField(null=True)),
                ('phone_number', models.IntegerField()),
                ('number_of_guests', models.IntegerField()),
            ],
        ),
    ]
