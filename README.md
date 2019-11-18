# todo-back

### pip install

```bash
$ pip install djangorestframework

$ pip install djangorestframework-jwt

$ pip install django-cors-headers
```

### Django rest framework

- Read installation of https://www.django-rest-framework.org/

```python
# settings.py
INSTALLED_APPS = [
    'rest_framework',
]

# urls.py
urlpatterns = [
    path('api-auth/', include('rest_framework.urls'))
]
```

### Django rest framework JWT

- Read https://jpadilla.github.io/django-rest-framework-jwt/

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

# urls.py
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('api-token-auth/', obtain_jwt_token),
]
```

> add additional settings for add settings

### Django CORS

- Read https://pypi.org/project/django-cors-headers/

```python
# settings.py
INSTALLED_APPS = [
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # caution for order
]
```

> add configuration for white-list checking