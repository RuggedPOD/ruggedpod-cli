[![Build Status](https://api.travis-ci.org/RuggedPOD/ruggedpod-cli.png?branch=master)](https://travis-ci.org/RuggedPOD/ruggedpod-cli)

# CLI for RuggedPOD API

Command line interface for the RuggedPOD API

## Installation

```bash
$ pip install git+https://github.com/RuggedPOD/ruggedpod-cli
```

This python package adds the `ruggedpod` command to your system.

## Usage

The `ruggedpod` command allows you to call easily the RuggedPOD API
from a terminal.

```bash
$ ruggedpod --help

Usage: ruggedpod [OPTIONS] COMMAND [ARGS]...

  RuggedPOD command line interface

Options:
  --api-url <url>        RuggedPOD API base URL (env RUGGEDPOD_URL)
                         [required]
  --username <username>  RuggedPOD API username (env RUGGEDPOD_USERNAME)
                         [required]
  --password <password>  RuggedPOD API password (env RUGGEDPOD_PASSWORD)
                         [required]
  --debug                Trace HTTP requests and responses
  --help                 Show this message and exit.

Commands:
  blade-powerlong   Power button long press
  blade-powershort  Power button short press
  blade-reset       Reset button press
```

You need to set your credentials either on the command line or through
environment variables.

**On the command line**

```bash
$ ruggedpod --username admin --password password \
            --api-url https://ruggedpod-host/admin blade-powershort 2

+-------+-------------------+---------+
| Blade |       Action      |  Status |
+-------+-------------------+---------+
|   2   | Power short press | Success |
+-------+-------------------+---------+
```

**With environment variables**

```bash
$ export RUGGEDPOD_URL='https://ruggedpod-host/admin'
$ export RUGGEDPOD_USERNAME='admin'
$ export RUGGEDPOD_PASSWORD='password'
$
$ ruggedpod blade-reset --all

+-------+--------+---------+
| Blade | Action |  Status |
+-------+--------+---------+
|   1   | Reset  | Success |
|   3   | Reset  | Success |
|   2   | Reset  | Success |
|   4   | Reset  | Success |
+-------+--------+---------+
```

## License

See the LICENSE file for license rights and limitations (GPL v3).
