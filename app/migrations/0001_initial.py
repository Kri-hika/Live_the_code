# Generated by Django 3.2.8 on 2021-10-09 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_key', models.CharField(max_length=200)),
                ('identifier', models.CharField(choices=[('email', 'Email'), ('phone_number_sms', 'Phone')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Customized_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=30)),
                ('logo', models.ImageField(upload_to='pics')),
                ('bg_img', models.ImageField(upload_to='pics')),
                ('url', models.URLField(max_length=231)),
                ('c_url', models.URLField(max_length=231)),
                ('desc', models.CharField(default='some_value', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
