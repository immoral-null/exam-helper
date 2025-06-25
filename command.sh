#!/usr/bin/env sh

set -e

# 1. Setup folders as root
chown -R appuser:appuser .
mkdir -p answers screenshots summary
chmod -R 777 .

# 2. Drop privileges and run the Python app
exec su appuser -s /bin/sh -c "python3 -m main"
