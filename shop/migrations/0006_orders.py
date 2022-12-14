# Generated by Django 4.1.3 on 2022-12-24 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_contact_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=90)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
                ('phone', models.CharField(default='', max_length=70)),
                ('address', models.TextField()),
                ('city', models.CharField(default='', max_length=90)),
                ('state', models.CharField(default='', max_length=90)),
                ('zipcode', models.CharField(default='', max_length=90)),
            ],
        ),
    ]
