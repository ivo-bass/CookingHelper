# Generated by Django 3.2.4 on 2021-06-20 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0009_alter_food_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images', verbose_name='food image'),
        ),
    ]
