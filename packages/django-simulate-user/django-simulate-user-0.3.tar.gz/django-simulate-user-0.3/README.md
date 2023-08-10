
# SimulateUser Django App

## General Details

### Description

The SimulateUser Django app provides developers with a robust toolset to simulate user experiences within their web applications. By impersonating a specific user or even an anonymous user, developers can observe user experiences firsthand, enabling easier debugging, testing, and understanding of user interfaces and functionality.

### Features
 - **Private Tags Functionality**: Safeguard sensitive content in templates with `{% private %}` and `{% privateblock %}` tags.

 - **Fully Simulated Sessions**: Impersonate any user in the system, including anonymous users, with a complete session simulation.

 - **Transparency with Notifications & Logs**: Stay informed about all simulation activities through comprehensive notifications and logs.

 - **Customizable with Settings**: Tweak the app behavior according to project requirements. It's important to note that this app should not be used in production environments due to potential security concerns.

 - **Extendable Template with UI**: An aesthetically pleasing user interface for switching users is available in the simulate_user_base.html template, which can be extended by any template in your project.

## Setup Instructions
1. **Install the App**:
```
pip install django-simulate-user
```

1. **Add the App**: 
Include 'simulateuser' in your INSTALLED_APPS setting.

```python
INSTALLED_APPS = [
    ...
    'simulate_user',
    ...
]
```

2. **Add the URLs**:
Ensure that you add the app's URL configurations to your project's urls.py:

```python
urlpatterns = [
    ...
    path('simulate_user/', include('simulate_user.urls')),
    ...
]
```

3. **Middleware and Context Manager**:
Ensure you add the necessary middleware and context manager for the app in the respective Django settings:
```python
MIDDLEWARE = [
    ...
    'simulate_user.middleware.SimulateUserMiddleware',
    ...
]
```

```python
TEMPLATES = [
    {
        ...
        'OPTIONS': {
            'context_processors': [
                ...
                'simulate_user.context_processors.simulate_user_context', 
                ...
            ],
        },
        ...
    },
]
```

4. **Database Migrations**:
After integrating the app, run:

```
python manage.py makemigrations
python manage.py migrate
```

## Contributing
As this is an open-source project hosted on GitHub, your contributions and improvements are welcome! Follow these general steps for contributing:

1. **Fork the Repository**: 
Start by forking the main repository to your personal GitHub account.

2. **Clone the Forked Repository**: 
Clone your forked repository to your local machine.

```
git clone https://github.com/YidiSprei/SimulateUserProject.git
```

3. **Create a New Branch**: 
Before making any changes, create a new branch:

```
git checkout -b feature-name
```

4. **Make Your Changes**: 
Implement your features, enhancements, or bug fixes.

5. **Commit & Push**:

```
git add .
git commit -m "Descriptive commit message about changes"
git push origin feature-name
```
6. **Create a Pull Request (PR)**: 
Go to your forked repository on GitHub and click the "New Pull Request" button. Make sure the base fork is the original repository, and the head fork is your repository and branch. Fill out the PR template with the necessary details.

Remember to always be respectful and kind in all interactions with the community. It's all about learning, growing, and helping each other succeed!

## Credits
Developed with 💙 by Yidi Sprei. We thank all the contributors and the Django community for their support and inspiration.

