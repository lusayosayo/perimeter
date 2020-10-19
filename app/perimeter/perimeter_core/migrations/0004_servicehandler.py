# Generated by Django 2.2.7 on 2020-02-22 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perimeter_core', '0003_auto_20200222_1601'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceHandler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('app_name', models.CharField(max_length=100)),
                ('on_created', models.DateField(auto_now_add=True)),
                ('on_updated', models.DateField(auto_now=True)),
            ],
        ),
    ]