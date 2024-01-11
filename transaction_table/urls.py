from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',include('HMS.urls')),
    #path('',include('temp.urls')),
    path('', include('transaction_tables.urls')),
    path('api/',include('dj_rest_auth.urls'))
]
