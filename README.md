# Project: TO-DO backend server

## RESTful API for django

> install

```bash
pip install djangorestframework
```

> core/settings.py

```python
INSTALLED_APPS = [
    'rest_framework',
]
```

> core/urls.py

```python
urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
]
```

## JWT

> install

```bash
pip install djangorestframework-simplejwt
```

> core/settings.py

```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}
```

> core/urls.py

```python
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('api-token-auth/', obtain_jwt_token),
]
```

## CORS

> install

```bash
pip install django-cors-headers
```

> core/settings.py

```python
INSTALLED_APPS = [
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
]
```

## CRUD with decorator

```python
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


@api_view(['GET', 'POST', 'PUT', 'DELETE', ])
@permission_classes((IsAuthenticated, ))
@authentication_classes((JSONWebTokenAuthentication, ))
def todo(request, todo_id):
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        pass
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
```
