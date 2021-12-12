# Generated by Django 3.2.9 on 2021-12-11 03:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_alter_book_isbn'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='genres',
            options={'verbose_name': 'genre', 'verbose_name_plural': 'genres'},
        ),
        migrations.AlterModelOptions(
            name='tags',
            options={'verbose_name': 'tag', 'verbose_name_plural': 'tags'},
        ),
        migrations.RenameField(
            model_name='book',
            old_name='name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='name',
            new_name='title',
        ),
    ]