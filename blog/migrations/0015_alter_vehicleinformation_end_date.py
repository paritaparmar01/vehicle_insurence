# Generated by Django 5.0.1 on 2024-02-20 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_alter_vehicleinformation_previous_policy_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicleinformation',
            name='end_date',
            field=models.DateField(null=True),
        ),
    ]
