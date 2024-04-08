# Generated by Django 3.2 on 2021-04-22 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website1', '0007_auto_20210422_1920'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=100)),
                ('user_email', models.CharField(max_length=100, unique=True)),
                ('user_designation', models.CharField(choices=[('STUDENT', 'STUDENT'), ('FACULTY', 'FACULTY')], default='STUDENT', max_length=50)),
                ('user_phone', models.IntegerField()),
                ('organisation', models.CharField(max_length=100)),
            ],
        ),
    ]
