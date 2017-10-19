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

### Testing

**Paw**
[Screenshots](https://imgur.com/a/xK8lT)

**unittest**

```shell
python -m unittest test 
```
***
If I were to write tests for these, I'd have tests that check that the API portion of it works properly.
To test that, I'd first instantiate the app, then I'd pass a json to the '/cases' endpoint and then assert that the output is the expected. 

I would also write tests to test each helper method in cases. I would use unittest and create a nested case dictionary and assert all of the various probablities:

* changing from support to runtime, runtime to support
* runtime team member to runtime team member
* case open to pending or closed, pending to open or closed, or closed to open or pending

And various combinations of those. 

### Other

[Wakatime](https://wakatime.com/@kawaiiru/projects/nolnmbxtji?start=2017-10-12&end=2017-10-18) - Time spent actively coding
