## new project using pipenv:
- Following FastAPI tutorial: https://fastapi.tiangolo.com/
- ...and pipenv tutorial: https://thoughtbot.com/blog/how-to-manage-your-python-projects-with-pipenv

With pip and pipenv installed:
```
> cd new-project-directory
> pipenv install
> pipenv install fastapi
> pipenv install 'uvicorn[standard]'
```

Create `main.py` file with basics (given in tutorial).

### Run the server
```
> pipenv shell
> uvicorn main:app --reload
```

### Automatic API docs
- Swagger (interactive): http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## to clone repo:

Per tutorial above, simply `pipenv install` should work.

Found this alternative wisdom:

In general an environment image probably shouldn't be copied to github. You'll get a bunch of unneeded files which clogs your repo.

Instead you should create a requirements.txt from your existing environment pip freeze > requirements.txt and commit that file.

Then when someone else clones your repo they can set up a new virtual environment using any tool they want and run python -m pip install -r requirements.txt

That is, requirements.txt is like a recipe for how to create your environment. By providing the recipe users can use it any way they want.

## more resources
- pipenv with PyCharm: https://www.jetbrains.com/help/pycharm/pipenv.html
- pipenv tut with PC PowerShell instructions: https://thinkdiff.net/how-to-use-python-pipenv-in-mac-and-windows-1c6dc87b403e