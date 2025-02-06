from django.contrib import admin
from .models import Hotel, HotelBooking, Amenities, HotelImages

# Đăng ký các models với admin site
admin.site.register(Hotel)
admin.site.register(HotelBooking)
admin.site.register(Amenities)
admin.site.register(HotelImages)

# Hoặc có thể đăng ký cùng lúc như sau:
# admin.site.register((Hotel, HotelBooking, Amenities, HotelImages))