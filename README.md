# Portfolio Python App using Django

## Introduction

This repository contains the code for a portfolio Python app developed using the Django framework. The app serves as a centralized platform for users to create and manage their portfolios, including personal information, contact details, and geographic location.

## Requirements

The following requirements must be met to successfully deploy the portfolio app:

- Django and Django REST Framework: Ensure you have Django installed on your system. You can find the official Django documentation [here](https://www.djangoproject.com/).

- PostgreSQL and PostGIS extension: The app utilizes PostgreSQL as the database backend. Install PostgreSQL and configure the database settings accordingly. With PostGIS, we can leverage a flexible solution built on top of an already robust open source database, PostgreSQL.

- Python 3: The app is developed using Python 3. Ensure you have a compatible Python version installed.

## Installation

Follow these steps to install and set up the portfolio app:

1. Clone the repository:

    `git@github.com:Qodestackr/gis_api_main.git`

2. Create a virtual environment:

   `python3 -m venv venv`

3. Activate the virtual environment:

   `source venv/bin/activate`

4. Install dependencies:

   Leverage `requirements.txt` file to quickly get started 

 
5. Create a superuser (for accessing the Django admin page and Django REST as well):

    `python manage.py createsuperuser`

6. Run the dev server
TIP: Check how Django works the magic when you fire up a dev server or uwsgi instance



The app will be accessible at http://localhost:8000/.

## Features

The portfolio Python app offers the following features:

**Extended User Profile:**
- The Django user module is extended to include additional details such as home address, phone number, and location (point geometry) where the user lives.

**User Profile and Edit Page:**
- Users can view their own profile page and edit their profile information using the edit page.

**Full-Screen Map:**
- The app includes a full-screen map displaying the locations of all registered users.

**User Icon Popup:**
- Clicking on a user icon (using the default icon) on the map will display a popup with the user's profile details.

Check React Client side work [here](https://github.com/Qodestackr/gis-portfolio-site)

**User Authentication and Authorization:**
- Users can log in from the default Django admin page.
- Users can only access their own profile page but not others.

(I took REST API way as a way to take time and play around with the tools,)

**Superuser Access:**
- Superusers can log in and access the Django admin page for all models.

# Coming Features

- **Unit tests**: Testing is a crucial part of software delivery and quality assurance. Modern Agile and DevOps teams have to iterate and build features quickly. As a developer myself, that is a bold claim but testing and automation helps us iterate quickly, break smalls and realized defects proactively. This goes a long way to product excellence, customer satisfaction, and long-term self(you or me) maintainability

- **Logging and Sentry**: Telemetry (Gathering data, metricsm Logs and so on): MELT(Metrics, Events, Log, Tracing)

- Feature rich spatial services to empower the frontend stacks: Continous improvement

- Automation: Scripts and Best Practices



# Known issues:
- Installation Quirk with Psycopg 3 and PostGIS Compatibility

To my advantage, I came across this short guide that provided clear insights into the specific problem and offered a quick tip on how to resolve it. Following the guide, I made the necessary adjustments to the installation procedure, ensuring that both the main package and the binary files of Psycopg 3 were installed.

STATUS: FIXED

Thanks to [this short guide](https://learndjango.com/tutorials/psycopg3-binary-and-django-42-installation-quick-t) 


# TL; DR:
To fully utilize Psycopg 3 and achieve PostGIS compatibility, ensure you install both the main package and the binary files. Psycopg 3 introduced a change where the binary files are now separated from the main package. Using commands like:
```bash
(.venv) $ python -m pip install psycopg==3.1.8
(.venv) $ python -m pip install psycopg-binary==3.1.8
```

- TypeError: Cannot set CustomUser SpatialProxy (POINT) with value of type: <class 'dict'>
 A common error that can keep occuring if models are not built with clarity. It seems to get triggered on mutations or operations that involves write. While not complex to understand it reassured me of how python can still be able to determine which version of a module to load for models involving spatial geometry or normal RDBMS related work.