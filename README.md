# pizzaria

Python Api Django Rest Framework

## Model realtionships in django rest framework

```
python.exe -m pip install --upgrade pip

pip install django django-restframework

```

## Create project

```
django-admin startproject core .

cd core
```

## Create app

```
python manage.py startapp api

```

## Relationship in django

1. One-to-many(ForeignKey)
1. One-to-one
1. Many-to-many

### In Django, we represent these relationship as fields on models using:

1. ForeignKey -> One-to-many relationship
1. OneToOneField -> One-to-one relationship
1. ManyToOneField -> Many-to-many relationship
