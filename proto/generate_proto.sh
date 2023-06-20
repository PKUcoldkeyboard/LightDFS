#!/bin/bash

PROTO_DIR="."
OUT_DIR="./generated"

# 创建输出目录
mkdir -p "$OUT_DIR"

# 解析metaserver.proto、nameserver.proto、chunkserver.proto、raft.proto、replica.proto
for file in "$PROTO_DIR"/*.proto; do
  # 如果不是metaserver.proto、nameserver.proto、chunkserver.proto、raft.proto、replica.proto则跳过
  if [[ "$file" != "$PROTO_DIR/metaserver.proto" && "$file" != "$PROTO_DIR/nameserver.proto" && "$file" != "$PROTO_DIR/chunkserver.proto" && "$file" != "$PROTO_DIR/raft.proto" && "$file" != "$PROTO_DIR/replica.proto" ]]; then
    continue
  fi
  filename=$(basename "$file")
  filename_without_ext="${filename%.*}"

  # 生成对应的py文件到generated目录中
  python3 -m grpc_tools.protoc \
    --proto_path="$PROTO_DIR" \
    --python_out="$OUT_DIR" \
    --grpc_python_out="$OUT_DIR" \
    "$filename"
done
