# Generated by Django 2.0 on 2018-10-18 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codefundo', '0008_auto_20181017_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='gov_fund',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fund', models.IntegerField(max_length=1000000)),
            ],
        ),
    ]
