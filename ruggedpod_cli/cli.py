# RuggedPOD management API
#
# Copyright (C) 2015 Guillaume Giamarchi <guillaume.guillaume@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import click
from prettytable import PrettyTable


@click.group()
@click.option('--api-url', metavar='<url>', envvar='RUGGEDPOD_URL',
              help='RuggedPOD API base URL (env RUGGEDPOD_URL)', required=True)
@click.option('--username', metavar='<username>', envvar='RUGGEDPOD_USERNAME',
              help='RuggedPOD API username (env RUGGEDPOD_USERNAME)', required=True)
@click.option('--password', metavar='<password>', envvar='RUGGEDPOD_PASSWORD',
              help='RuggedPOD API password (env RUGGEDPOD_PASSWORD)', required=True)
@click.pass_context
def ruggedpod(ctx, api_url, username, password):
    """RuggedPOD command line interface"""
    pass


def main():
    ruggedpod(obj={})


if __name__ == '__main__':
    main()
