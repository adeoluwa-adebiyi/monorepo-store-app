from django.apps import AppConfig


class InventoryConfig(AppConfig):
    name = 'inventory'


    def ready(self):

        # Add necessary signals on model events
        import .signals
