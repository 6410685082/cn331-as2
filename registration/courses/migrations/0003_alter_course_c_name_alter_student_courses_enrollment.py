# Generated by Django 4.2.5 on 2023-10-06 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_remove_student_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='c_name',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(blank=True, to='courses.course'),
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courses', models.CharField(max_length=32)),
                ('name', models.ManyToManyField(blank=True, to='courses.course')),
            ],
        ),
    ]
