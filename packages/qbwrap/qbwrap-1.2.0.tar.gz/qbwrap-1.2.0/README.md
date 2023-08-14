# QBwrap

Quick Bubblewrap chroot management tool.

## About

QBwrap is a tool that allows for quick bwrap chroot management with toml
configuration files.

### Sample

A sample QBwrap configuration file might look something like this:

```toml
[core]
location = "/chroots/my-chroot"
hostname = "test"
process = "bash -l"

[mount]
rw = [
    ["/chroots/my-chroot", "/"],
]
ro = [
    "/etc/resolv.conf",
]
dev = [
    "/dev",
]
proc = [
    "/proc",
]
tmpfs = [
    ["/dev/shm", {}],
    ["/tmp", {perms = "1777"}],
]
```

## Documentation

Documentation can either be built locally or browsed online on
[GitLab pages](https://xgqt.gitlab.io/xgqt-python-app-qbwrap/).

## Command-line interface

### Usage

```text
qbwrap [-h] [-V] [-q] [-f] [-r]
       [-R ROOT_METHOD] [-S DEV_SIZE] [-e EXECUTABLE] [-p PROCESS] [-m MERGE]
       [-P COLLECTION_PATH]
       [-c {default,always,never}]
       [--no-setup] [--force-setup]
       qbwrap_file
```

### Positional arguments

```text
  qbwrap_file           path to the QBwrap config file
```

### Options

```text
  -h, --help            show this help message and exit
  -V, --version         show program's version number and exit
  -q, --quiet           be quiet, limit information output
  -f, --fake            do not actually call bwrap
  -r, --root            call bwrap as root
  -R ROOT_METHOD, --root-method ROOT_METHOD
                        which method to use to become root
  -S DEV_SIZE, --dev-size DEV_SIZE
                        default size for special devices, eg. tmpfs
  -e EXECUTABLE, --executable EXECUTABLE
                        bubblewrap executable to call, defaults to "bwrap"
  -p PROCESS, --process PROCESS
                        override process command to start inside bwrap chroot
  -m MERGE, --merge MERGE
                        override any stanza of given QBwrap config
  -P COLLECTION_PATH, --collection-path COLLECTION_PATH
                        overwrite path of the QBwrap collection
  -c {default,always,never}, --use-collection {default,always,never}
                        whether and how to use the QBwrap collection
  --no-setup            do not run setup (from the setup stanza) even if required
  --force-setup         force to run setup defined in the setup stanza
```

## Installation

### PyPi

Available at [pypi.org/project/qbwrap](https://pypi.org/project/qbwrap/).

```shell
pip install --user --break-system-packages qbwrap
```

### Repository

See instructions in the
[xgqt-python-app-qbwrap](https://gitlab.com/xgqt/xgqt-python-app-qbwrap)
repository's
[README.md](https://gitlab.com/xgqt/xgqt-python-app-qbwrap/-/blob/master/README.md)
file.
