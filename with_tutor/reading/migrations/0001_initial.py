# Generated by Django 4.0.3 on 2022-04-11 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReadingTheme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, upload_to='reading_theme', verbose_name='Image')),
            ],
        ),
        migrations.CreateModel(
            name='ReadingSubsections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, upload_to='Reading_subsections', verbose_name='Image')),
                ('theme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reading_subsection', to='reading.readingtheme')),
            ],
        ),
        migrations.CreateModel(
            name='ReadingMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, upload_to='reading_material', verbose_name='Image')),
                ('subsection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reading_material', to='reading.readingsubsections')),
            ],
        ),
    ]
