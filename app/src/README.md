# Usage tipps

## Dockerfile usage:
* if you want: uncomment and use the `--upgrade` flags for the pip install commands
* decide if you want to use the venv variant

## other
* `docker-compose run web <command>`, where `web` is the service name from `docker-compose.yaml`.
* to create a production-ready requirements.txt
  * `docker-compose run web bash -i`
  * `pip freeze > requirements.txt`
  * alternative: in docker container shell, run
    ```
    pip install pip-tools
    pip-compile  -n /requirements.txt > requirements.txt
    ```
  * this will create a requirements.txt with all packages in requiremnts.in, with their
    currently used version, and also adds their dependency packages with version
  * so its easier to create a reproduzible docker image
  * pip-compile should be run from the same virtual environment as your project so conditional dependencies that require a specific Python version, or other environment markers, resolve relative to your project's environment
  * see https://github.com/jazzband/pip-tools
* Using VENV in docker container (espeacially for prodction use): https://pythonspeed.com/articles/activate-virtualenv-dockerfile/