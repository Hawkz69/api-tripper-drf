# Generated by Django 2.2.3 on 2019-07-04 03:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
        ('attractions', '0003_auto_20190704_0259'),
    ]

    operations = [
        migrations.AddField(
            model_name='attractions',
            name='location',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='location.Location'),
            preserve_default=False,
        ),
    ]
