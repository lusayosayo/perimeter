# Generated by Django 2.2.7 on 2020-04-06 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infrastructure_monitoring_api', '0007_nodeinterfaceavailabilitycache_node_availability_cache'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='networkavailabilitycache',
            name='number_of_nodes_offline',
        ),
        migrations.RemoveField(
            model_name='networkavailabilitycache',
            name='number_of_nodes_online',
        ),
        migrations.RemoveField(
            model_name='networkavailabilitycache',
            name='total_number_of_nodes',
        ),
    ]
