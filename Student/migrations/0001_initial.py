# Generated by Django 4.0 on 2024-03-01 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentname', models.CharField(max_length=100)),
                ('studentemail', models.EmailField(max_length=254)),
                ('studentvillage', models.CharField(max_length=100)),
                ('studentpassword', models.CharField(max_length=100)),
                ('studentbranch', models.CharField(max_length=100)),
                ('studentphno', models.ImageField(upload_to='')),
            ],
        ),
    ]
