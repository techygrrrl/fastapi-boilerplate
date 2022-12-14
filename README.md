# FastAPI Python example

## System Requirements

- Python 3.x (3.8 was used) should be available at either `python` or `python3`
- `pip` or `pip3`


### Virtual Env

Source the virtual env.

If you don't have a virtual env, create one:

    python -m venv env

#### Linux, macOS, WSL

    source env/bin/activate

#### Windows

    source env/Scripts/activate


## Dependencies

Install the dependencies:

    pip install -r requirements.txt

After installing new dependencies, you can update the file:

    pip freeze > requirements.txt


## Development Server

Run the development server with the following command:

    ./serve.sh

If the file is not executable, you may need to do the following command:

    chmod u+x serve.sh

## Endpoints

### GET /

You can get the health check endpoint at the root:

http://127.0.0.1:8000


### GET /todos/:todo_id?q=:query

Here's an example request to an endpoint that takes dynamic parameters:

http://127.0.0.1:8000/todo/1337?q=foobar

