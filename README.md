# RizinApiComment
Inject Comment in Thai language to Translate short description of API Durin Reverse Engineer Task on Rizin

from pathlib import Path

readme_path = Path("README.md")

readme_content = """\
# 🇹🇭 Rizin API Comment Injector (Thai)
**Inject คำอธิบายภาษาไทยเข้าไปในไฟล์ PE เพื่อช่วยวิเคราะห์ Reverse Engineering ด้วย Rizin CLI**

---

## 🔧 กลไกเบื้องต้นของโครงการนี้

เครื่องมือนี้ช่วยให้ reverser โดยเฉพาะผู้ใช้ชาวไทยสามารถ:
- เห็นความหมายของ API ที่เรียกใน `pdf`, `VV` ของ Rizin
- เข้าใจหน้าที่ของ API โดยไม่ต้องเปิด MSDN หรือหาคำอธิบาย
- Inject ข้อความภาษาไทยเป็นคอมเมนต์ลงใน Rizin ผ่าน `.rz` script

---

## 📁 หน้าที่ของแต่ละไฟล์

| ไฟล์ | หน้าที่ |
|------|---------|
| `api_comments_th.json` | ไฟล์ฐานข้อมูล: รายชื่อ Windows API และคำอธิบายเป็นภาษาไทย |
| `rizin_API_Description_CommentInjectTH.py` | สคริปต์หลัก: ประมวลผลและสร้างไฟล์ `.rz` สำหรับ inject comment |
| `comment_inject_vX.rz` | ไฟล์ผลลัพธ์: comment script ที่สามารถ load เข้า Rizin ได้โดยตรง |
| `pd_output.txt` _(optional)_ | ตัวอย่าง output ของคำสั่ง `pd 10000~.dll` สำหรับนำไปใช้ในการทดสอบ |
| `test_grab_apiname.py` | สคริปต์สำหรับตรวจสอบว่า API ใน sample มีอยู่ในฐานข้อมูลหรือไม่ |
| `inject_comments.sh` _(deprecated)_ | สคริปต์แบบ bash เดิม ใช้แทนด้วย Python script แล้ว |

> 🔸 สามารถใช้คำสั่ง `. ./comment_inject_vX.rz` เพื่อ load comment script ใน Rizin

---

## 📦 ตำแหน่งการวางไฟล์ และ permission

- วางทุกไฟล์ไว้ใน working directory เดียวกัน (ที่รัน Rizin CLI)
- ใช้ `chmod +x *.sh` หากจะเรียกใช้งานสคริปต์ bash
- ไฟล์ `.rz` ไม่ต้องตั้ง permission พิเศษ ใช้งานได้ทันทีผ่าน `rizin -c` หรือ `.`

---

## 💻 สภาพแวดล้อมที่เหมาะสม

- ✅ Ubuntu หรือ Kali Linux
- ✅ รองรับ WSL (Windows Subsystem for Linux)
- ✅ ใช้ Rizin CLI (`rizin`, `rizin -c`, `pd`, `VV`, `pdf`)
- ✅ ใช้ฟอนต์ monospace ที่แสดงภาษาไทยได้ เช่น `SOV_Monomon` (แนะนำสำหรับ Yakuake)

---

## ⚠️ ข้อจำกัด (Limitation)

| หัวข้อ | รายละเอียด |
|--------|-------------|
| **ครอบคลุม API** | ครอบคลุมเฉพาะ API ที่ถูกเรียกในโค้ด `.text` จริง ๆ เท่านั้น |
| **Dynamically Resolved API** | ยังไม่รองรับกรณี malware ใช้ `GetProcAddress`, `LoadLibrary` |
| **API ที่ import แต่ไม่ถูกเรียก** | จะไม่ถูก inject comment เพราะ `pd 10000~.dll` มองไม่เห็น |
| **Coverage** | การ disasm 10000 byte จาก `entry0` เหมาะสมกับ PE ส่วนใหญ่ |
| **Obfuscated Binary** | ยังไม่รองรับไฟล์ที่ obfuscate หรือ packed อย่างซับซ้อน |

> ❗หากต้องการ coverage เต็ม 100% ควรใช้ `ii` (import table) ควบคู่กับ `pd` แล้ว merge API แบบ dedup ภายหลัง

---

## 🤝 แนวทางการ contribute

### 📌 หากคุณต้องการช่วยเพิ่มฐานข้อมูล API:
1. แก้ไขหรือเพิ่ม entry ใน `api_comments_th.json`
   ```json
   {
     "WinExec": "เรียกโปรเซสใหม่จากคำสั่งแบบดั้งเดิม",
     "VirtualAlloc": "จองหน่วยความจำใน virtual memory"
   }

