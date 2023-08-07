# Generated by Django 3.2.20 on 2023-08-07 16:02

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
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=150)),
                ('content', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, default='../default_post_image_rwq55u', upload_to='images/')),
                ('dog_breed', models.CharField(choices=[('german_shepherd', 'German Shepherd'), ('bulldog', 'Bulldog'), ('labrador_retriever', 'Labrador Retriever'), ('golden_retriever', 'Golden Retriever'), ('french_bulldog', 'French Bulldog'), ('siberian_husky', 'Siberian Husky'), ('alaskan_malamute', 'Alaskan Malamute'), ('poodle', 'Poodle'), ('chihuahua', 'Chihuahua'), ('border_collie', 'Border Collie'), ('dachshund', 'Dachshund'), ('terrier', 'Terrier'), ('rottweiler', 'Rottweiler'), ('australian_shepherd', 'Australian Shepherd'), ('bichon_frisé', 'Bichon Frisé'), ('chow_chow', 'Chow Chow'), ('pomeranian', 'Pomeranian'), ('cavalier_king_charles_spaniel', 'Cavalier King Charles Spaniel'), ('english_cocker_spaniel', 'English Cocker Spaniel')], default='none', max_length=30)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]