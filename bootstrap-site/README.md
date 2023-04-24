# rudiweb: Bootstrap Site Demo

## Description

rudiweb with [Bootstrap](https://getbootstrap.com) and decorations.

Demonstrates:

* use of `/asis/*`
* use of bootstrap and bootstrap-icons
* bootstrap-based decorations (`top.html`, `bottom.html`, `navbar.html`, `footer.html`)
* use of `/.rudi/*` (refer to internals handling decorations)
* bootstrap-based html content (e.g., `/index.html`, `/about.html`)
* serving `/favicon.ico`
* serving directory views
* caching (see browser tools to view)

## Configuration

Configuration: [bootstrap-site.yaml](bootstrap-site.yaml).

Update `site-root` in `~/tmp/rudiweb-examples/bootstrap-site/bootstrap-site.yaml`.

Install bootstrap and bootstrap-icons:

```
cd ~/tmp/rudiweb-examples/bootstrap-site
./install-bootstrap.sh .
```

## Run Server

Assumes rudiweb is installed at `~/tmp/rudiweb`.

```
cd
~/tmp/rudiweb/src/rudiweb.py ~/tmp/rudiweb-examples/bootstrap-site/bootstrap-site.yaml
```
