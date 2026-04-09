import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')
django.setup()

from django.contrib.auth.models import User
from shop.models import Category, Product

# Create superuser
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')
    print("Superuser 'admin' created with password 'admin'.")

# Create categories
cat1, _ = Category.objects.get_or_create(name='Electronics', slug='electronics')
cat2, _ = Category.objects.get_or_create(name='Books', slug='books')

# Create products
Product.objects.get_or_create(
    category=cat1,
    name='Smartphone',
    slug='smartphone',
    price=599.99,
    description='A great smartphone.'
)

Product.objects.get_or_create(
    category=cat2,
    name='Django for Beginners',
    slug='django-for-beginners',
    price=39.00,
    description='Learn Django from scratch.'
)

print("Database populated with sample data!")
