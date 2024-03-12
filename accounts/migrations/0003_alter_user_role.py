# Generated by Django 5.0.1 on 2024-03-12 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_userprofile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="role",
            field=models.PositiveSmallIntegerField(
                blank=True, choices=[(1, "RESTAURANT"), (2, "CUSTOMER")], null=True
            ),
        ),
    ]
