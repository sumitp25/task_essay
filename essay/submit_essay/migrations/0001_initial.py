# Generated by Django 2.2.8 on 2020-02-13 08:33

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
            name='WriteEssay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(choices=[('RIGHT TO EDUCATION', 'Right to Education'), ('EFFECTS OF POLLUTION', 'Effects of pollution'), ('GROWING UP IN POVERTY', 'Growing up in poverty'), ('INTERNET INFLUENCE ON KIDS', 'Internet Influence on kids')], max_length=25)),
                ('essay_language', models.CharField(choices=[('ENGLISH', 'English'), ('HINDI', 'Hindi')], max_length=12)),
                ('essay_text', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
