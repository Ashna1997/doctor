# Generated by Django 3.0.3 on 2020-02-24 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_doctor1_patient1_specialization1'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='specialization1',
            new_name='sp1',
        ),
        migrations.DeleteModel(
            name='doctor',
        ),
        migrations.DeleteModel(
            name='patient',
        ),
        migrations.DeleteModel(
            name='specialization',
        ),
        migrations.RenameField(
            model_name='sp1',
            old_name='categoryid',
            new_name='category_id',
        ),
    ]
