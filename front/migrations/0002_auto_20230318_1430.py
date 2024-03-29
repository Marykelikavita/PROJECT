# Generated by Django 3.2.9 on 2023-03-18 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='age',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='bloodpressure',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='bmi',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='diabetespedigreefunction',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='glucose',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='insulin',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='pregnancies',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='skinthickness',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
