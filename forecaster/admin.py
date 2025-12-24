from django.contrib import admin
from .models import Scenario, ScenarioSnapshot, Alert, Notification


@admin.register(Scenario)
class ScenarioAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'scenario_type', 'initial_investment', 
                    'monthly_contribution', 'projected_value', 'created_at']
    list_filter = ['scenario_type', 'created_at']
    search_fields = ['name', 'user__username']
    readonly_fields = ['projected_value', 'total_contributions', 'total_gains', 
                      'created_at', 'updated_at']


@admin.register(ScenarioSnapshot)
class ScenarioSnapshotAdmin(admin.ModelAdmin):
    list_display = ['scenario', 'year', 'value', 'contributions_to_date', 'gains_to_date']
    list_filter = ['scenario']
    search_fields = ['scenario__name']


@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'alert_type', 'status', 'scenario', 'created_at', 'triggered_at']
    list_filter = ['alert_type', 'status', 'created_at']
    search_fields = ['name', 'user__username']
    readonly_fields = ['triggered_at', 'last_checked']


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'notification_type', 'is_read', 'created_at']
    list_filter = ['notification_type', 'is_read', 'created_at']
    search_fields = ['title', 'user__username', 'message']
