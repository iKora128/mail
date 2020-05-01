# Generated by Django 3.0.5 on 2020-05-01 09:35

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
            name='MailModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='タイトル')),
                ('text', models.CharField(max_length=200, verbose_name='テキスト')),
                ('like_counter', models.IntegerField(blank=True, default=0, verbose_name='いいね数')),
                ('created_at', models.DateField(auto_now_add=True, null=True, verbose_name='作成時間')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='お名前')),
            ],
            options={
                'verbose_name_plural': 'メール',
                'db_table': 'mail',
            },
        ),
    ]
