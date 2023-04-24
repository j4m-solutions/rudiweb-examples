#! /bin/bash
#
# install-bootstrap.sh

print_usage() {
    progname=$(basename $0)
    echo "\
usage: ${progname} <siteroot>
       ${progname} -h|--help

Install bootstrap and bootstrap-icons under {siteroot}/html/asis."
}

while [ $# -gt 0 ]; do
    case $1 in
    -h|--help)
        print_usage
        exit 0
        ;;
    *)
        siteroot=$1; shift 1
        ;;
    esac
done

if [ "${siteroot}" = "" ]; then
    echo "error: bad/missing siteroot" 1>&2
    exit 1
fi

if [ ! -d "${siteroot}" ]; then
    echo "error: siteroot is missing or not a directory" 1>&2
    exit 1
fi

echo "preparing ..."
cd "${siteroot}"
mkdir -p html/asis

echo "installing bootstrap ..."
wget https://github.com/twbs/bootstrap/releases/download/v5.3.0-alpha3/bootstrap-5.3.0-alpha3-dist.zip

echo "unpacking bootstrap ..."
unzip bootstrap-5.3.0-alpha3-dist.zip

echo "setting up bootstrap ..."
mv bootstrap-5.3.0-alpha3-dist html/asis
(cd html/asis; ln -s bootstrap-5.3.0-alpha3-dist bootstrap)

echo "installing bootstrap-icons ..."
wget https://github.com/twbs/icons/releases/download/v1.10.4/bootstrap-icons-1.10.4.zip

echo "unpacking bootstrap-icons ..."
unzip bootstrap-icons-1.10.4

echo "setting up bootstrap-icons ..."
mv bootstrap-icons-1.10.4 html/asis
(cd html/asis; ln -s bootstrap-icons-1.10.4 bootstrap-icons)

echo "done"
