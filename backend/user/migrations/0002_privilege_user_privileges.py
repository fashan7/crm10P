# Generated by Django 4.2.2 on 2023-06-23 18:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Privilege',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('assigned_users', models.ManyToManyField(related_name='assigned_privileges', related_query_name='assigned_privileges', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='privileges',
            field=models.ManyToManyField(related_name='users', related_query_name='users', to='user.privilege'),
        ),
    ]
