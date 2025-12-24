from django import forms
from .models import Scenario, Alert


class ScenarioForm(forms.ModelForm):
    class Meta:
        model = Scenario
        fields = [
            'name', 'scenario_type', 'initial_investment', 
            'monthly_contribution', 'annual_return_rate', 
            'investment_period_years', 'inflation_rate', 'volatility'
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Retirement Plan 2025'
            }),
            'scenario_type': forms.Select(attrs={'class': 'form-control'}),
            'initial_investment': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '10000.00',
                'step': '0.01'
            }),
            'monthly_contribution': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '500.00',
                'step': '0.01'
            }),
            'annual_return_rate': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '7.00',
                'step': '0.01',
                'min': '-100',
                'max': '100'
            }),
            'investment_period_years': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '20',
                'min': '1',
                'max': '100'
            }),
            'inflation_rate': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '2.50',
                'step': '0.01'
            }),
            'volatility': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0.00',
                'step': '0.01'
            }),
        }
        labels = {
            'name': 'Scenario Name',
            'scenario_type': 'Scenario Type',
            'initial_investment': 'Initial Investment ($)',
            'monthly_contribution': 'Monthly Contribution ($)',
            'annual_return_rate': 'Expected Annual Return (%)',
            'investment_period_years': 'Investment Period (Years)',
            'inflation_rate': 'Inflation Rate (%)',
            'volatility': 'Volatility (%)',
        }


class AlertForm(forms.ModelForm):
    class Meta:
        model = Alert
        fields = [
            'name', 'alert_type', 'scenario', 'target_value', 
            'target_roi', 'reminder_frequency_days', 'message', 'send_email'
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., $100K Milestone'
            }),
            'alert_type': forms.Select(attrs={'class': 'form-control'}),
            'scenario': forms.Select(attrs={'class': 'form-control'}),
            'target_value': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '100000.00',
                'step': '0.01'
            }),
            'target_roi': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '50.00',
                'step': '0.01'
            }),
            'reminder_frequency_days': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '30',
                'min': '1'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Alert message to display when triggered...'
            }),
            'send_email': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'name': 'Alert Name',
            'alert_type': 'Alert Type',
            'scenario': 'Linked Scenario (Optional)',
            'target_value': 'Target Portfolio Value ($)',
            'target_roi': 'Target ROI (%)',
            'reminder_frequency_days': 'Reminder Frequency (Days)',
            'message': 'Alert Message',
            'send_email': 'Send Email Notification',
        }
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        if user:
            self.fields['scenario'].queryset = Scenario.objects.filter(user=user)
            self.fields['scenario'].required = False
