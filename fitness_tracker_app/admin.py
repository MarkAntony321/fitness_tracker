from django.contrib import admin

# Register your models here.
from fitness_tracker_app.models import *

admin.site.register(User)
admin.site.register(MembershipCard)
admin.site.register(Workout)
admin.site.register(Exercise)
admin.site.register(Meal)
