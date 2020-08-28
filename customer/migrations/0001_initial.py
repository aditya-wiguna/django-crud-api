# Generated by Django 3.0.7 on 2020-08-27 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('marital_status', models.CharField(default='', max_length=50)),
                ('identity_number', models.CharField(default='', max_length=100)),
                ('address', models.CharField(default='', max_length=191)),
                ('parent_name', models.CharField(default='', max_length=191)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
    ]
