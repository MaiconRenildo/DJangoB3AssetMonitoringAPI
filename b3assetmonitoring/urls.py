from django.urls import path,include
from rest_framework import routers
from django.contrib import admin
from assets import viewset
from assets import views


route = routers.DefaultRouter()
route.register(r'assets',viewset.AssetViewSet,basename='assets')
route.register(r'monitoring',viewset.MonitoringViewSet,basename='monitoring')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(route.urls)),
    path('monitoring',views.AssetMonitoring.as_view())
]