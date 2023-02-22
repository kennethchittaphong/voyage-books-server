# Generated by Django 4.1.7 on 2023-02-22 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=55)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('about', models.CharField(max_length=280)),
                ('profile_image_url', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55)),
                ('location', models.CharField(max_length=55)),
                ('photo_url', models.CharField(max_length=255)),
                ('content', models.TextField(max_length=1000)),
                ('creation_date', models.DateField()),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voyagebooksapi.user')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=800)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voyagebooksapi.user')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voyagebooksapi.post')),
            ],
        ),
    ]
