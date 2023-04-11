# Generated by Django 4.2 on 2023-04-10 16:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_post_post_date_alter_post_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='adventure_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]