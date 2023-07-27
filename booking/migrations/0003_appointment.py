# Generated by Django 4.2.3 on 2023-07-20 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_rename_price_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('chosen_time', models.DateTimeField(auto_now_add=True)),
                ('dpt', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='booking.department')),
            ],
        ),
    ]