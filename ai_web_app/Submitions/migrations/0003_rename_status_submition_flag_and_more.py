# Generated by Django 4.1.3 on 2023-03-18 17:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Submitions', '0002_rename_email_submition_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submition',
            old_name='status',
            new_name='flag',
        ),
        migrations.RenameField(
            model_name='submition',
            old_name='suggesyions',
            new_name='suggestions',
        ),
        migrations.RenameField(
            model_name='submition',
            old_name='id',
            new_name='username',
        ),
        migrations.AddField(
            model_name='submition',
            name='accuracy',
            field=models.IntegerField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='submition',
            name='answer_status',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
