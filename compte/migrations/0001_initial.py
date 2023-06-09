# Generated by Django 4.1.5 on 2023-04-12 01:06

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('permission', models.CharField(blank=True, choices=[('Commercial', 'Commercial'), ('Administrateur', 'Administrateur')], default='commercial', max_length=15, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Adresse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_commune', models.CharField(max_length=50)),
                ('nom_voie', models.CharField(max_length=50, unique=True)),
                ('code_postal', models.CharField(max_length=10)),
                ('x', models.CharField(max_length=10)),
                ('y', models.CharField(max_length=10)),
                ('geo', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Locataire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=30, unique=True)),
                ('Nbcontrat', models.CharField(max_length=20)),
                ('nom', models.CharField(max_length=20)),
                ('prenom', models.CharField(max_length=20)),
                ('photo', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=85, scale=None, size=[250, 350], upload_to='photo')),
                ('sexe', models.CharField(choices=[('homme', 'homme'), ('femme', 'femme')], max_length=20)),
                ('numberPhone', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')])),
            ],
        ),
        migrations.CreateModel(
            name='Appartement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('piece', models.CharField(choices=[('3 piece', '3 piece'), ('2 piece', '2 piece'), ('4 piece', '4 piece'), ('1 piece', '1 piece'), ('5 piece', '5 piece'), ('6 piece', '6 piece')], max_length=100)),
                ('loyer', models.IntegerField()),
                ('date', models.DateField(blank=True, null=True)),
                ('charges', models.IntegerField()),
                ('allocation', models.IntegerField(blank=True, null=True)),
                ('caution', models.IntegerField()),
                ('sanitaire', models.CharField(choices=[('Cuisine, salle de bain(wc)', 'Cuisine, salle de bain(wc)'), ('Cuisine américaine, salle de bain (wc)', 'Cuisine américaine, salle de bain (wc)'), ('Cuisine, salle de bain, (wc) à part', 'Cuisine, salle de bain, (wc) à part'), ('Cuisine américaine, salle de bain, (wc) à part', 'Cuisine américaine, salle de bain, (wc) à part')], max_length=100)),
                ('solde', models.BooleanField(default=False)),
                ('montant', models.IntegerField()),
                ('agence', models.BooleanField(default=True)),
                ('etat', models.CharField(choices=[('bon', 'Bon'), ('correct', 'Correct'), ('Abimé', 'Abimé'), ('Insalubre', 'Insalubre')], max_length=20)),
                ('observation', models.CharField(max_length=200)),
                ('numeros', models.IntegerField()),
                ('adresse', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='compte.adresse')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='locataire', to='compte.locataire')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Annonce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=30)),
                ('sous_titre', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=1000)),
                ('photo', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=85, scale=None, size=[250, 350], upload_to='photo')),
                ('photo1', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=85, scale=None, size=[250, 350], upload_to='photo')),
                ('photo2', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=85, scale=None, size=[250, 350], upload_to='photo')),
                ('appartement', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='compte.appartement')),
            ],
        ),
    ]
