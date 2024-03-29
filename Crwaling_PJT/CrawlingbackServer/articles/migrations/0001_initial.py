# Generated by Django 3.2.18 on 2023-04-21 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('name', models.TextField(primary_key=True, serialize=False)),
                ('current_price', models.IntegerField()),
                ('previous_rate', models.IntegerField()),
                ('rate_of_change', models.TextField()),
                ('face_value', models.IntegerField()),
                ('market_capitalization', models.IntegerField()),
                ('listed_stock', models.IntegerField()),
                ('foreigner_ratio', models.FloatField()),
                ('trading_volume', models.TextField()),
                ('per', models.FloatField()),
                ('roe', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('title', models.TextField()),
                ('content', models.TextField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.stock')),
            ],
        ),
    ]
