from django.contrib import admin
from django.urls import path
from appointments import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('thank-you/', views.thank_you, name='thank_you'),
    # path('create_visit/', views.create_visit, name='create_visit'),
    path('get-services/<int:master_id>/', views.get_services, name='get_services'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
