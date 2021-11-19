
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
  <summary>Context</summary>
  <ol>
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
# Create and Activate virtual environment

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


