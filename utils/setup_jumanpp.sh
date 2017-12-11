#!/usr/bin/env bash

curl -O http://nlp.ist.i.kyoto-u.ac.jp/nl-resource/knp/pyknp-0.3.tar.gz
tar xvf pyknp-0.3.tar.gz
cd pyknp-0.3
python setup.py install


function download_pykp() {
    curl -O http://nlp.ist.i.kyoto-u.ac.jp/nl-resource/knp/pyknp-0.3.tar.gz
}

function install() {
    tar xvf pyknp-0.3.tar.gz
    cd pyknp-0.3/
    python setup.py install
    cd ..
}

function clean() {
    echo "Cleaning..."
    rm -rf pyknp-0.3/
    rm pyknp-0.3.tar.gz
}

download_pykp
install
clean
