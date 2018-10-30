# Generated by Django 2.0 on 2018-10-17 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codefundo', '0007_auto_20181016_1522'),
    ]

    operations = [
        migrations.CreateModel(
            name='track_users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pincode', models.IntegerField(max_length=100, unique=True)),
                ('user_count', models.IntegerField(max_length=100000)),
            ],
        ),
        migrations.RemoveField(
            model_name='user_details',
            name='author',
        ),
    ]
