### Overview

API endpoint for the Runtime team to track active hours spent on each support case. [Link to instructions.](https://gist.github.com/jkvor/bfffcd67c08f211738626cc58dfbc3ac)

### Tech Stack

* [flask](http://flask.pocoo.org/)
* [flask-restful](https://flask-restful.readthedocs.io/en/0.3.5/index.html)

### Requirements

- Python 2.7.x (with pip)
- virtualenv (`sudo easy_install virtualenv`)

### Initial Setup/Running the app
Clone the project, and `cd` to the folder `cd runtime-project-frances`

```shell
git clone https://github.com/heroku/runtime-project-frances.git
```

1. Create a virtual env for Python 

    ```Shell
    virtualenv venv
    ```

2. Activate the virtual env

    ```Shell
    source venv/bin/activate
    ```

3. Install dependencies

    ```Shell
    pip install –r requirements.txt
    ```

4. To start the app

    ```shell
    python run.py
    ```

### Curl commands

For provided `input.json`

```shell
curl -X POST http://localhost:8080/cases -H "Content-Type: application/json" -d @input.json
```


### Other

[Wakatime](https://wakatime.com/@kawaiiru/projects/nolnmbxtji?start=2017-10-12&end=2017-10-18) - Time spent actively coding
