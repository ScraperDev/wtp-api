# Generated by Django 2.2.7 on 2019-11-15 18:08

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
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('asking_price', models.IntegerField(editable=False)),
                ('volume', models.IntegerField(editable=False)),
                ('water_type', models.CharField(editable=False, max_length=50)),
                ('partial_listing', models.BooleanField(default=False, editable=False)),
                ('minimum_increment', models.IntegerField(blank=True, editable=False, null=True)),
                ('twai_confirmed', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
