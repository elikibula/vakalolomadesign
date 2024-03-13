# designs/apps.py
from django.apps import AppConfig

class DesignsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'designs'
    verbose_name = 'Vanua ni Taba'  # Change this to your desired label
