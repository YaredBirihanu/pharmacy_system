# Generated by Django 5.0.2 on 2024-04-29 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0007_alter_pharmacyclerk_admin_alter_pharmacyclerk_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='age',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
