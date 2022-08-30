from django.apps import AppConfig
import sys 

class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'assets'

    def ready(self):
        is_manage_py = any(arg.casefold().endswith("manage.py") for arg in sys.argv)
        is_runserver = any(arg.casefold() == "runserver" for arg in sys.argv)

        if (is_manage_py and is_runserver):
            from assets import config,queue
            queue.monitoring_queue().empty()
            config.insert_assets()
            config.start_crons()