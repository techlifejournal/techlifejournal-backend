# Generated by Django 3.2.7 on 2021-12-14 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210921_2134'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='Tags',
            new_name='tags',
        ),
    ]
