# Generated by Django 2.1.5 on 2019-01-12 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject_and_marks', '0005_auto_20190111_0019'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjects',
            name='batch',
            field=models.CharField(default='', max_length=11),
        ),
    ]
