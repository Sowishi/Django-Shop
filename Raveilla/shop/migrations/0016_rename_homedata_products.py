# Generated by Django 4.2 on 2024-05-02 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_delete_womendata'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HomeData',
            new_name='Products',
        ),
    ]
