# Generated by Django 4.1.4 on 2023-01-02 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_integrator', '0005_alter_card_name_alter_credential_key_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='datasource',
            name='last_response',
            field=models.JSONField(blank=True, null=True),
        ),
    ]