# Generated by Django 4.1.2 on 2023-01-17 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_alter_productmodel_pltem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='pprice',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='pquantity',
            field=models.IntegerField(),
        ),
    ]
