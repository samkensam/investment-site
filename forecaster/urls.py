from django.urls import path
from . import views

app_name = 'forecaster'

urlpatterns = [
    path('', views.scenario_list, name='scenario_list'),
    path('create/', views.scenario_create, name='scenario_create'),
    path('<int:pk>/', views.scenario_detail, name='scenario_detail'),
    path('<int:pk>/update/', views.scenario_update, name='scenario_update'),
    path('<int:pk>/delete/', views.scenario_delete, name='scenario_delete'),
    path('compare/', views.scenario_compare, name='scenario_compare'),
    
    # Alert URLs
    path('alerts/', views.alert_list, name='alert_list'),
    path('alerts/create/', views.alert_create, name='alert_create'),
    path('alerts/<int:pk>/update/', views.alert_update, name='alert_update'),
    path('alerts/<int:pk>/delete/', views.alert_delete, name='alert_delete'),
    path('alerts/<int:pk>/toggle/', views.alert_toggle, name='alert_toggle'),
    path('alerts/check/', views.check_alerts, name='check_alerts'),
    
    # Notification URLs
    path('notifications/', views.notification_list, name='notification_list'),
    path('notifications/<int:pk>/read/', views.notification_mark_read, name='notification_mark_read'),
    path('notifications/mark-all-read/', views.notification_mark_all_read, name='notification_mark_all_read'),
]
