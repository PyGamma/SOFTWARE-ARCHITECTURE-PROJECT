# Generated by Django 2.2.6 on 2019-11-15 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0003_auto_20191114_2119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.AlterField(
            model_name='student',
            name='stu_id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
