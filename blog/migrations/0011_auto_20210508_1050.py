# Generated by Django 3.1.7 on 2021-05-08 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20210507_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='country',
            field=models.CharField(choices=[('Chiny', 'Chiny'), ('Grecja', 'Grecja'), ('Hiszpania', 'Hiszpania'), ('Indie', 'Indie'), ('Portugalia', 'Portugalia'), ('Tajlandia', 'Tajlandia'), ('INNE', 'INNE')], default=None, max_length=30),
        ),
        migrations.CreateModel(
            name='Spice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spice', models.CharField(max_length=50)),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.dish')),
            ],
        ),
    ]
