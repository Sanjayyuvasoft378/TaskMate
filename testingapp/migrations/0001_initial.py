# Generated by Django 2.2.12 on 2022-11-29 05:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CommonModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdOn', models.DateTimeField()),
                ('createdBy', models.CharField(max_length=10)),
                ('updatedOn', models.DateTimeField()),
                ('updatedBy', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TestTaskModel',
            fields=[
                ('commonmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='testingapp.CommonModel')),
                ('image', models.ImageField(upload_to='testing')),
                ('name', models.CharField(max_length=20)),
                ('post', models.CharField(max_length=100)),
                ('testimonial_description', models.TextField(max_length=200)),
            ],
            options={
                'db_table': 'Task',
            },
            bases=('testingapp.commonmodel',),
        ),
        migrations.CreateModel(
            name='TodoListModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=200)),
                ('done', models.BooleanField(default=False)),
                ('manage', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]