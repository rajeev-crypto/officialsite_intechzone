# Generated by Django 2.2.13 on 2021-05-12 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_career'),
    ]

    operations = [
        migrations.AlterField(
            model_name='career',
            name='message',
            field=models.TextField(help_text='Why you?'),
        ),
    ]