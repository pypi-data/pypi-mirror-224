#!/bin/bash

set -x
set -e

export LC_ALL=C

# install tools
sudo apt-get install apache2-utils -y

# write a basic auth mod for lighttp
cat <<EOL | sudo tee /etc/lighttpd/conf-available/98-basic-auth.conf
server.modules += ("mod_auth", "mod_authn_file")
auth.backend = "htpasswd"
auth.backend.htpasswd.userfile = "/etc/lighttpd.user.htpasswd"
auth.require = ( "" => ("method" => "basic", "realm" => "example", "require" => "valid-user") )
EOL

# enable mod
sudo lighttpd-enable-mod basic-auth
