#!/bin/bash

DataServer_DIR="./dataserver"

python3 -m grpc_tools.protoc \
    --proto_path="$DataServer_DIR" \
    --python_out="$DataServer_DIR" \
    --grpc_python_out="$DataServer_DIR" \
    "$DataServer_DIR"/dataserver.proto