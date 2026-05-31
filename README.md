# Health Prediction Application

## Project Overview
A Django-based healthcare application that stores patient blood test information and predicts possible health risks using rule-based logic.

## Features
- Create patient records
- Read records
- Update records
- Delete records
- Automatic health prediction
- Validation checks
- Admin panel

## Tech Stack
- Python
- Django
- SQLite
- Bootstrap

## Prediction Logic
Prediction is generated using glucose, haemoglobin, and cholesterol values.

## Installation Steps

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
