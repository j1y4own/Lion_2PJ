# Generated by Django 4.1.1 on 2022-10-02 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashbookapp', '0020_alter_cashbook_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='cashbook',
            name='image',
            field=models.ImageField(blank=True, upload_to='image/'),
        ),
    ]
