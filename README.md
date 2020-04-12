
> Este proyecto fue hecho en el marco de [Hacktic](https://hackdash.org/projects/5e7e205a875b954b4a1d13de), una Hackaton dónde participan múltiples cooperativas de [Facttic](https://facttic.org.ar/)  
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](docs/code_of_conduct.md)



# FITness
Web platform developed to manage collaborative work opportunities between software development cooperatives.

This is a HackTic 2020 project by in which developers of cooperatives associated with FACTTIC participated.

## Goal
The main goal is to have a tool that facilitates the identification of available developers when a software development opportunity is brought to FIT by one of the cooperatives participating in it.

The expected workflow is to: create an opportunity > identify co-operatives that have developers available in the required technology > notify co-operatives that may come forward to take the opportunity.


## Setting up

### Backend

#### Pre-requisites
- Python 3.7 or later
- Pipenv

#### Start and configure local env
    $ pipenv shell
    $ pipenv install
    
#### Migrate models, create superuser and start server

    $ pipenv run python manage.py migrate
    $ pipenv run python manage.py createsuperuser
    $ pipenv run python manage.py runserver

## Using


## Running Frontend

1. Install node dependencies:

	      cd frontend && npm install && npm run build

2. Start the frontend app:
        
        cd frontend && npm run serve

3. App core and landing page should be accesible on:

        http://localhost:8080/