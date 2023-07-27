# Generated by Django 4.2.3 on 2023-07-25 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0009_alter_appointment_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='reference',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]