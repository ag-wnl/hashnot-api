# Generated by Django 4.2.4 on 2023-08-30 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HashnotUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_subject', models.TextField()),
                ('post_content', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='hashnot',
            name='active',
        ),
        migrations.AddField(
            model_name='hashnot',
            name='fav_techstack',
            field=models.TextField(default='None'),
        ),
        migrations.AddField(
            model_name='hashnot',
            name='user_mail',
            field=models.CharField(default='None', max_length=255),
        ),
    ]