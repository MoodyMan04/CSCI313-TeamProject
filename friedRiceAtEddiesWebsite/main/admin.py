from django.contrib import admin
from main import models as main_models
from checkout import models as checkout_models

# Register your models here.
admin.site.register(main_models.Ingredient)
admin.site.register(main_models.Recipe)
admin.site.register(main_models.Menu)
admin.site.register(main_models.Order)
admin.site.register(main_models.Way_Recieved)
admin.site.register(checkout_models.Member)
