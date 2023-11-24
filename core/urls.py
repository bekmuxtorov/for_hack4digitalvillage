from django.contrib import admin
from django.urls import path, include

admin.site.site_title = "Terminal Group"
admin.site.site_header = "Terminal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("base.urls"))
]
