import re
import json

# โหลดฐานข้อมูลคำแปล API ภาษาไทย
with open("api_comments_th.json", "r", encoding="utf-8") as f:
    api_dict = json.load(f)

# อ่าน output จาก pd ที่เก็บการเรียก API (ผ่าน sym.imp.*)
with open("pd_output.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

found_apis = set()

# regex: หา symbol เช่น sym.imp.KERNEL32.dll_CreateFileW
pattern = re.compile(r"sym\.imp\.[\w\d]+\.dll_([\w\d]+)")

for line in lines:
    match = pattern.search(line)
    if match:
        found_apis.add(match.group(1))

# ตรวจสอบว่าอันไหนยังไม่มีใน dict
missing_apis = sorted([api for api in found_apis if api not in api_dict])

# แสดงผล
print(f"📌 พบ API ที่ยังไม่มีคำแปลไทยในฐานข้อมูล ({len(missing_apis)} รายการ):")
for name in missing_apis:
    print(f"- {name}")
