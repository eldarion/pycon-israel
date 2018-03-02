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

- Use the `pycon.israel.devops@gmail.com` account to add site collaborators
- Install the Heroku CLI and login via `heroku login`
- `git push heroku $branch_name:master`, e.g. `git push heroku heroku-deploy:master`

## Configure the site to be ran behind a reverse proxy

To run the site behind a reverse proxy, we need to:

- Set the proxy path via `settings.FORCE_SCRIPT_NAME`
- Update the `domain` of the current `contrib.sites.Site` model to include the proxy (since current_site.domain is used in Symposion templates to construct URLs)

### Setting the reverse proxy path
_e.g., configure the project to be accessed via `/2018-WIP` rather than `/`:_

1. Set the `FORCE_SCRIPT_NAME` env var:

```
heroku config:set FORCE_SCRIPT_NAME="/2018-WIP"
```

2. Run the `update_site_domain` management command:

```
heroku run python manage.py update_site_domain
```

3. Restart the web dyno(s) to pick up the change to Site.domain

```
heroku ps:restart web
```

### Updating the reverse proxy path
_e.g., configure the project to be accessed via `/2018` rather than `/2018-WIP`:_

1. Update the `FORCE_SCRIPT_NAME` env var:

```
heroku config:set FORCE_SCRIPT_NAME="/2018"
```

2. Run the `update_site_domain` management command:

```
heroku run python manage.py update_site_domain
```

3. Restart the web dyno(s) to pick up the change to Site.domain

```
heroku ps:restart web
```


### Clearing the reverse proxy path

1.  Clear the `FORCE_SCRIPT_NAME` env var:

```
heroku config:remove FORCE_SCRIPT_NAME
```

2. Run the `update_site_domain` management command:

```
heroku run python manage.py update_site_domain
```

3. Restart the web dyno(s) to pick up the change to Site.domain

```
heroku ps:restart web
```
