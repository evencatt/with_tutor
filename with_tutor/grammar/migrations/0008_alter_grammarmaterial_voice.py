# Generated by Django 4.0.3 on 2022-04-24 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grammar', '0007_delete_grammarvoices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grammarmaterial',
            name='voice',
            field=models.FileField(blank=True, upload_to='grammar_voices'),
        ),
    ]
