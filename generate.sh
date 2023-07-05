#!/bin/bash

DataServer_DIR="./dataserver"
NameServer_DIR="./nameserver"

python3 -m grpc_tools.protoc \
    --proto_path="$DataServer_DIR" \
    --python_out="$DataServer_DIR" \
    --grpc_python_out="$DataServer_DIR" \
    "$DataServer_DIR"/dataserver.proto

python3 -m grpc_tools.protoc \
    --proto_path="$NameServer_DIR" \
    --python_out="$NameServer_DIR" \
    --grpc_python_out="$NameServer_DIR" \
    "$NameServer_DIR"/nameserver.proto

