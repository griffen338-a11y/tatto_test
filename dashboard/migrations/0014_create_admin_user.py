from django.db import migrations
from django.contrib.auth.models import User

def create_admin_user(apps, schema_editor):
    if not User.objects.filter(username='studio_admin').exists():
        User.objects.create_superuser(
            username='studio_admin',
            email='contact@inkspire.com',
            password='AdminSecure#2025'
        )

class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_alter_artist_bio_alter_testimonial_stars'),  # latest migration
    ]

    operations = [
        migrations.RunPython(create_admin_user),
    ]

