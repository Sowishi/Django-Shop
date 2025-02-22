# Generated by Django 4.2 on 2024-05-06 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_rename_homedata_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='WomenProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('price', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to='images/')),
            ],
        ),
    ]
