#!/bin/bash
set -ev

echo "Replacing snips-nlu-ffi url for local version"
perl -p -i -e \
    "s/^snips-nlu-ffi = .*\$/snips-nlu-ffi = { path = \"..\/..\/..\/ffi\" \}/g" \
    platforms/python/ffi/Cargo.toml
