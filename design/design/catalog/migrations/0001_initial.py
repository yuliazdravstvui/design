# Generated by Django 3.2.23 on 2023-11-02 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a floor plans', max_length=200)),
                ('file', models.FileField(null=True, upload_to='files/')),
            ],
        ),
    ]
