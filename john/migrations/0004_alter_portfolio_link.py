# Generated by Django 4.2.7 on 2024-02-01 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('john', '0003_portfolio_name_alter_about_career_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='link',
            field=models.FileField(upload_to='pdfs/'),
        ),
    ]
