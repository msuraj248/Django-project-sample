# Generated by Django 3.1 on 2020-08-07 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_id', models.CharField(max_length=20)),
                ('e_name', models.CharField(max_length=50)),
                ('e_mail', models.EmailField(max_length=254)),
                ('e_contact', models.CharField(max_length=20)),
            ],
        ),
    ]
