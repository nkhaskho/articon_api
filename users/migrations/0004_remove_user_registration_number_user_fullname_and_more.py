# Generated by Django 4.2.7 on 2024-05-05 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_region'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='registration_number',
        ),
        migrations.AddField(
            model_name='user',
            name='fullname',
            field=models.CharField(db_index=True, default='CE01XXXXXX', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='registration',
            field=models.TextField(null=True, unique=True),
        ),
    ]
