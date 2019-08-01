# Generated by Django 2.2.3 on 2019-07-30 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coureur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('nationaliter', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('pays', models.CharField(max_length=30)),
                ('detail', models.TextField()),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('participend', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='coureur_competition', to='profil.Coureur')),
            ],
        ),
    ]