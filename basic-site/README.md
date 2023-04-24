# rudiweb-examples: Basic Site Demo

## Description

rudiweb site with a minimal setup.

Demonstrates:

* minimal setup
* serving a regular file: `/index.html`
* serving an executable file: `/thetimeis.html`, which is a symlink to `{site-root}/bin/thetimeis.sh`.

## Configuration

Configuration: [basic-site.yaml](basic-site.yaml).

Update `site-root` in `~/tmp/rudiweb-examples/basic-site/basic-site.yaml`.

## Run Server

Assumes rudiweb is installed at `~/tmp/rudiweb`.

```
cd
~/tmp/rudiweb/src/rudiweb.py ~/tmp/rudiweb-examples/basic-site/basic-site.yaml
```
