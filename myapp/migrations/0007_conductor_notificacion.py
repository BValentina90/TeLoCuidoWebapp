# Generated by Django 3.0.5 on 2020-04-16 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20200416_0131'),
    ]

    operations = [
        migrations.AddField(
            model_name='conductor',
            name='notificacion',
            field=models.IntegerField(default=0),
        ),
    ]
