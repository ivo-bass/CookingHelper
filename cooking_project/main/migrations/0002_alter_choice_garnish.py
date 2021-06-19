# Generated by Django 3.2.4 on 2021-06-19 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0006_remove_food_garnish'),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='garnish',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='food.garnish'),
        ),
    ]