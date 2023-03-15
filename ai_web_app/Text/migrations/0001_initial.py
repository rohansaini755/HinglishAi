# Generated by Django 4.1.3 on 2023-02-09 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Text',
            fields=[
                ('text_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('level', models.CharField(blank=True, max_length=20, null=True)),
                ('subLevel', models.IntegerField(default=0)),
                ('hindiText', models.CharField(max_length=2000)),
                ('englishText', models.CharField(max_length=2000)),
                ('flag1', models.BooleanField(default=True)),
                ('hintString', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'db_table': 'text_content',
            },
        ),
    ]
