
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

2. **Add the App**: 
Include 'simulateuser' in your INSTALLED_APPS setting.

    ```python
    INSTALLED_APPS = [
        ...
        'simulate_user',
        ...
    ]
    ```

3. **Add the URLs**:
Ensure that you add the app's URL configurations to your project's urls.py:

    ```python
    urlpatterns = [
        ...
        path('simulate_user/', include('simulate_user.urls')),
        ...
    ]
    ```

4. **Middleware and Context Manager**:
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

5. **Database Migrations**:
After integrating the app, run:

    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

## Usage
- **Extend the Simulated User Base Template**:
In order to make use of the Simulate User features, you must decide which pages on your website should have the Simulate User UI on it. Any page that you want to be able to be viewed in a simulated session should be extending the simulate_user_base.html template
    ```html
    {% extends 'simulate_user/simulate_user_base.html' %}

    {% block headtitle %}
        My App Title
    {% endblock %}
    {% block extrahead %}
        Extra Head Content
    {% endblock %}
    
    {% block maincontent %}
        Actual Content
    {% endblock %}
    ```
- **Simulate User and Session Data**:
The Simulate User app, when set to do so will automatically set the request.user to be an authenticated version of the user you are simulating. Or if you chose unauthenticated, it will simulate request.user as an unauthenticated user.
The app will also create an entirely separate session for the simulated user. When you access request.session of a simulated session, it will be the session of the simulated user and not the real user. You will always be able to access the real user by referencing request.real_user.
The Simulate User app can switch back to the user's real session and real user data by the user disabling the simulation in their UI or by logging out. Simulated session will also expire at a set time (by default 3600 seconds).

- **Simulate User Logs**:
For the purposes of ensuring the security and safety of your users. Superusers are able to see in their Django Admin Site a log of all simulated sessions and all actions taken while in simulation. Please be aware that these logs are set to delete after a set amount of time (by default 14 days) in order to ensure that they do not take up too much space in your database.

- **Simulate User Notifications**:
Simulate User is set to notify users by email when someone uses the Simulate User feature to simulate their account. This is meant to ensure transparency for your users. The default templates for these emails can be overwritten. Please read more about overwriting templates in Django documentation for more details.

- **Set Certain Information as Private**:
While in simulation mode, it might be the case that certain information is deemed private and only for the real user to see. When encountering such cases, you can make use of the private tags to ensure that private information is only seen by the real user.
    ```html
    <p>{% private 'Some Content that should be private' %}</p>
    ```
    ```html
    {% privateblock %}
    <p>Some Content that should be private</p>
    <p>Some Content that should be private</p>
    <p>Some Content that should be private</p>
    {% endprivateblock %}
    ```

## Configuration
Simulate User has many different settings that you can control to ensure that your Simulate User experience is exactly the solution your project needs.

- **Enable or Disable Simulate User**: 
By default, Simulate User is enabled. This means that the UI and entire feature set supplied by the Simulate User is working as designed. However, you can disable it. To disable Simulate User, you simply need to have the following line in your settings file and set it to False.
We highly recommend against leaving Simulate User enabled in production.
    ```python
    ENABLE_SIMULATE_USER: bool = True
    ```
  
- **Enable or Disable Simulate User Notifications**: 
By default, Simulate User Notifications are enabled. This means that Simulate User will notify an end user when they are being simulated. This can be toggled with the following setting but is highly recommended against for security purposes.
    ```python
    ENABLE_SIMULATE_USER_NOTIFICATIONS: bool = True
    ```
  
- **Set Authentication Backend**:
If you use an authentication backend other than the default backend, you should alter the simulate user backend with the path for the one that it should use. By default, it is set to use the django default authentication backend. However, if you use different backends, it might be necessary to make Simulate User use the correct one.
    ```python
    SIMULATE_USER_AUTHENTICATION_BACKEND: str = 'django.contrib.auth.backends.ModelBackend'
    ```
  
- **Restrict Actions of Staff Members in Simulation Mode**:
By default, Simulate User only allows GET and HEAD requests to be done in simulation mode. This is for security and safety purposes. However, you can change this by toggling the setting:
    ```python
    ONLY_ALLOW_SIMULATED_GET_AND_HEAD_REQUESTS: bool = True
    ```
  
- **Set Custom Private Replacement Text**:
By default, Simulate User replaces all text in private tags with 'HIDDEN FOR USER PRIVACY PURPOSES'. However, you can change that using the following setting:
    ```python
    PRIVATE_CONTENT_REPLACEMENT: str = 'HIDDEN FOR USER PRIVACY PURPOSES'
    ```
  
- **Set Custom Session Settings**:
By default, Simulate User sets all simulated sessions to last for a maximum of 3600 seconds. It also automatically deletes all simulated sessions and simulated session actions after 14 days. You can toggle those settings as follows:
    ```python
    SIMULATED_SESSION_EXPIRY: int = 3600
    SIMULATED_SESSION_RETENTION: int =  14
    ```

- **Set Who Can See and Use Simulated User**:
By default, Simulate User is set to be enabled for all users who have the is_staff attribute as True. However, you can change this by using any bool attribute of your user model. You can create your own for maximum integration. You can toggle the following setting:
    ```python
    SIMULATED_USER_CONTROL_CONDITION: str = 'is_staff'
    ```
  
- **Set Who Can Simulate Which Users**:
By default, Simulate User is set to allow all staff members to simulate all users. However, you can customize this and make any users be able to simulate any users. This setting works based on attributes and it works in order lists. Simulate user will look for the setting SIMULATE_USER_PERMISSIONS and will go through it in order. This setting should contain a list of dictionaries. Each dictionary should contain two key, value pairs. The first key value pair should be SIMULATED_USER_ATTRIBUTE and a bool attribute in your user model. the second pair should be REAL_USER_ATTRIBUTE and a bool attribute of your user model. When checking if a user has permissions to simulate any given user, simulate user will go through the list and find the first simulated_user_attribute that the simulated user meets as true and then it will check the real user attribute for that setting for the real user and if it returns as true, permission will be granted, otherwise it will be denied.:
    ```python
    SIMULATE_USER_PERMISSIONS: list[dict[str, str]] = [
        {"SIMULATED_USER_ATTRIBUTE": "is_active", "REAL_USER_ATTRIBUTE": "is_staff"}
    ]    
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

