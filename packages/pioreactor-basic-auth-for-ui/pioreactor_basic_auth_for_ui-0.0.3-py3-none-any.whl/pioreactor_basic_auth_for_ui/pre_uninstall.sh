#!/bin/bash

set -x
set -e

export LC_ALL=C

sudo lighttpd-disable-mod basic-auth
sudo service lighttpd force-reload