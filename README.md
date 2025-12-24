# Investment Forecaster 📈

A Django-based web application for investment scenario analysis, portfolio projections, and automated alerts. Plan your financial future with interactive charts, ROI calculations, and smart notifications.

## ✨ Features

### 📊 Scenario Analysis
- Create multiple investment scenarios (Optimistic, Realistic, Pessimistic, Custom)
- Set initial investment amounts and monthly contributions
- Configure expected annual returns and investment time horizons
- Factor in inflation rates and volatility

### 📈 Interactive Projections
- Year-by-year portfolio growth breakdown
- Interactive Chart.js visualizations
- Total contributions vs. gains analysis
- ROI calculations and metrics
- Inflation-adjusted projections

### 🔔 Automatic Alerts
- **Milestone Alerts**: Get notified when portfolio reaches target values
- **ROI Target Alerts**: Track when returns hit percentage goals
- **Threshold Monitoring**: Monitor important value thresholds
- **Periodic Reminders**: Regular investment review notifications
- Email notification support (configurable)

### 📱 User-Friendly Interface
- Responsive Bootstrap 5 design
- Clean, modern UI with gradient accents
- Mobile-friendly navigation
- Real-time notification system
- Side-by-side scenario comparisons

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/samkensam/investment-site.git
   cd investment_site
   ```

2. **Create virtual environment**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install Django==4.2.27
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser**
   ```bash
   python manage.py createsuperuser
   # Or use the provided script:
   python create_superuser.py
   ```

6. **Start development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Main App: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/admin/

### Default Credentials
- **Username**: admin
- **Password**: admin123

## 📖 Usage Guide

### Creating a Scenario
1. Navigate to "Create Scenario" from the menu
2. Fill in the form:
   - **Scenario Name**: Descriptive name (e.g., "Retirement 2045")
   - **Scenario Type**: Optimistic/Realistic/Pessimistic/Custom
   - **Initial Investment**: Starting capital ($)
   - **Monthly Contribution**: Regular monthly deposits ($)
   - **Expected Annual Return**: Average yearly return rate (%)
   - **Investment Period**: Time horizon (years)
   - **Inflation Rate**: Expected annual inflation (%)
   - **Volatility**: Expected market volatility (%)
3. Click "Create Scenario" to save

### Viewing Projections
- Click "View Details" on any scenario
- See interactive growth chart
- Review year-by-year breakdown table
- Analyze ROI metrics and total gains

### Comparing Scenarios
1. Go to "Compare" in the navigation
2. Select multiple scenarios (Ctrl/Cmd + Click)
3. Click "Compare" to view side-by-side analysis
4. View overlaid growth chart

### Setting Up Alerts
1. Navigate to "Alerts" menu
2. Click "New Alert"
3. Configure alert parameters:
   - **Alert Name**: Descriptive identifier
   - **Alert Type**: Milestone/ROI/Threshold/Reminder
   - **Linked Scenario**: Specific scenario or leave empty for all
   - **Target Value**: Portfolio value goal ($)
   - **Target ROI**: Return percentage goal (%)
   - **Message**: Custom alert text
4. Click "Check Alerts Now" to manually trigger evaluation

### Managing Notifications
- View all notifications in "Notifications" menu
- Mark individual notifications as read
- Mark all as read with one click
- Notifications link back to related scenarios

## 🛠️ Technology Stack

- **Backend**: Django 4.2.27
- **Database**: SQLite (development) / PostgreSQL (production ready)
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Charts**: Chart.js
- **Icons**: Bootstrap Icons
- **Authentication**: Django Auth System

## 📁 Project Structure

```
investment_site/
├── forecaster/              # Main Django app
│   ├── migrations/          # Database migrations
│   ├── templates/           # HTML templates
│   │   ├── forecaster/      # App templates
│   │   └── registration/    # Auth templates
│   ├── models.py            # Data models
│   ├── views.py             # View logic
│   ├── forms.py             # Django forms
│   ├── urls.py              # URL routing
│   └── admin.py             # Admin configuration
├── investment_site/         # Project settings
│   ├── settings.py          # Django settings
│   ├── urls.py              # Root URL config
│   └── wsgi.py              # WSGI config
├── manage.py                # Django CLI
├── .gitignore               # Git ignore rules
└── README.md                # This file
```

## 🔧 Configuration

### Settings (investment_site/settings.py)

**Debug Mode** (Development only):
```python
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
```

**Production Settings**:
```python
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']
SECRET_KEY = os.environ.get('SECRET_KEY')
```

**Database Configuration**:
```python
# SQLite (default)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# PostgreSQL (production)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 📊 Mathematical Models

### Future Value Calculation
The app uses the compound interest formula with periodic contributions:

```
FV = P(1+r)^n + PMT * [((1+r)^n - 1) / r]

Where:
- FV = Future Value
- P = Initial Investment
- PMT = Monthly Contribution
- r = Monthly Interest Rate (annual rate / 12)
- n = Total number of months
```

### ROI Calculation
```
ROI = (Total Gains / Total Contributions) × 100%
```

## 🚢 Deployment

### Deploy to Heroku

1. **Install Heroku CLI and login**
   ```bash
   heroku login
   ```

2. **Create Heroku app**
   ```bash
   heroku create your-app-name
   ```

3. **Add PostgreSQL**
   ```bash
   heroku addons:create heroku-postgresql:mini
   ```

4. **Set environment variables**
   ```bash
   heroku config:set SECRET_KEY='your-secret-key'
   heroku config:set DEBUG=False
   ```

5. **Create Procfile**
   ```
   web: gunicorn investment_site.wsgi
   ```

6. **Add requirements.txt**
   ```
   Django==4.2.27
   gunicorn
   psycopg2-binary
   whitenoise
   ```

7. **Deploy**
   ```bash
   git push heroku main
   heroku run python manage.py migrate
   heroku run python manage.py createsuperuser
   ```

### Deploy to Railway/Render
Follow similar steps with platform-specific configurations.

## 🔒 Security Notes

⚠️ **Important for Production**:
- Change `SECRET_KEY` in settings.py
- Set `DEBUG = False`
- Configure `ALLOWED_HOSTS`
- Use environment variables for sensitive data
- Enable HTTPS
- Use strong passwords
- Regular security updates

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Future Enhancements

- [ ] Monte Carlo simulations for risk analysis
- [ ] Real-time market data integration
- [ ] PDF report generation
- [ ] CSV/Excel export functionality
- [ ] Email notification integration
- [ ] User registration and profiles
- [ ] Asset allocation calculator
- [ ] Tax implications calculator
- [ ] Multi-currency support
- [ ] Mobile app (React Native/Flutter)

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Sam Ken Sam**
- GitHub: [@samkensam](https://github.com/samkensam)
- Repository: [investment-site](https://github.com/samkensam/investment-site)

## 🙏 Acknowledgments

- Django Framework
- Bootstrap Team
- Chart.js Contributors
- Django Community

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check existing documentation
- Review Django documentation

---

**Built with ❤️ using Django**

*Last Updated: December 24, 2025*
