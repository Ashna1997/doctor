# Generated by Django 3.0.3 on 2020-02-24 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='doctor1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('special', models.CharField(max_length=50)),
                ('hospital', models.CharField(max_length=50)),
                ('salary', models.CharField(max_length=50)),
                ('photo', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'doctor1',
            },
        ),
        migrations.CreateModel(
            name='patient1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('doctor', models.CharField(max_length=50)),
                ('bill', models.CharField(max_length=50)),
                ('hospital', models.CharField(max_length=50)),
                ('photo', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'patient1',
            },
        ),
        migrations.CreateModel(
            name='specialization1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryid', models.CharField(max_length=50)),
                ('special', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'specialization1',
            },
        ),
    ]
