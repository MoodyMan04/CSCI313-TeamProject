# Generated by Django 5.0.3 on 2024-05-02 02:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_cartitem_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='checkout.member'),
        ),
    ]