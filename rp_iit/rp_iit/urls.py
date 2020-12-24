
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from .views import index
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='RP -IIT API')

urlpatterns = [
    path('', schema_view),
    path('admin/', admin.site.urls),
    path('<str:key>/', include([ 
            path('check_server/', index),
            path('auth/',include('authentication.urls')),
            path('api/', include('rest_api.urls')),
        ]))


]

if settings.DEBUG == True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

