# Generated by Django 5.1.5 on 2025-02-01 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nycapi', '0003_nycaddresslookuppage_appear_in_search_results_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nycaddresslookuppage',
            name='instructions',
            field=models.TextField(blank=True, default='Enter an address and zip code to retrieve NYC OpenData information, including 311 complaints, lead violations, bedbug reports, housing violations, and NYCHA data.', help_text='Instructions displayed to users on how to use the tool.'),
        ),
    ]
