# Generated by Django 4.2.8 on 2023-12-18 18:16

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0004_user_created_at"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="verificada",
            new_name="is_checked",
        ),
    ]
