# Generated by Django 3.0.5 on 2020-05-14 22:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20200513_0015'),
    ]

    operations = [
        migrations.CreateModel(
            name='PictureUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='picture/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.User')),
            ],
            options={
                'verbose_name': 'Фото',
            },
        ),
    ]
