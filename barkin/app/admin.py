from django.contrib import admin

# Register your models here.
from .models import User
from .models import Dog
from .models import Park
from .models import ParkReview
from .models import Schedule


admin.site.register(User)
admin.site.register(Dog)
admin.site.register(Park)
admin.site.register(ParkReview)
admin.site.register(Schedule)
