# -*- coding: utf-8 -*-
from __future__ import annotations

import subprocess

import click
from pioreactor.mureq import basic_auth


@click.command(name="change_ui_credentials")
@click.argument("username")
@click.argument("password")
def click_change_ui_credentials(username: str, password: str):
    """
    (leader only) Change the basic-auth creds for the UI
    """
    from shlex import quote

    # write to password file
    subprocess.run(
        f"sudo htpasswd -b -c /etc/lighttpd.user.htpasswd {quote(username)} {quote(password)}",
        shell=True,
    )

    # reboot lighttp server
    subprocess.run("sudo service lighttpd force-reload", shell=True)
    # print API key
    click.echo("Assign the following to field api_key under [ui_basic_auth] in your config.ini:")
    click.secho(basic_auth(username, password), bold=True)
    click.echo("It's recommended you restart the leader Pioreactor, too.")
