# Generated by Django 3.1.5 on 2021-02-01 16:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pages', '0010_posts_anonymous'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sub_Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField()),
                ('comment', models.ManyToManyField(to='pages.Comments')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.posts')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
