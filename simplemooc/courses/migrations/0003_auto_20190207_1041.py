# Generated by Django 2.1.5 on 2019-02-07 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20190207_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='courses/images', verbose_name='Imagem'),
        ),
    ]
