#!/bin/bash
# inject_comments_v4_fixed.sh
# Inject คอมเมนต์ลงบนตำแหน่งของ sym.imp.* โดยใช้ .realname จาก isj

if [ -z "$1" ]; then
  echo "Usage: $0 <target_exe>"
  exit 1
fi

TARGET=$1
DB="data/api_comments_th.json"
TMP_JSON="/tmp/symbols_v4_fixed.json"
TMP_RZ="/tmp/comment_inject_v4.rz"

if [ ! -f "$DB" ]; then
  echo "❌ ไม่พบไฟล์ฐานข้อมูล: $DB"
  exit 1
fi

echo "🔍 ดึง symbol ที่ import (.realname) จาก: $TARGET"
rizin -q -c "isj" "$TARGET" | jq -c '.[] | select(.is_imported == true) | {realname, vaddr}' > "$TMP_JSON"

TOTAL_API=$(wc -l < "$TMP_JSON")
echo "📦 พบ API (imported) ทั้งหมด: $TOTAL_API รายการ"

INJECTED=0
> "$TMP_RZ"

while IFS= read -r line; do
  API_NAME=$(echo "$line" | jq -r '.realname')
  API_ADDR=$(echo "$line" | jq -r '.vaddr')
  DESC=$(jq -r --arg key "$API_NAME" '.[$key] // empty' "$DB")

  if [ ! -z "$DESC" ]; then
    echo "✅ MATCH: $API_NAME → $DESC"
    echo "CCu $API_ADDR $API_NAME: $DESC" >> "$TMP_RZ"
    ((INJECTED++))
  else
    echo "⚠️  NO MATCH: $API_NAME"
  fi
done < "$TMP_JSON"

if [ $INJECTED -eq 0 ]; then
  echo "⚠️  ไม่พบ API ที่สามารถ inject ได้จากฐานข้อมูล"
else
  echo "🚀 Injecting $INJECTED คอมเมนต์ลงใน Rizin..."
  rizin -q -i "$TMP_RZ" "$TARGET"
  echo "✅ Inject เสร็จสิ้น: $INJECTED รายการ 🎉"
fi
