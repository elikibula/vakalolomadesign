from django.contrib import admin
from django.urls import path, include
from designs.admin import custom_admin_site

urlpatterns = [
       path('admin/', custom_admin_site.urls),
       path('', include('designs.urls')),
]


# Admin Site Config
admin.sites.AdminSite.site_header = 'Web Admin'
admin.sites.AdminSite.site_title = 'Web Admin'
admin.sites.AdminSite.index_title = 'Vakaloloma Designs'