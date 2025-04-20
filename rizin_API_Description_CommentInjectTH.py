import re
import json

# โหลดไฟล์คำแปล API ภาษาไทย
with open("api_comments_th.json", "r", encoding="utf-8") as f:
    api_dict = json.load(f)

# โหลดผลลัพธ์ของ pd 10000~.dll ที่คุณเซฟเป็น pd_output.txt
with open("pd_output.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

comment_lines = []
pattern = re.compile(r"sym\.imp\.[\w\d]+\.dll_([\w\d]+)")

for line in lines:
    match = pattern.search(line)
    if match:
        api_name = match.group(1)
        if api_name in api_dict:
            addr_match = re.match(r"[│└┌ ]*\s*0x([0-9a-fA-F]+)", line)
            if addr_match:
                addr = int(addr_match.group(1), 16)
                comment = f"CCu {addr} {api_name}: {api_dict[api_name]}"
                comment_lines.append(comment)

# เขียนออกเป็นไฟล์ .rz สำหรับ rizin
with open("comment_inject_v8.rz", "w", encoding="utf-8") as f:
    f.write("\n".join(comment_lines))

print(f"✅ เขียนคอมเมนต์ทั้งหมด {len(comment_lines)} รายการ ไปยัง comment_inject_v8.rz แล้ว")
