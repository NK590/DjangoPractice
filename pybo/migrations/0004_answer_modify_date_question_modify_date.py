# Generated by Django 4.0.2 on 2022-02-05 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0003_answer_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
