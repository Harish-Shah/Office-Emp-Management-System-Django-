from django.contrib import admin

from .models import Employee,Role,Department
# Register your models here.

# registering the models with the Django admin interface.
#  By registering the models, Django automatically generates an admin interface for each model, 
# allowing easy management and manipulation of the corresponding data.

admin.site.register(Employee)
admin.site.register(Role)
admin.site.register(Department)