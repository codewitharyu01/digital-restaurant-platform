from django.contrib import admin
from .models import Repass,FoodDiliver,BookingTable,FeedbackForm

# Register your models here.

admin.register(Repass)
admin.register(FoodDiliver)
admin.register(BookingTable)
admin.register(FeedbackForm)

