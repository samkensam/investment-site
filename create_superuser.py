import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'investment_site.settings')
django.setup()

from django.contrib.auth.models import User

# Create superuser if it doesn't exist
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print("✓ Superuser created successfully!")
    print("  Username: admin")
    print("  Password: admin123")
    print("  Email: admin@example.com")
else:
    print("Superuser 'admin' already exists.")
