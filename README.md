# ilpycon

## Getting Started

Make sure you are using a virtual environment of some sort (e.g. `virtualenv` or
`pyenv`).

```
npm install
pip install -r requirements.txt
./manage.py migrate
./manage.py loaddata sites conference sponsor_levels sponsor_benefits proposal_base pages
./manage.py sitetree_resync_apps ilpycon

npm run dev
```

Browse to http://localhost:3000/

## Deploy a branch to Heroku

- Use the `pycon.israel.devops@gmail.com` to add a Heroku collaborator account
- Install the Heroku CLI and login via `heroku login`
- `git push heroku $branch_name:master`, e.g. `git push heroku heroku-deploy:master`

## Configure the site to be ran behind a reverse proxy

To configure the project to be accessed via `/2018` rather than `/`:

Set the `FORCE_SCRIPT_NAME` env var:

```
heroku config:set FORCE_SCRIPT_NAME="/2018"
```

To configure the project for direct access, clear the `FORCE_SCRIPT_NAME` env var:

```
heroku config:remove FORCE_SCRIPT_NAME
```
