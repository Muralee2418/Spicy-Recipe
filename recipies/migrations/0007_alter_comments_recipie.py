# Generated by Django 3.2.5 on 2022-01-20 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipies', '0006_auto_20220120_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='recipie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recipies.recipie'),
        ),
    ]