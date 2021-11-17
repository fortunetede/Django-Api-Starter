
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/fortunetede/Django-Api-Starter">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center"> Django API Starter ( DAS.) </h3>

  <p align="center"> An awesome Open source project to fast track you new api base project </p>
</div>



<!-- Features -->
<details>
  <summary>Features</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#heres-why-django-api-starter-is-greate">Here's why Django Api Starter is Greate</a></li>
      </ul>
    </li>
    <li>
      <a href="#setup">Setup</a>
      <ul>
        <li><a href="#users-app-models">Clone project </a></li>
        <li><a href="#users-app-models">Project Structure</a></li>
        <li><a href="#users-app-models">Install Requirements</a></li>
        <li><a href="#users-app-models">Run Project</a></li>
      </ul>
    </li>
  </ol>
</details>

<br><br>
<!-- ABOUT THE PROJECT -->
## About The Project

<img src="images/logo.png" alt="Logo" width="80" height="80">
There are many great README templates available on GitHub; however, I didn't find one that really suited my needs so I created this enhanced one. I want to create a README template so amazing that it'll be the last one you ever need -- I think this is it.

##### Here's why Django Api Starter is Greate:
* Your time should be focused on creating something amazing. A project that solves a problem and helps others
* You shouldn't be doing the same tasks over and over like creating a README from scratch
* You should implement DRY principles to the rest of your life :smile:


<br><br>
<!-- SETUP -->
## SETUP

##### Clone project 
```object
git clone https://github.com/fortunetede/Django-Api-Starter.git
```

##### Project Structure
```
|-apps
    |-users
        |-admin.py
        |-apps.py
        |-models.py
        |-serializers.py
        |-urls.py
        |-views.py
|-project
    |-settings.py
    |-urls.py
    |-views.py
    |-wsgi.py
|-static
|-templates
    |-index.html
|-db.sqlites3
|-manage.py
|-Profile
|-requirements.txt
|-runtime.txt
```

##### Setup environment and Install Requirements
```python
# create a virtual environment

> pip3 install virtualenv

> virtualenv -p python3 venv

> source venv/bin/activate  

# New structure
|-django-api-starter
|-venv

> source venv/bin/activate
>(venv)
>cd django-api-starter
```
<a href="#project-structure">Project Structure </a>  
