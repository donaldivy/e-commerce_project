# Generated by Django 3.0.8 on 2021-04-07 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store1', '0003_auto_20201001_0932'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('people', models.CharField(choices=[('1 person', '1 PERSON'), ('2 person', '2 PERSON'), ('3 person', '3 PERSON'), ('4+ person', '4+ PERSON')], max_length=200)),
                ('phone', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=100)),
                ('message', models.TextField(blank=True)),
                ('contact_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]