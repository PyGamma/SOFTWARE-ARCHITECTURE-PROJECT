# Generated by Django 2.2.6 on 2019-11-14 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0002_remove_student_hobbies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='b_date',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='stu_id',
            field=models.CharField(max_length=20),
        ),
    ]
