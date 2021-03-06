# Generated by Django 3.2.7 on 2021-09-12 18:24

import codechallenege.validators
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
            name='OtherLoans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank', models.CharField(max_length=100, validators=[codechallenege.validators.onlyletters])),
                ('amount_advanced', models.PositiveIntegerField()),
                ('date_granted', models.DateField()),
                ('Repayment_period', models.PositiveIntegerField()),
                ('Outstanding_balance', models.PositiveIntegerField()),
                ('bio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'OtherLoans',
            },
        ),
        migrations.CreateModel(
            name='LoanType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan', models.CharField(choices=[('normal', 'normal'), ('Development', 'Development'), ('Development', 'Development'), ('school fee', 'school fee')], max_length=16)),
                ('Purposeofloan', models.TextField(validators=[codechallenege.validators.onlyletters])),
                ('amountapplied', models.PositiveIntegerField()),
                ('bio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmploymentDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employer', models.CharField(max_length=100, validators=[codechallenege.validators.onlyletters])),
                ('physical_add', models.CharField(max_length=100, validators=[codechallenege.validators.onlyletters])),
                ('designation', models.CharField(max_length=100, validators=[codechallenege.validators.onlyletters])),
                ('employmenterms', models.CharField(choices=[('Peranent', 'Peranent'), ('casual', 'casual'), ('Contract', 'Contract')], max_length=9)),
                ('bio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'EmploymentDetails',
            },
        ),
        migrations.CreateModel(
            name='BusinessDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeofbusiness', models.CharField(max_length=100, validators=[codechallenege.validators.onlyletters])),
                ('yrsoperation', models.PositiveIntegerField()),
                ('Businessincome', models.PositiveIntegerField()),
                ('bio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'BusinessDetails',
            },
        ),
        migrations.CreateModel(
            name='Bioinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('membership_no', models.PositiveIntegerField()),
                ('first_name', models.CharField(max_length=50, validators=[codechallenege.validators.onlyletters])),
                ('middle_name', models.CharField(max_length=50, validators=[codechallenege.validators.onlyletters])),
                ('last_name', models.CharField(max_length=50, validators=[codechallenege.validators.onlyletters])),
                ('DateOfBirth', models.DateField()),
                ('Homeaddress', models.CharField(max_length=50, validators=[codechallenege.validators.onlyletters])),
                ('OffieNumber', models.PositiveIntegerField()),
                ('mobile_no', models.CharField(max_length=12)),
                ('Pin_no', models.CharField(max_length=50, validators=[codechallenege.validators.onlyisalnum])),
                ('Email', models.EmailField(max_length=100)),
                ('physical_add', models.CharField(max_length=100, validators=[codechallenege.validators.onlyletters])),
                ('town', models.CharField(max_length=100, validators=[codechallenege.validators.onlyletters])),
                ('estate', models.CharField(max_length=100, validators=[codechallenege.validators.onlyletters])),
                ('house_no', models.CharField(max_length=100, validators=[codechallenege.validators.onlyisalnum])),
                ('livedthrere', models.CharField(max_length=100, validators=[codechallenege.validators.onlyisnumeric])),
                ('Houseowned', models.CharField(choices=[('No', 'No'), ('yes', 'yes')], max_length=3)),
                ('martial_status', models.CharField(choices=[('single', 'single'), ('married', 'married'), ('window', 'window'), ('other', 'other')], max_length=7)),
                ('No_dependents', models.PositiveIntegerField()),
                ('bio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Bioinfo',
            },
        ),
        migrations.CreateModel(
            name='Bankdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.CharField(max_length=100)),
                ('acount_no', models.PositiveIntegerField()),
                ('Bank', models.CharField(max_length=100, validators=[codechallenege.validators.onlyletters])),
                ('branch', models.CharField(max_length=100)),
                ('bio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'bankdetails',
            },
        ),
    ]
