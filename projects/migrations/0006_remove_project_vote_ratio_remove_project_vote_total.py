# Generated by Django 4.0.5 on 2022-07-18 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_review_owner_alter_review_unique_together'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='vote_ratio',
        ),
        migrations.RemoveField(
            model_name='project',
            name='vote_total',
        ),
    ]
