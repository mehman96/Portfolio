# Generated by Django 4.0.1 on 2022-01-29 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_portfolio_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('job', models.CharField(blank=True, max_length=128, null=True)),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('desc', models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
    ]
