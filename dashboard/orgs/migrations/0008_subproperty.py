# Generated by Django 2.1.7 on 2019-02-20 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgs', '0007_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('body', models.TextField()),
                ('group', models.ManyToManyField(related_name='group', to='orgs.Detail')),
            ],
        ),
    ]
