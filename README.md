# Multi-Organizational Management System

A Django web application that supports multiple organizations with role-based management.

## Features

- Main Organization management of sub-organizations
- Organization-specific user management
- Role-based access control
- Custom user model with organization affiliation
- Bootstrap-based responsive UI

## Setup Instructions

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Project Structure

- `core/`: Project settings and main URL configuration
- `organizations/`: Main application
  - `models.py`: Database models (Organization, User, Role)
  - `views.py`: View logic
  - `forms.py`: Form definitions
  - `urls.py`: URL routing
  - `admin.py`: Admin interface configuration
- `templates/`: HTML templates
  - `base.html`: Base template with common layout
  - `organizations/`: App-specific templates

## Initial Setup

1. Log in as superuser
2. Create the main organization (set is_main=True)
3. Create roles (Admin, Editor, Viewer)
4. Create sub-organizations
5. Create users and assign them to organizations and roles

## Security Features

- Organization-specific data isolation
- Role-based access control
- Permission checks for sensitive operations
- CSRF protection
- Secure password handling

## Notes

- Only the main organization's admin can create sub-organizations
- Organization admins can only manage users within their organization
- Users can only access data within their organization
- Role assignments are restricted to organization admins