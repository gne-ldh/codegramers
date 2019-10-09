# Generated by Django 2.1.1 on 2018-09-01 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.CharField(default=' ', max_length=15, primary_key=True, serialize=False)),
                ('name', models.CharField(default=' ', max_length=50)),
                ('code_name', models.CharField(default=' ', max_length=5)),
                ('stream', models.CharField(default=' ', max_length=20)),
                ('mentees1', models.CharField(default='0-0', max_length=7)),
                ('mentees2', models.CharField(default='0-0', max_length=7)),
                ('mentees3', models.CharField(default='0-0', max_length=7)),
                ('mentees4', models.CharField(default='0-0', max_length=7)),
                ('is_registered', models.BooleanField(default=False)),
                ('is_varified', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=70)),
                ('is_hod', models.BooleanField(default=False)),
            ],
        ),
    ]
