# Generated by Django 4.2.7 on 2024-06-06 22:23

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_registration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='registration',
            field=models.TextField(blank=True, validators=[users.models.validate]),
        ),
    ]
