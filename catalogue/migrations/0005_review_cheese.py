# Generated by Django 4.1.7 on 2023-02-22 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0004_remove_review_cheese'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='cheese',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogue.cheese'),
        ),
    ]
