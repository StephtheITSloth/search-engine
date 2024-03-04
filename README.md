# search-tool-reorg


# Setup
## FRONTEND
### Create a react app with vite
- Install tailwind CSS and daisy UI pluggin.
- Add necessary configs to get the app running.
### TECHS:
- REACT
- TAILWIND CSS & DAISY UI: For style (use vite installation)
- FORMIK & YUP: Form handler and validation
- REACT QUERY: Request & Caching

## BACKEND
### Install a flask server 
- Create a virtual environment
- setup elasticsearch connection
- upload file to elasticsearch


# MVP & Technical Requirements
- user can enter doctorId in the search from
- user can download response file

# Improvements
- Need to run some end to end tests
- Find a better way to protect environments variables
- upload larger data (couldn't upload the data we wanted because of the 100MB limit on elasticsearch)

# TO USE

## Install
- clone the repo
- run npm i
## Frontend
- navigate to search-tool/frontend/search-tool/src
- In the command line run <$ npm run dev>
## backend
- navigate to search-tool/backend/venv
- In te command line run <$ flask --app server run>
## Tailwind
-run npx tailwindcss -i ./src/index.css -o ./src/output.css --watch



