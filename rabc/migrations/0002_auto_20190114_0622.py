# Generated by Django 2.0 on 2019-01-14 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rabc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PermissonGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='permission',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rabc.PermissonGroup'),
        ),
    ]
