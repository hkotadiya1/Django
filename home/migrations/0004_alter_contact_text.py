# Generated by Django 4.1.1 on 2022-09-22 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_contact_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='text',
            field=models.TextField(blank=True, default='', max_length=100, null=True),
        ),
    ]