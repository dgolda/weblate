# Generated by Django 1.11.16 on 2018-11-01 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("billing", "0008_auto_20181024_1151")]

    operations = [
        migrations.AlterField(
            model_name="billing",
            name="state",
            field=models.IntegerField(
                choices=[(0, "Active"), (1, "Trial"), (2, "Expired")],
                default=0,
                verbose_name="Billing state",
            ),
        )
    ]