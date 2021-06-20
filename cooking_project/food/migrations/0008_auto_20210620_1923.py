# Generated by Django 3.2.4 on 2021-06-20 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0007_food_needs_garnish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='image',
            field=models.ImageField(upload_to='static/images', verbose_name='food image'),
        ),
        migrations.AlterField(
            model_name='food',
            name='needs_garnish',
            field=models.BooleanField(default=False),
        ),
    ]
