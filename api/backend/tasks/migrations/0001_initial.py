# Generated by Django 3.1.4 on 2021-01-01 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('detail', models.TextField(blank=True, max_length=500, null=True, verbose_name='Detail')),
                ('deadline', models.DateField(blank=True, null=True, verbose_name='Deadline')),
                ('status', models.IntegerField(choices=[(10, 'Added'), (20, 'Doing'), (30, 'Pending'), (100, 'Done')], default=10, verbose_name='Status')),
            ],
        ),
    ]
