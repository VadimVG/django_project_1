# Generated by Django 4.1.5 on 2023-07-16 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tech_blog', '0007_alter_articles_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questions',
            old_name='username',
            new_name='user_id',
        ),
    ]
