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

## Common operations

### Editing pages

After editing static pages from the CMS, export them them into fixtures using the following command:
```
./manage.py dumpdata --indent 2 pinax_pages >fixtures/pages.json
```
