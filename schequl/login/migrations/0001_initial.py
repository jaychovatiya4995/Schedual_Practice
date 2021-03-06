# Generated by Django 3.2.9 on 2021-11-19 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fnm', models.CharField(max_length=20)),
                ('lnm', models.CharField(max_length=20)),
                ('birth', models.CharField(max_length=10)),
                ('gen', models.CharField(max_length=10)),
                ('marital', models.CharField(max_length=10)),
                ('mobile', models.IntegerField()),
                ('email', models.CharField(max_length=120)),
                ('address', models.CharField(max_length=120)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
