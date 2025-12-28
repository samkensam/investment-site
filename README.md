# Investment Forecaster 📈

> **🎯 Django Template Repository**
> 
> This is a ready-to-use template for building investment forecasting applications. Use it as a starting point for your own investment analysis and portfolio projection projects.

A Django-based web application for investment scenario analysis, portfolio projections, and automated alerts. Plan your financial future with interactive charts, ROI calculations, and smart notifications.

---

## 🚀 Using This Template

### Option 1: Use as GitHub Template
1. Click the "Use this template" button at the top of this repository
2. Create your new repository
3. Clone your new repository and follow the setup instructions below

### Option 2: Clone Directly
```bash
git clone https://github.com/samkensam/investment-site.git
cd investment-site
```

---

## 📋 Setup Instructions

Follow these steps to get the application running on your local machine:

### 1. Create Virtual Environment
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables
```bash
# Copy the example environment file
cp .env.example .env

# Edit .env and configure your settings:
# - Generate a new SECRET_KEY for production
# - Set DEBUG=False for production
# - Configure ALLOWED_HOSTS for your domain
# - Set up database credentials if using PostgreSQL
```

**Generate a new SECRET_KEY:**
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 4. Run Database Migrations
```bash
python manage.py migrate
```

### 5. Create Superuser Account
```bash
# Interactive method
python manage.py createsuperuser

# Or use the provided script (creates admin/admin123)
python create_superuser.py
```

### 6. Run Development Server
```bash
python manage.py runserver
```

### 7. Access the Application
- **Main Application**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/
- **Default Credentials** (if using create_superuser.py):
  - Username: `admin`
  - Password: `admin123`

---

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
│   ├── settings.py          # Django settings (with env var support)
│   ├── urls.py              # Root URL config
│   └── wsgi.py              # WSGI config
├── .env.example             # Environment variables template
├── .gitignore               # Git ignore rules
├── requirements.txt         # Python dependencies
├── create_superuser.py      # Helper script for creating admin user
├── manage.py                # Django CLI
└── README.md                # This file
```

## 🔧 Configuration

### Environment Variables (.env file)

The application uses environment variables for configuration. Copy `.env.example` to `.env` and customize:

**Development Settings** (default in .env.example):
```ini
SECRET_KEY=your-secret-key-here-change-this-in-production
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_ENGINE=django.db.backends.sqlite3
DATABASE_NAME=db.sqlite3
```

**Production Settings**:
```ini
SECRET_KEY=<generate-new-secret-key>
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

# PostgreSQL Database
DATABASE_ENGINE=django.db.backends.postgresql
DATABASE_NAME=your_db_name
DATABASE_USER=your_db_user
DATABASE_PASSWORD=your_db_password
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

> **💡 Tip**: Generate a secure SECRET_KEY with:
> ```bash
> python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
> ```

### Database Configuration

The project supports both SQLite (for development) and PostgreSQL (for production).

**SQLite** (default - no additional setup required):
```ini
DATABASE_ENGINE=django.db.backends.sqlite3
DATABASE_NAME=db.sqlite3
```

**PostgreSQL** (recommended for production):
1. Install PostgreSQL and create a database
2. Update `.env` file with PostgreSQL credentials:
```ini
DATABASE_ENGINE=django.db.backends.postgresql
DATABASE_NAME=your_database_name
DATABASE_USER=your_database_user
DATABASE_PASSWORD=your_database_password
DATABASE_HOST=localhost
DATABASE_PORT=5432
```
3. Install PostgreSQL driver: `pip install psycopg2-binary` (uncomment in requirements.txt)
4. Run migrations: `python manage.py migrate`

---

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

### Prerequisites for Production

1. **Uncomment production dependencies in `requirements.txt`**:
   - `psycopg2-binary` (PostgreSQL driver)
   - `gunicorn` (WSGI server)
   - `whitenoise` (static files)

2. **Set up environment variables** with production values

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
   heroku config:set SECRET_KEY='<your-generated-secret-key>'
   heroku config:set DEBUG=False
   heroku config:set ALLOWED_HOSTS='your-app-name.herokuapp.com'
   ```

5. **Create Procfile** (if not exists)
   ```
   web: gunicorn investment_site.wsgi
   ```

6. **Deploy**
   ```bash
   git push heroku main
   heroku run python manage.py migrate
   heroku run python manage.py createsuperuser
   ```

### Deploy to Railway/Render

Similar process:
1. Connect your GitHub repository
2. Set environment variables via platform dashboard
3. Configure build and start commands
4. Deploy automatically on git push

---

## 🔒 Security Notes

⚠️ **Important for Production**:

1. **Never commit sensitive data** - The `.env` file is in `.gitignore` to prevent accidental commits
2. **Generate a unique SECRET_KEY** - Don't use the default one in production
3. **Set DEBUG=False** - Debug mode exposes sensitive information
4. **Configure ALLOWED_HOSTS** - Restrict which domains can serve your app
5. **Use HTTPS** - Enable SSL/TLS for secure communication
6. **Use strong passwords** - Especially for admin accounts
7. **Keep dependencies updated** - Regularly update Django and other packages for security patches
8. **Review `.env.example`** - Make sure it doesn't contain real secrets

---

## 🤝 Contributing

This is a template repository, but contributions are welcome! 

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Contribution Guidelines

- Follow Django best practices
- Maintain backwards compatibility when possible
- Update documentation for new features
- Test your changes thoroughly
- Keep the template nature of the repository in mind

---

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

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👤 Author

**Sam Ken Sam**
- GitHub: [@samkensam](https://github.com/samkensam)
- Repository: [investment-site](https://github.com/samkensam/investment-site)

---

## 🙏 Acknowledgments

- Django Framework
- Bootstrap Team  
- Chart.js Contributors
- Django Community

---

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check existing documentation
- Review Django documentation

---

**🎯 This is a Template Repository**

Feel free to use this as a starting point for your own investment forecasting applications. Customize it, extend it, and make it your own!

**Built with ❤️ using Django**

*Last Updated: December 2024*
