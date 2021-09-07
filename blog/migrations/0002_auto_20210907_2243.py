# Generated by Django 3.2.7 on 2021-09-07 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.TextField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='entry',
            name='mod_date',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='entry',
            name='pub_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='tags',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='blog.tags'),
            preserve_default=False,
        ),
    ]
