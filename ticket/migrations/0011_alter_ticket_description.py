# Generated by Django 4.0.1 on 2022-01-25 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0010_alter_ticket_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='description',
            field=models.TextField(),
        ),
    ]