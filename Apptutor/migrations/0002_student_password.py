# Generated by Django 4.2.3 on 2023-08-23 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Apptutor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Password',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
