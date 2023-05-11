## Dev environment setup
Clone this repo. With pip and pipenv installed, navigate to the root of the repo (`forge-artisan-workshop/`) and run: 
```
> pipenv install
```

### Enter the virtual environment
To run the server or tests, you need to be in the pipenv virtual environment (shell). Enter the shell by running:
```
> pipenv shell
```
You should only need to run this once per terminal session. (If you exit the shell, you'll need to run this to enter it again.)

To exit the shell:
```
> exit
```

### Run the server
While in the pipenv shell:
```
> uvicorn main:app --reload
```
- `--reload`: Reload the server after saving changes to any file (so you don't have to manually stop the server and start it again to see changes reflected)

### Run tests
While in the pipenv shell:
```
> pytest -f --color=yes
```
- `-f`: Rerun tests after saving changes to any file
- `--color=yes`: Color-code test output in terminal (i.e. green for pass, red for fail)

### Automatic API docs
With the server running, navigate here in your browser to view the automatic documentation for your API. You can use the Swagger UI to actually make requests to your endpoints to test them out.
- Swagger (interactive): http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Steps to recreate the initial app:
- Following FastAPI tutorial: https://fastapi.tiangolo.com/
- ...and pipenv tutorial: https://thoughtbot.com/blog/how-to-manage-your-python-projects-with-pipenv

With pip and pipenv installed:
```
> cd new-project-directory
> pipenv install
> pipenv install fastapi
> pipenv install 'uvicorn[standard]'
> pipenv install --dev pytest-xdist
```

Create `main.py` file with basics (given in tutorial).

## More resources
- pipenv with PyCharm: https://www.jetbrains.com/help/pycharm/pipenv.html
- pipenv tut with PC PowerShell instructions: https://thinkdiff.net/how-to-use-python-pipenv-in-mac-and-windows-1c6dc87b403e