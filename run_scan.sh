#!/bin/bash
set -euo pipefail

# ===== 設定 =====
TARGET="${TARGET:-127.0.0.1}"        # 環境変数 TARGET があればそれを使う
OUTPUT_DIR="${OUTPUT_DIR:-./reports}"
SCAN_NAME="${SCAN_NAME:-PushScan}"
TARGET_NAME="${TARGET_NAME:-GitHubScanTarget}"
CONFIG_NAME="${CONFIG_NAME:-Full and fast}"  # "Ultimate" は重いのでまずは通常版
# =================

mkdir -p "$OUTPUT_DIR"

echo "[*] Feed sync (may take long the first time)"
sudo greenbone-feed-sync --type all

echo "[*] Ensure GVM is running"
sudo gvm-start || true
sleep 3

# gvm-cli を _gvm ユーザーで実行し、XMLを投げる関数
gmp() {
  local xml="$1"
  sudo -u _gvm gvm-cli socket \
    --gmp-username "${GMP_USER}" \
    --gmp-password "${GMP_PASSWORD}" \
    --xml "$xml"
}

# xmllint が無い場合は入れる（属性抽出に使う）
if ! command -v xmllint >/dev/null 2>&1; then
  echo "[*] Installing xmllint (libxml2-utils)"
  sudo apt-get update -y
  sudo apt-get install -y libxml2-utils
fi

# 1) Config（スキャン設定）のID取得
echo "[*] Resolving config id for name: ${CONFIG_NAME}"
CONFIG_XML="$(gmp "<get_configs/>")"
CONFIG_ID="$(echo "$CONFIG_XML" | xmllint --xpath \
  "string(//config[name[contains(., '${CONFIG_NAME}')]]/@id)" - 2>/dev/null || true)"
if [ -z "$CONFIG_ID" ]; then
  echo "[-] Could not find config named like '${CONFIG_NAME}'. Available names:"
  echo "$CONFIG_XML" | xmllint --xpath "//config/name/text()" - | tr ' ' '\n' | sed 's/^/  - /'
  exit 1
fi
echo "[+] CONFIG_ID=$CONFIG_ID"

# 2) 既存ターゲットを再利用 or 作成
echo "[*] Ensuring target exists for ${TARGET}"
TARGETS_XML="$(gmp "<get_targets/>")"
TARGET_ID="$(echo "$TARGETS_XML" | xmllint --xpath \
  "string(//target[name='${TARGET_NAME}' and hosts='${TARGET}']/@id)" - 2>/dev/null || true)"
if [ -z "$TARGET_ID" ]; then
  CREATE_TARGET_XML="$(gmp "<create_target><name>${TARGET_NAME}</name><hosts>${TARGET}</hosts></create_target>")"
  TARGET_ID="$(echo "$CREATE_TARGET_XML" | xmllint --xpath "string(//@id)" - 2>/dev/null)"
  echo "[+] Created target: $TARGET_ID"
else
  echo "[+] Reusing target: $TARGET_ID"
fi

# 3) タスク作成 or 取得
echo "[*] Ensuring task exists"
TASKS_XML="$(gmp "<get_tasks/>")"
TASK_ID="$(echo "$TASKS_XML" | xmllint --xpath \
  "string(//task[name='${SCAN_NAME}']/@id)" - 2>/dev/null || true)"
if [ -z "$TASK_ID" ]; then
  CREATE_TASK_XML="$(gmp "<create_task><name>${SCAN_NAME}</name><comment>Scan on push</comment><config id='${CONFIG_ID}'/><target id='${TARGET_ID}'/></create_task>")"
  TASK_ID="$(echo "$CREATE_TASK_XML" | xmllint --xpath "string(//@id)" - 2>/dev/null)"
  echo "[+] Created task: $TASK_ID"
else
  echo "[+] Reusing task: $TASK_ID"
fi

# 4) スキャン開始
echo "[*] Starting task..."
START_XML="$(gmp "<start_task task_id='${TASK_ID}'/>")"
REPORT_ID="$(echo "$START_XML" | xmllint --xpath \
  "string(//start_task/@report_id)" - 2>/dev/null || true)"
if [ -z "$REPORT_ID" ]; then
  echo "[-] Could not obtain report_id from start_task response:"
  echo "$START_XML"
  exit 1
fi
echo "[+] REPORT_ID=$REPORT_ID"

# 5) 完了待ちポーリング
echo "[*] Waiting for task to finish..."
for i in {1..120}; do  # 最大 ~20分 (10秒 * 120)
  STATUS_XML="$(gmp "<get_tasks task_id='${TASK_ID}' details='1'/>")"
  STATUS="$(echo "$STATUS_XML" | xmllint --xpath "string(//task/status/text())" - 2>/dev/null || true)"
  PROGRESS="$(echo "$STATUS_XML" | xmllint --xpath "string(//task/progress/text())" - 2>/dev/null || true)"
  echo "    status=${STATUS}, progress=${PROGRESS}%"
  if [ "$STATUS" = "Done" ]; then
    break
  fi
  sleep 10
done

# 6) PDF フォーマットIDを動的に取得
echo "[*] Resolving PDF report format id"
FORMATS_XML="$(gmp "<get_report_formats/>")"
PDF_FORMAT_ID="$(echo "$FORMATS_XML" | xmllint --xpath \
  "string(//report_format[name[contains(., 'PDF')]]/@id)" - 2>/dev/null || true)"
if [ -z "$PDF_FORMAT_ID" ]; then
  echo "[-] Could not find PDF report format. Available names:"
  echo "$FORMATS_XML" | xmllint --xpath "//report_format/name/text()" - | tr ' ' '\n' | sed 's/^/  - /'
  exit 1
fi
echo "[+] PDF_FORMAT_ID=$PDF_FORMAT_ID"

# 7) レポート取得（PDF）
PDF_PATH="${OUTPUT_DIR}/scan.pdf"
echo "[*] Exporting PDF to ${PDF_PATH}"
gmp "<get_reports report_id='${REPORT_ID}' format_id='${PDF_FORMAT_ID}' details='1'/>" \
  | tail -n +2 | base64 -d > "${PDF_PATH}" || {
    echo "[-] PDF export failed. Trying raw write..."
    gmp "<get_reports report_id='${REPORT_ID}' format_id='${PDF_FORMAT_ID}' details='1'/>" > "${OUTPUT_DIR}/scan.pdf.raw.xml"
    echo "Raw XML saved to ${OUTPUT_DIR}/scan.pdf.raw.xml"
    exit 1
  }

echo "[+] PDF saved: ${PDF_PATH}"