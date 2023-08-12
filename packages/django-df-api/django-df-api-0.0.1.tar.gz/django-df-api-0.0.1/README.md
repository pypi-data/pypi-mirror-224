# Django DF API

Module for automatic including Djangoflow apps API to your project.

## Installation:

- Install the package

```
pip install django-df-api
```

- Add the package to your INSTALLED_APPS

```
INSTALLED_APPS = [
    ...
    'df_api',
    ...
]
```

- Add the package to your urls.py

```
urlpatterns = [
    ...
    path("api/v1/", include("df_api.urls")),
    ...
]
```
