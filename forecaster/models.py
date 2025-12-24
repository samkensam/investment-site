from django.db import models
from django.contrib.auth.models import User

class Scenario(models.Model):
    """Model for investment scenario analysis"""
    SCENARIO_TYPES = [
        ('optimistic', 'Optimistic'),
        ('realistic', 'Realistic'),
        ('pessimistic', 'Pessimistic'),
        ('custom', 'Custom'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='scenarios')
    name = models.CharField(max_length=200)
    scenario_type = models.CharField(max_length=20, choices=SCENARIO_TYPES, default='realistic')
    
    # Investment parameters
    initial_investment = models.DecimalField(max_digits=12, decimal_places=2)
    monthly_contribution = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    annual_return_rate = models.DecimalField(max_digits=5, decimal_places=2, help_text="Expected annual return percentage")
    investment_period_years = models.IntegerField(help_text="Investment period in years")
    
    # Additional parameters
    inflation_rate = models.DecimalField(max_digits=5, decimal_places=2, default=2.5, help_text="Annual inflation rate percentage")
    volatility = models.DecimalField(max_digits=5, decimal_places=2, default=0, help_text="Expected volatility percentage")
    
    # Results (calculated)
    projected_value = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    total_contributions = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    total_gains = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} ({self.scenario_type})"
    
    def calculate_projection(self):
        """Calculate the projected investment value"""
        P = float(self.initial_investment)
        PMT = float(self.monthly_contribution)
        r = float(self.annual_return_rate) / 100 / 12  # Monthly rate
        n = self.investment_period_years * 12  # Total months
        
        # Future value with monthly contributions
        if r == 0:
            future_value = P + (PMT * n)
        else:
            # FV = P(1+r)^n + PMT * [((1+r)^n - 1) / r]
            future_value = P * ((1 + r) ** n) + PMT * (((1 + r) ** n - 1) / r)
        
        total_contributions = P + (PMT * n)
        total_gains = future_value - total_contributions
        
        self.projected_value = round(future_value, 2)
        self.total_contributions = round(total_contributions, 2)
        self.total_gains = round(total_gains, 2)
        self.save()
        
        return self.projected_value


class ScenarioSnapshot(models.Model):
    """Yearly snapshots of scenario projections"""
    scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE, related_name='snapshots')
    year = models.IntegerField()
    value = models.DecimalField(max_digits=15, decimal_places=2)
    contributions_to_date = models.DecimalField(max_digits=15, decimal_places=2)
    gains_to_date = models.DecimalField(max_digits=15, decimal_places=2)
    
    class Meta:
        ordering = ['year']
        unique_together = ['scenario', 'year']
    
    def __str__(self):
        return f"{self.scenario.name} - Year {self.year}"


class Alert(models.Model):
    """Investment alerts and notifications"""
    ALERT_TYPES = [
        ('milestone', 'Milestone Reached'),
        ('goal', 'Investment Goal'),
        ('threshold', 'Value Threshold'),
        ('roi', 'ROI Target'),
        ('reminder', 'Periodic Reminder'),
    ]
    
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('triggered', 'Triggered'),
        ('disabled', 'Disabled'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='alerts')
    scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE, related_name='alerts', null=True, blank=True)
    
    name = models.CharField(max_length=200)
    alert_type = models.CharField(max_length=20, choices=ALERT_TYPES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    
    # Alert parameters
    target_value = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, 
                                      help_text="Target portfolio value")
    target_roi = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True,
                                    help_text="Target ROI percentage")
    reminder_frequency_days = models.IntegerField(null=True, blank=True,
                                                  help_text="Days between reminders")
    
    message = models.TextField(help_text="Custom alert message")
    
    # Email notification
    send_email = models.BooleanField(default=False, help_text="Send email notification")
    
    # Tracking
    created_at = models.DateTimeField(auto_now_add=True)
    triggered_at = models.DateTimeField(null=True, blank=True)
    last_checked = models.DateTimeField(null=True, blank=True)
    next_reminder = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} ({self.get_alert_type_display()})"
    
    def check_condition(self):
        """Check if alert condition is met"""
        if self.status != 'active':
            return False
        
        if self.scenario:
            if self.alert_type == 'threshold' and self.target_value:
                return self.scenario.projected_value >= self.target_value
            
            elif self.alert_type == 'roi' and self.target_roi:
                if self.scenario.total_contributions > 0:
                    current_roi = (float(self.scenario.total_gains) / float(self.scenario.total_contributions)) * 100
                    return current_roi >= float(self.target_roi)
            
            elif self.alert_type == 'milestone' and self.target_value:
                return self.scenario.projected_value >= self.target_value
            
            elif self.alert_type == 'goal' and self.target_value:
                return self.scenario.projected_value >= self.target_value
        
        return False


class Notification(models.Model):
    """User notifications"""
    NOTIFICATION_TYPES = [
        ('alert', 'Alert'),
        ('info', 'Information'),
        ('warning', 'Warning'),
        ('success', 'Success'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    alert = models.ForeignKey(Alert, on_delete=models.SET_NULL, null=True, blank=True, related_name='notifications')
    scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE, null=True, blank=True)
    
    notification_type = models.CharField(max_length=20, choices=NOTIFICATION_TYPES, default='info')
    title = models.CharField(max_length=200)
    message = models.TextField()
    
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.title} - {self.user.username}"
