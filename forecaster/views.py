from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q
from .models import Scenario, ScenarioSnapshot, Alert, Notification
from .forms import ScenarioForm, AlertForm


@login_required
def scenario_list(request):
    """Display all scenarios for the logged-in user"""
    scenarios = Scenario.objects.filter(user=request.user)
    return render(request, 'forecaster/scenario_list.html', {'scenarios': scenarios})


@login_required
def scenario_create(request):
    """Create a new scenario"""
    if request.method == 'POST':
        form = ScenarioForm(request.POST)
        if form.is_valid():
            scenario = form.save(commit=False)
            scenario.user = request.user
            scenario.save()
            scenario.calculate_projection()
            generate_snapshots(scenario)
            messages.success(request, f'Scenario "{scenario.name}" created successfully!')
            return redirect('forecaster:scenario_detail', pk=scenario.pk)
    else:
        form = ScenarioForm()
    
    return render(request, 'forecaster/scenario_form.html', {'form': form, 'action': 'Create'})


@login_required
def scenario_detail(request, pk):
    """Display detailed scenario analysis with projections"""
    scenario = get_object_or_404(Scenario, pk=pk, user=request.user)
    snapshots = scenario.snapshots.all()
    
    context = {
        'scenario': scenario,
        'snapshots': snapshots,
    }
    return render(request, 'forecaster/scenario_detail.html', context)


@login_required
def scenario_update(request, pk):
    """Update an existing scenario"""
    scenario = get_object_or_404(Scenario, pk=pk, user=request.user)
    
    if request.method == 'POST':
        form = ScenarioForm(request.POST, instance=scenario)
        if form.is_valid():
            scenario = form.save()
            scenario.calculate_projection()
            # Clear old snapshots and regenerate
            scenario.snapshots.all().delete()
            generate_snapshots(scenario)
            messages.success(request, f'Scenario "{scenario.name}" updated successfully!')
            return redirect('forecaster:scenario_detail', pk=scenario.pk)
    else:
        form = ScenarioForm(instance=scenario)
    
    return render(request, 'forecaster/scenario_form.html', {
        'form': form,
        'action': 'Update',
        'scenario': scenario
    })


@login_required
def scenario_delete(request, pk):
    """Delete a scenario"""
    scenario = get_object_or_404(Scenario, pk=pk, user=request.user)
    
    if request.method == 'POST':
        name = scenario.name
        scenario.delete()
        messages.success(request, f'Scenario "{name}" deleted successfully!')
        return redirect('forecaster:scenario_list')
    
    return render(request, 'forecaster/scenario_confirm_delete.html', {'scenario': scenario})


@login_required
def scenario_compare(request):
    """Compare multiple scenarios side by side"""
    scenarios = Scenario.objects.filter(user=request.user)
    
    selected_ids = request.GET.getlist('scenarios')
    if selected_ids:
        selected_scenarios = scenarios.filter(id__in=selected_ids)
    else:
        # Default: show up to 3 most recent scenarios
        selected_scenarios = scenarios[:3]
    
    return render(request, 'forecaster/scenario_compare.html', {
        'all_scenarios': scenarios,
        'selected_scenarios': selected_scenarios,
    })


def generate_snapshots(scenario):
    """Generate yearly snapshots for a scenario"""
    P = float(scenario.initial_investment)
    PMT = float(scenario.monthly_contribution)
    r = float(scenario.annual_return_rate) / 100 / 12
    
    ScenarioSnapshot.objects.filter(scenario=scenario).delete()
    
    for year in range(1, scenario.investment_period_years + 1):
        n = year * 12
        
        if r == 0:
            value = P + (PMT * n)
        else:
            value = P * ((1 + r) ** n) + PMT * (((1 + r) ** n - 1) / r)
        
        contributions = P + (PMT * n)
        gains = value - contributions
        
        ScenarioSnapshot.objects.create(
            scenario=scenario,
            year=year,
            value=round(value, 2),
            contributions_to_date=round(contributions, 2),
            gains_to_date=round(gains, 2)
        )


# Alert Views
@login_required
def alert_list(request):
    """Display all alerts for the logged-in user"""
    alerts = Alert.objects.filter(user=request.user)
    notifications = Notification.objects.filter(user=request.user, is_read=False)[:10]
    
    return render(request, 'forecaster/alert_list.html', {
        'alerts': alerts,
        'notifications': notifications
    })


@login_required
def alert_create(request):
    """Create a new alert"""
    if request.method == 'POST':
        form = AlertForm(request.POST, user=request.user)
        if form.is_valid():
            alert = form.save(commit=False)
            alert.user = request.user
            alert.save()
            messages.success(request, f'Alert "{alert.name}" created successfully!')
            return redirect('forecaster:alert_list')
    else:
        form = AlertForm(user=request.user)
    
    return render(request, 'forecaster/alert_form.html', {'form': form, 'action': 'Create'})


@login_required
def alert_update(request, pk):
    """Update an existing alert"""
    alert = get_object_or_404(Alert, pk=pk, user=request.user)
    
    if request.method == 'POST':
        form = AlertForm(request.POST, instance=alert, user=request.user)
        if form.is_valid():
            alert = form.save()
            messages.success(request, f'Alert "{alert.name}" updated successfully!')
            return redirect('forecaster:alert_list')
    else:
        form = AlertForm(instance=alert, user=request.user)
    
    return render(request, 'forecaster/alert_form.html', {
        'form': form,
        'action': 'Update',
        'alert': alert
    })


@login_required
def alert_delete(request, pk):
    """Delete an alert"""
    alert = get_object_or_404(Alert, pk=pk, user=request.user)
    
    if request.method == 'POST':
        name = alert.name
        alert.delete()
        messages.success(request, f'Alert "{name}" deleted successfully!')
        return redirect('forecaster:alert_list')
    
    return render(request, 'forecaster/alert_confirm_delete.html', {'alert': alert})


@login_required
def alert_toggle(request, pk):
    """Toggle alert active/disabled status"""
    alert = get_object_or_404(Alert, pk=pk, user=request.user)
    
    if alert.status == 'active':
        alert.status = 'disabled'
        messages.info(request, f'Alert "{alert.name}" disabled.')
    elif alert.status == 'disabled':
        alert.status = 'active'
        alert.triggered_at = None
        messages.success(request, f'Alert "{alert.name}" activated.')
    
    alert.save()
    return redirect('forecaster:alert_list')


@login_required
def check_alerts(request):
    """Manually check all active alerts"""
    alerts = Alert.objects.filter(user=request.user, status='active')
    triggered_count = 0
    
    for alert in alerts:
        if alert.check_condition():
            # Trigger alert
            alert.status = 'triggered'
            alert.triggered_at = timezone.now()
            alert.save()
            
            # Create notification
            Notification.objects.create(
                user=request.user,
                alert=alert,
                scenario=alert.scenario,
                notification_type='alert',
                title=f'Alert Triggered: {alert.name}',
                message=alert.message
            )
            triggered_count += 1
    
    if triggered_count > 0:
        messages.success(request, f'{triggered_count} alert(s) triggered!')
    else:
        messages.info(request, 'No alerts triggered. All conditions are within normal ranges.')
    
    return redirect('forecaster:alert_list')


@login_required
def notification_list(request):
    """Display all notifications"""
    notifications = Notification.objects.filter(user=request.user)
    unread_count = notifications.filter(is_read=False).count()
    
    return render(request, 'forecaster/notification_list.html', {
        'notifications': notifications,
        'unread_count': unread_count
    })


@login_required
def notification_mark_read(request, pk):
    """Mark notification as read"""
    notification = get_object_or_404(Notification, pk=pk, user=request.user)
    notification.is_read = True
    notification.save()
    
    return redirect('forecaster:notification_list')


@login_required
def notification_mark_all_read(request):
    """Mark all notifications as read"""
    Notification.objects.filter(user=request.user, is_read=False).update(is_read=True)
    messages.success(request, 'All notifications marked as read.')
    return redirect('forecaster:notification_list')
