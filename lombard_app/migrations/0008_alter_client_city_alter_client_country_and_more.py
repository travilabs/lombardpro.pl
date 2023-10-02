# Generated by Django 4.2.5 on 2023-10-02 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lombard_app', '0007_client_user_loan_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='city',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='client',
            name='country',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='client',
            name='first_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='client',
            name='id_card',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='client',
            name='last_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='client',
            name='notes',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='client',
            name='street',
            field=models.CharField(max_length=255),
        ),
    ]