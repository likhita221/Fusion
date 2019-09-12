# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-09-12 12:21
from __future__ import unicode_literals

import applications.globals.models
import datetime
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
            name='DepartmentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='student', max_length=50, unique=True)),
                ('full_name', models.CharField(default='Computer Science and Engineering', max_length=100)),
                ('type', models.CharField(choices=[('academic', 'Academic Designation'), ('administrative', 'Administrative Designation')], default='academic', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ExtraInfo',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('title', models.CharField(choices=[('Mr.', 'Mr.'), ('Mrs.', 'Mrs.'), ('Ms.', 'Ms.'), ('Dr.', 'Dr.'), ('Professor', 'Prof.'), ('Shreemati', 'Shreemati'), ('Shree', 'Shree')], default='Dr.', max_length=20)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='M', max_length=2)),
                ('date_of_birth', models.DateField(default=datetime.date(1970, 1, 1))),
                ('address', models.TextField(default='', max_length=1000)),
                ('phone_no', models.BigIntegerField(default=9999999999, null=True)),
                ('user_type', models.CharField(choices=[('student', 'student'), ('staff', 'staff'), ('compounder', 'compounder'), ('faculty', 'faculty')], max_length=20)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='globals/profile_pictures')),
                ('about_me', models.TextField(blank=True, default='NA', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('feedback', models.TextField(blank=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='fusion_feedback', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HoldsDesignation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('held_at', models.DateTimeField(auto_now=True)),
                ('designation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='designees', to='globals.Designation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='holds_designations', to=settings.AUTH_USER_MODEL)),
                ('working', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='current_designation', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_type', models.CharField(choices=[('feature_request', 'Feature Request'), ('bug_report', 'Bug Report'), ('security_issue', 'Security Issue'), ('ui_issue', 'User Interface Issue'), ('other', 'Other than the ones listed')], max_length=63)),
                ('module', models.CharField(choices=[('academic_information', 'Academic'), ('central_mess', 'Central Mess'), ('complaint_system', 'Complaint System'), ('eis', 'Employee Imformation System'), ('file_tracking', 'File Tracking System'), ('health_center', 'Health Center'), ('leave', 'Leave'), ('online_cms', 'Online Course Management System'), ('placement_cell', 'Placement Cell'), ('scholarships', 'Scholarships'), ('visitor_hostel', 'Visitor Hostel'), ('other', 'Other')], max_length=63)),
                ('closed', models.BooleanField(default=False)),
                ('text', models.TextField()),
                ('title', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='IssueImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=applications.globals.models.Issue_image_directory)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='globals.ExtraInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='globals.ExtraInfo')),
            ],
        ),
        migrations.AddField(
            model_name='issue',
            name='images',
            field=models.ManyToManyField(blank=True, to='globals.IssueImage'),
        ),
        migrations.AddField(
            model_name='issue',
            name='support',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='issue',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reported_issues', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='extrainfo',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='globals.DepartmentInfo'),
        ),
        migrations.AddField(
            model_name='extrainfo',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
