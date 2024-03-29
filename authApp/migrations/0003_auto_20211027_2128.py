# Generated by Django 3.2.8 on 2021-10-28 02:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0002_auto_20211027_2028'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('car_type', models.CharField(choices=[('sedan', 'sedan'), ('sedan', 'sedan'), ('pickup', 'pickup'), ('other', 'other')], max_length=45)),
                ('license_number', models.CharField(max_length=10)),
                ('location', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('city', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('cellphone', models.CharField(max_length=12)),
                ('created', models.DateTimeField(auto_now=True)),
                ('date', models.DateField()),
                ('is_manager', models.BooleanField()),
            ],
        ),
        migrations.DeleteModel(
            name='Passenger',
        ),
        migrations.AddField(
            model_name='manager',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='manager_user', to='authApp.user'),
        ),
    ]
