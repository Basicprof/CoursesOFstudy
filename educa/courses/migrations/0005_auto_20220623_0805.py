# Generated by Django 2.0.5 on 2022-06-23 05:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_course_students'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['-created'], 'verbose_name': 'Курс', 'verbose_name_plural': 'Курсы'},
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={'ordering': ['title'], 'verbose_name': 'Предмет', 'verbose_name_plural': 'Предметы'},
        ),
    ]
