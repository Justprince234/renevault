# Generated by Django 4.1.2 on 2022-11-23 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_updateuser_confirm_transaction_pin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updateuser',
            name='confirm_transaction_pin',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='updateuser',
            name='transaction_pin',
            field=models.IntegerField(),
        ),
    ]
