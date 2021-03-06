# Generated by Django 3.2.6 on 2021-09-15 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('projectlink', models.URLField()),
                ('language', models.TextField(max_length=40)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('about', models.TextField()),
                ('status', models.IntegerField(choices=[(0, 'Working!'), (1, 'Finished')], default=0)),
            ],
        ),
    ]
