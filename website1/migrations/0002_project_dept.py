# Generated by Django 3.2 on 2021-04-18 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='dept',
            field=models.CharField(choices=[('it', 'IT'), ('comps', 'COMPS'), ('extc', 'EXTC'), ('mech', 'MECH')], default='it', max_length=6),
        ),
    ]
