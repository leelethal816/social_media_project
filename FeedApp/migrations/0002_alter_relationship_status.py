# Generated by Django 3.2 on 2023-04-28 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FeedApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relationship',
            name='status',
            field=models.CharField(choices=[('sent', 'sent'), ('accepted', 'accepted')], default='send', max_length=8),
        ),
    ]
