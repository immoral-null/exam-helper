#!/bin/env bash

set -e
set -x

# 1. Setup folders as root
chown -R appuser:appuser .
mkdir -p answers screenshots summary
chmod -R 777 .

# 2. Drop privileges and run the Python app
exec su appuser -s /bin/bash -c "python3 -m main"

