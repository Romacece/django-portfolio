# Generated by Django 4.2.7 on 2024-02-02 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('john', '0005_skills_progress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='home',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='skills',
            name='skill_name',
            field=models.CharField(max_length=50),
        ),
    ]
