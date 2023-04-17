# Generated by Django 3.2.4 on 2023-04-17 22:34

import authentication.models
import datetime
from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(blank=True, error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, null=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, unique=True, verbose_name='email address')),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6)),
                ('lnd_directory', models.CharField(blank=True, max_length=200, verbose_name='lnd directory')),
                ('tls_cert_path', models.CharField(blank=True, max_length=200, verbose_name='tls cert_path')),
                ('grpc_host', models.CharField(blank=True, max_length=30, verbose_name='grpc host')),
                ('grpc_port', models.IntegerField(blank=True, verbose_name='grpc port')),
                ('macaroon_path', models.CharField(blank=True, max_length=200, verbose_name='macaroon path')),
                ('network', models.CharField(default='regtest', max_length=30, verbose_name='network')),
                ('is_verified', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=True, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('Id', models.UUIDField(default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'), primary_key=True, serialize=False)),
                ('is_passenger', models.BooleanField(default=False, verbose_name='user is a passenger')),
                ('is_driver', models.BooleanField(default=False, verbose_name='user is a driver')),
                ('wallet_balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', authentication.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='PasswordResetInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reset_code', models.CharField(default='000000', max_length=6, unique=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('expires_at', models.DateTimeField(default=datetime.datetime(2023, 4, 18, 22, 34, 17, 721598, tzinfo=utc))),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Password Reset Info',
                'ordering': ['user'],
            },
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('registered_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('lastupdated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.UUIDField(default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'), primary_key=True, serialize=False)),
                ('is_available', models.BooleanField(default=True)),
                ('lastupdated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='authentication_passenger_lastmodified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by')),
                ('registered_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='authentication_passenger_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Passenger', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-lastupdated_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('registered_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('lastupdated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.UUIDField(default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'), primary_key=True, serialize=False)),
                ('permit_number', models.CharField(default='UAX', max_length=50)),
                ('permit_class', models.CharField(default='UAX', max_length=50)),
                ('permit_expiry_date', models.CharField(default='UAX', max_length=50)),
                ('permit_issuance_date', models.CharField(default='UAX', max_length=50)),
                ('is_available', models.BooleanField(default=True)),
                ('lastupdated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='authentication_driver_lastmodified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by')),
                ('registered_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='authentication_driver_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Driver', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-lastupdated_at'],
                'abstract': False,
            },
        ),
    ]
