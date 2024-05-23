# TrueNAS Power Manager

This program aims to turn off an inactive TrueNAS instance, within certain hours. You'll be able to setup what hours would you like to check for inactivity, and it will stop the server if it's not running anything. You can run both locally and remote.

It was inspired on [Eric Kreuwels](https://gist.github.com/erkr)'s [TrueNAS Auto shutdown script](https://gist.github.com/erkr/843b9c7c2b6fa511c09a5773029c32e0), but using the TrueNAS API.


## Instructions with Docker (recommended)

For any of the following sections, you'll need [Docker](https://docs.docker.com/get-docker/) on your machine.

### Run

- Go to the `docker` directory and run `docker compose up -d`

> Note for developers: to try new code, remove the `-d` and add `--build`.

### Running the tests

If you'd like to run the test, you'll have to run the following command:

TODO


## Instructions for local

If you prefer to install the dependencies locally, follow this steps.

### Installing the dependencies

Run `python3 -m pip install -r requirements.txt`

### Run

Run `python3 src/__main__.py`. You can specify a custom path for the config file using `--config-path <new_path>`.