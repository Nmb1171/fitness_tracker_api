# Generated by Django 5.1.3 on 2024-12-14 19:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('running', 'Running'), ('cycling', 'Cycling'), ('swimming', 'Swimming'), ('yoga', 'Yoga'), ('gym', 'gym'), ('walking', 'Walking'), ('hiking', 'Hiking'), ('dancing', 'Dancing'), ('boxing', 'Boxing'), ('weightlifting', 'Weightlifting'), ('aerobics', 'Aerobics'), ('pilates', 'Pilates'), ('other', 'Other')], max_length=50)),
                ('duration', models.PositiveIntegerField()),
                ('calories', models.PositiveIntegerField()),
                ('date', models.DateField()),
                ('notes', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]