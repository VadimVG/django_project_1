# Generated by Django 4.1.5 on 2023-07-16 12:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tech_blog', '0008_rename_username_questions_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
