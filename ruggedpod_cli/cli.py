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

from click import group, option, pass_context, argument, UsageError
from prettytable import PrettyTable

from client import RuggedPODClient


@group()
@option('--api-url', metavar='<url>', envvar='RUGGEDPOD_URL',
        help='RuggedPOD API base URL (env RUGGEDPOD_URL)', required=True)
@option('--username', metavar='<username>', envvar='RUGGEDPOD_USERNAME',
        help='RuggedPOD API username (env RUGGEDPOD_USERNAME)', required=True)
@option('--password', metavar='<password>', envvar='RUGGEDPOD_PASSWORD',
        help='RuggedPOD API password (env RUGGEDPOD_PASSWORD)', required=True)
@option('--debug', is_flag=True, help='Trace HTTP requests and responses')
@pass_context
def ruggedpod(ctx, api_url, username, password, debug):
    """RuggedPOD command line interface"""
    ctx.obj['api'] = RuggedPODClient(api_url, username, password, debug)


@ruggedpod.command(name='blade-powershort')
@argument('blade_number', metavar='<blade_number>', required=False)
@option('--all', is_flag=True, help='Do it on all blades')
@pass_context
def power_short_press(ctx, blade_number, all):
    """Power button short press"""
    _action(ctx, "Power short press", "SetBladeShortOnOff", "SetAllBladesShortOnOff", blade_number, all)


@ruggedpod.command(name='blade-powerlong')
@argument('blade_number', metavar='<blade_number>', required=False)
@option('--all', is_flag=True, help='Do it on all blades')
@pass_context
def power_long_press(ctx, blade_number, all):
    """Power button long press"""
    _action(ctx, "Power long press", "SetBladeLongOnOff", "SetAllBladesLongOnOff", blade_number, all)


@ruggedpod.command(name='blade-reset')
@argument('blade_number', metavar='<blade_number>', required=False)
@option('--all', is_flag=True, help='Do it on all blades')
@pass_context
def reset(ctx, blade_number, all):
    """Reset button press"""
    _action(ctx, "Reset", "SetBladeReset", "SetAllBladesReset", blade_number, all)


def _action(ctx, label, action, action_all, blade_number, all):
    if blade_number:
        _blade_action(ctx, label, action, blade_number)
    elif all:
        _all_blade_action(ctx, label, action_all)
    else:
        raise UsageError("Either a blade number or the --all option must be provided")


def _all_blade_action(ctx, label, action):
    blades = ctx.obj['api'].action(action)
    table = PrettyTable(["Blade", "Action", "Status"])
    for blade in blades:
        table.add_row([blade['bladeNumber'], label, blade['CompletionCode']])
    print table


def _blade_action(ctx, label, action, blade_number):
    blade = ctx.obj['api'].action(action, blade_number)
    table = PrettyTable(["Blade", "Action", "Status"])
    table.add_row([blade['bladeNumber'], label, blade['CompletionCode']])
    print table


def main():
    ruggedpod(obj={})


if __name__ == '__main__':
    main()
