# Generated by Django 2.0.2 on 2018-02-10 12:37

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0002_auto_20180210_1913'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nmae')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='taskmanager.Profile', verbose_name='user')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
                'ordering': ('user', 'name'),
            },
        ),
        migrations.AlterField(
            model_name='project',
            name='color',
            field=models.CharField(default='#fff', help_text='Enter the hex color code, like #ccc or # cccccc', max_length=7, validators=[django.core.validators.RegexValidator('(^#[0-9a-fA-F]{3}$)|(^#[0-9a-fA-F]{6}$)')], verbose_name='color'),
        ),
        migrations.AlterUniqueTogether(
            name='tag',
            unique_together={('user', 'name')},
        ),
    ]
