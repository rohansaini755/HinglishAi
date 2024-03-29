# Generated by Django 4.1.3 on 2023-03-17 14:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Text', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='submition',
            fields=[
                ('submition_id', models.AutoField(primary_key=True, serialize=False)),
                ('answer', models.CharField(max_length=2000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('suggesyions', models.CharField(default='', max_length=1000, null=True)),
                ('status', models.BooleanField(default=True)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('text_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Text.text')),
            ],
            options={
                'db_table': 'submitions',
            },
        ),
    ]
