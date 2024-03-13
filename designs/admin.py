from django.contrib.admin import AdminSite
from .models import Product

class CustomAdminSite(AdminSite):
    site_header = 'Vakaloloma Designs'  # Change this to your desired admin header
    site_title = 'Vakaloloma Designs'  # Change this to your desired site title

custom_admin_site = CustomAdminSite(name='customadmin')

# Register your models with the custom admin site
custom_admin_site.register(Product)
