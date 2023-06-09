# Generated by Django 4.1.9 on 2023-05-27 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("measure", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="soilmeasurement", name="coordinates",),
        migrations.RemoveField(model_name="soilmeasurement", name="npk_values",),
        migrations.AddField(
            model_name="soilmeasurement",
            name="drilled_status",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="soilmeasurement",
            name="location_x",
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name="soilmeasurement",
            name="location_y",
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name="soilmeasurement",
            name="nitrogen_reading",
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name="soilmeasurement",
            name="nitrogen_sensor",
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name="soilmeasurement",
            name="ph_current",
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name="soilmeasurement",
            name="phosphorous_reading",
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name="soilmeasurement",
            name="phosphorous_sensor",
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name="soilmeasurement",
            name="potassium_reading",
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name="soilmeasurement",
            name="potassium_sensor",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="soilmeasurement",
            name="ph_value",
            field=models.FloatField(default=0.0),
        ),
    ]
