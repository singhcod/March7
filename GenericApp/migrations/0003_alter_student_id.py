# Generated by Django 3.2.12 on 2022-03-09 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GenericApp', '0002_auto_20220308_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
