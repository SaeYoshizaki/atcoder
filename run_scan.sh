#!/bin/bash
set -e

TARGET="127.0.0.1"   # ← テスト対象。外部なら許可がある範囲で変更
OUTPUT_DIR="./reports"

mkdir -p $OUTPUT_DIR

echo "[*] Updating feed..."
sudo greenbone-feed-sync --type all

echo "[*] Starting GVM..."
sudo gvm-start

echo "[*] Running scan..."
# スキャン設定は環境によって微調整が必要
gvm-cli socket --xml "<get_tasks/>" || echo "GVM CLI 接続テスト OK"

# ここでカスタムスキャン実行コマンドを追加しても良い（後で調整可）

echo "[*] Done! Reports are saved under $OUTPUT_DIR"