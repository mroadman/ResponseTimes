# J4462 project template

As promised, I've put together a simple project template there that you can use to start your final projects.

Here's how it works:

Just as with the crime project before, begin by checking out the template from the repository. The PROJECT_NAME placeholder below should be replaced with the name of your specific project (it can be anything you want).

**git clone git://github.com/cjdd3b/j4462-project-template.git PROJECT_NAME**

Once you've done that, you'll need to do a few things to get everything up and running:

- First, you'll notice that your project folder is called "project" by default. Don't change it unless you know what you're doing -- a number of settings depend on it. If you want to change it for some reason, ask me and I'll explain how to make that work.

- Now open your settings file. Remember that the first thing we need to do when starting a new project is to set up our database. Your project is set up use SQLite, but you still need to add the name of your database to the NAME setting under DATABASES. Go ahead and name the database anything you want (it's called project.sqlite by default).

- If you remember way back to the beginning of our Django training, you'll remember that the first thing we have to do once we create
our database setting is sync the database. Go back to your project's base directory and type ```python manage.py syncdb``` to do that.

- You'll also remember that Django projects are composed of apps, which you'll need to create before you get started. To do that, navigate into the second level of your project directory (the place with settings.py, urls.py, etc.) and type ```django-admin.py startapp APP_NAME```, where APP_NAME is whatever you want to call your app. That's all you should need to get started.

The rest of your settings should work fine right out of the box. This approach should help alleviate some of the path and dependency issues some of you were having earlier in the semester. If you have any problems, let me know!