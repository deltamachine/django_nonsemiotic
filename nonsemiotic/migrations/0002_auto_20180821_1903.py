# Generated by Django 2.0.3 on 2018-08-21 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nonsemiotic', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='languagesdata',
            options={'managed': False, 'ordering': ['lang_code', 'num'], 'verbose_name': 'языковые данные', 'verbose_name_plural': 'языковые данные'},
        ),
    ]