# Generated by Django 4.2.4 on 2024-09-02 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arcticApp', '0013_alertimage_shoeservice'),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthHeaderImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='header_images/')),
                ('alt_text', models.CharField(default='header', max_length=100)),
            ],
        ),
    ]
