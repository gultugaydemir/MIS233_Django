# Generated by Django 3.1.5 on 2021-01-19 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dotabase', '0007_runes'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeeklyPolls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=100)),
            ],
        ),
    ]