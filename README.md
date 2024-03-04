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
- sheetjs-style 
- file-saver (save large file)

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

# Credits:
- export excel tool : https://blog.bitsrc.io/exporting-data-to-excel-with-react-6943d7775a92

# TO USE

## Install
- clone the repo
- move to the appropriate directory
## Frontend
- npm i
- navigate to search-tool/frontend/search-tool/src
- In the command line run <$ npm run dev>
## backend
- navigate to search-tool/backend/venv
- activate the environment <$ venv/Scripts/activate>
- May have to install Flask, Flask_cors, elasticSearch
- Create and add the provided file to the venv directory (file name elasticsearch_connection.py
- In te command line run <$ flask --app server run>
## Tailwind
-run npx tailwindcss -i ./src/index.css -o ./src/output.css --watch



