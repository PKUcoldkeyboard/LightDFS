#!/bin/bash

PROTO_DIR="."
OUT_DIR="./generated"

# 创建输出目录
mkdir -p "$OUT_DIR"

for file in "$PROTO_DIR"/*.proto; do
  filename=$(basename "$file")
  filename_without_ext="${filename%.*}"

  # 生成对应的py文件到generated目录中
  python3 -m grpc_tools.protoc \
    --proto_path="$PROTO_DIR" \
    --python_out="$OUT_DIR" \
    --grpc_python_out="$OUT_DIR" \
    "$filename"
done
