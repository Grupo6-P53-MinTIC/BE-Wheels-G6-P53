# Generated by Django 3.2.7 on 2021-10-31 17:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authApp', '0004_alter_user_is_manager'),
    ]

    operations = [
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('from_place', models.CharField(max_length=100)),
                ('to_place', models.CharField(max_length=100)),
                ('pass_through', models.CharField(max_length=100, null=True)),
                ('published', models.DateTimeField(auto_now_add=True)),
                ('date_travel', models.DateTimeField(auto_now_add=True)),
                ('seats', models.IntegerField(default=1)),
                ('id_manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
