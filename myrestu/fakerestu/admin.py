from django.contrib import admin
from .models import Repass,FoodDiliver,BookingTable,FeedbackForm

# Register your models here.

admin.site.register(Repass)
admin.site.register(FoodDiliver)
admin.site.register(BookingTable)
admin.site.register(FeedbackForm)

