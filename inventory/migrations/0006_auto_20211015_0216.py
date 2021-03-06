# Generated by Django 3.1.6 on 2021-10-15 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_auto_20211014_0228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryitem',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_query_name='categories', to='inventory.categories', to_field='category'),
        ),
    ]
