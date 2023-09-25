
<h1 align="center">Hi 👋, I'm sathyaseelan</h1>
<h3 align="center">A passionate developer from India</h3>
<hr>


# TODO Web Application

This is a simple web application for managing your tasks. It's built using Django and Python, with PostgreSQL as the database.
<h3>Technologies used:</h3>
<ul>
 <li>Django</li>
 <li>HTML</li>
 <li>PostgreSQL</li>
</ul>
<hr>


## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
<hr>

## Installation

Before you can run this project, you need to set up PostgreSQL and configure it in the Django settings.

### PostgreSQL Installation

1. **Install PostgreSQL**: Download and install PostgreSQL from the official website: [PostgreSQL Downloads](https://www.postgresql.org/download/).

2. **Create a Database**: Open the PostgreSQL command line or a GUI tool like pgAdmin and create a new database for your project.

### Django Database Configuration

1. **Clone the Repository**: Clone this repository to your local machine:

   ```bash
   git clone https://github.com/SATHYASEELAN-S/todo-webapplication.git

2. **Install Dependencies**: Install the required Python packages using pip:
 
   ```bash
   pip install -r requirements.txt

3. **Database Configuration**: Open the settings.py file in the todo app folder and configure the database settings. Update the DATABASES section with your PostgreSQL database information:

   ```bash
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',  # or your database host
        'PORT': '5432',       # or your database port
       }
   }

4. **Migrate Database**: Run the following command to create the database tables:

    ```bash
    python manage.py migrate

5. **Create a Superuser**: Create an admin superuser to manage the application:
 
   ```bash
   python manage.py createsuperuser

6. **Run the Application**: Start the development server:

   ```bash
   python manage.py runserver

7. **Access the Application**: Open your web browser and go to http://localhost:8000/ to access the TODO web application. 

   Now, your installation section provides a step-by-step guide for setting up and running your "TODO Web Application."
<hr>   

## Usage

- **Login**: Access the application and log in with the superuser credentials created during setup.

- **Tasks**: Add your tasks to the task field and mark them as completed or not in the "Completed" section.

- **Manage Tasks**: Use the application to manage your tasks, mark them as completed, and update task details.
<hr>

## Contributing

If you'd like to contribute to this project, we welcome your contributions to make it even better. Here's how you can get started:

1. **Fork the Repository**: Click the "Fork" button at the top right of this repository to create your own copy.

2. **Clone Your Fork**: Clone your forked repository to your local machine:

   ```bash
   git clone https://github.com/SATHYASEELAN-S/todo-webapplication.git

3. **Create a New Branch**: Create a new branch for your feature or bug fix:

    ```bash
    git checkout -b feature-name

4. **Make Your Changes**: Make the necessary changes and improvements to the project.

5. **Commit Your Changes**: Commit your changes with a clear and concise commit message: 

    ```bash
    git commit -m "Add feature-name"
    
6. **Push to Your Fork**: Push your changes to your forked repository on GitHub:

    ```bash
    git push origin feature-name
7. **Create a Pull Request**: Go to the main repository and click on the "New Pull Request" button. Provide a detailed description of your changes and submit the pull request.
   We appreciate your contributions and look forward to collaborating with you!

   ```vbnet
   Make sure to replace `your-username` with your GitHub username and `feature-name` with the name of your feature or bug fix branch. This section provides detailed guidance on how contributors can get involved    in the development process of your project.
<hr>

<h3 align="left">Connect with me:</h3>
<p align="left">
<a href="https://linkedin.com/in/sathyaseelans" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="sathyaseelans" height="30" width="40" /></a>
<a href="https://www.hackerrank.com/iamsathyaseelan3" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/hackerrank.svg" alt="iamsathyaseelan3" height="30" width="40" /></a>
<a href="https://www.leetcode.com/sathyaseelan_s" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/leet-code.svg" alt="sathyaseelan_s" height="30" width="40" /></a>
</p>

<h3 align="left">Languages and Tools:</h3>
<p align="left"> <a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="django" width="40" height="40"/> </a> <a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a> <a href="https://www.mysql.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg" alt="mysql" width="40" height="40"/> </a> <a href="https://www.oracle.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/oracle/oracle-original.svg" alt="oracle" width="40" height="40"/> </a> <a href="https://www.postgresql.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-original-wordmark.svg" alt="postgresql" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>

