# Investment Forecaster Template 📈

**A Django-based template repository for building investment scenario analysis and portfolio projection applications.**

> 🎯 **This is a template repository** – Use it to quickly start your own investment forecasting project with all the essential features pre-built and ready to customize!

## ✨ What's Included

This template provides a fully functional Django application with:

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

## 🚀 Quick Start Guide

### Prerequisites
- Python 3.9 or higher
- pip (Python package manager)
- Git

### Setup Instructions

1. **Use this template**
   
   Click the "Use this template" button on GitHub to create your own repository, or clone it directly:
   ```bash
   git clone https://github.com/samkensam/investment-site.git
   cd investment-site
   ```

2. **Create and activate virtual environment**
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
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   # Copy the example environment file
   cp .env.example .env
   
   # Edit .env and set your configuration
   # At minimum, generate a new SECRET_KEY for production:
   # python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
   ```

5. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser account**
   ```bash
   python manage.py createsuperuser
   # Or use the provided script:
   python create_superuser.py
   ```

7. **Start the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Main App: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/admin/

### Default Credentials (if using create_superuser.py)
- **Username**: admin
- **Password**: admin123

**⚠️ Important:** Change these credentials immediately for any production or public-facing deployment!

## 📖 How to Use

### Creating Investment Scenarios
1. Navigate to "Create Scenario" from the menu
2. Fill in the investment parameters:
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

\`\`\`
investment-site/
├── forecaster/              # Main Django app
│   ├── migrations/          # Database migrations
│   ├── templates/           # HTML templates
│   │   ├── forecaster/      # App templates
│   │   └── registration/    # Auth templates
│   ├── models.py            # Data models (Scenario, Alert, Notification)
│   ├── views.py             # View logic
│   ├── forms.py             # Django forms
│   ├── urls.py              # URL routing
│   └── admin.py             # Admin configuration
├── investment_site/         # Project settings
│   ├── settings.py          # Django settings (configured for env vars)
│   ├── urls.py              # Root URL config
│   └── wsgi.py              # WSGI config
├── .env.example             # Environment variable template
├── .gitignore               # Git ignore rules
├── requirements.txt         # Python dependencies
├── manage.py                # Django CLI
└── README.md                # This file
\`\`\`

## 🔧 Configuration

### Environment Variables

The application is configured to use environment variables for sensitive configuration. Copy \`.env.example\` to \`.env\` and customize:

\`\`\`bash
# Required Settings
SECRET_KEY=your-secret-key-here
DEBUG=True  # Set to False in production
ALLOWED_HOSTS=127.0.0.1,localhost

# Optional: Database (defaults to SQLite)
# DB_ENGINE=django.db.backends.postgresql
# DB_NAME=your_db_name
# DB_USER=your_db_user
# DB_PASSWORD=your_db_password
# DB_HOST=localhost
# DB_PORT=5432

# Optional: Email Configuration
# EMAIL_HOST=smtp.gmail.com
# EMAIL_PORT=587
# EMAIL_USE_TLS=True
# EMAIL_HOST_USER=your_email@gmail.com
# EMAIL_HOST_PASSWORD=your_app_password
\`\`\`

### Database Configuration

**Development (Default - SQLite):**
No additional configuration needed. SQLite database is created automatically.

**Production (PostgreSQL):**
1. Uncomment \`psycopg2-binary\` in \`requirements.txt\`
2. Install dependencies: \`pip install -r requirements.txt\`
3. Configure database settings in \`.env\`
4. Update \`settings.py\` DATABASES configuration if needed

## 📊 Mathematical Models

### Future Value Calculation
The app uses the compound interest formula with periodic contributions:

\`\`\`
FV = P(1+r)^n + PMT * [((1+r)^n - 1) / r]

Where:
- FV = Future Value
- P = Initial Investment
- PMT = Monthly Contribution
- r = Monthly Interest Rate (annual rate / 12)
- n = Total number of months
\`\`\`

### ROI Calculation
\`\`\`
ROI = (Total Gains / Total Contributions) × 100%
\`\`\`

## 🚢 Deployment

### Deploy to Heroku

1. **Install Heroku CLI and login**
   \`\`\`bash
   heroku login
   \`\`\`

2. **Create Heroku app**
   \`\`\`bash
   heroku create your-app-name
   \`\`\`

3. **Add PostgreSQL**
   \`\`\`bash
   heroku addons:create heroku-postgresql:mini
   \`\`\`

4. **Set environment variables**
   \`\`\`bash
   heroku config:set SECRET_KEY='your-secret-key'
   heroku config:set DEBUG=False
   \`\`\`

5. **Add production dependencies to requirements.txt**
   \`\`\`
   gunicorn
   psycopg2-binary
   whitenoise
   \`\`\`

6. **Create Procfile**
   \`\`\`
   web: gunicorn investment_site.wsgi
   \`\`\`

7. **Deploy**
   \`\`\`bash
   git push heroku main
   heroku run python manage.py migrate
   heroku run python manage.py createsuperuser
   \`\`\`

### Deploy to Railway/Render
Follow similar steps with platform-specific configurations.

## 🔒 Security Checklist

Before deploying to production:

- [ ] Generate a new \`SECRET_KEY\` (don't use the default!)
- [ ] Set \`DEBUG=False\` in \`.env\`
- [ ] Configure proper \`ALLOWED_HOSTS\` with your domain
- [ ] Use environment variables for all sensitive data
- [ ] Enable HTTPS (use your hosting provider's SSL certificate)
- [ ] Change default superuser credentials
- [ ] Keep Django and dependencies up to date
- [ ] Set up regular database backups
- [ ] Configure proper error logging
- [ ] Review and harden security settings in \`settings.py\`

## 🎨 Customization Ideas

Here are some ways you can customize this template for your specific needs:

- Add more investment scenario types
- Integrate real-time market data APIs
- Add PDF report generation
- Implement CSV/Excel export functionality
- Add user registration and profiles
- Create asset allocation calculators
- Add tax implications calculator
- Implement multi-currency support
- Add two-factor authentication
- Create mobile app companion

## 🤝 Contributing

Contributions are welcome! If you'd like to improve this template:

1. Fork the repository
2. Create a feature branch (\`git checkout -b feature/AmazingFeature\`)
3. Commit your changes (\`git commit -m 'Add AmazingFeature'\`)
4. Push to the branch (\`git push origin feature/AmazingFeature\`)
5. Open a Pull Request

## 📝 License

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
- Review Django documentation at https://docs.djangoproject.com/

---

**Built with ❤️ using Django**

*Happy Investing! 📈*
