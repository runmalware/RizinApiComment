# RizinApiComment
Inject Comment in Thai language to Translate short description of API Durin Reverse Engineer Task on Rizin
.
จากการใช้งาน Rizin ซึ่งเป็นเครื่องมือ Reverse Engineer ที่รองรับ Binary File ได้หลายรูปแบบ
แต่ผมมี scope ความสนใจไปที่ Windows PE Executble file เป็นหลัก
ก็เลยจะเน้นทำไปที่กลุ่มไฟล์เหล่านี้

แต่เนื่องจาก Windows เป็น API Based OS , ทุกๆ Process มักจะเรียกใช้ API เสมอ 
มือใหม่ Reverser แบบเรา ก็จะจำไม่ค่อยได้ หรือ "ไม่รู้" ว่า API นี้มีความหมายอะไร , มีลำดับเรียกตอนไหน หรือมันอันตรายอย่างไร อะไรมั้ย
ก็เลยพัฒนา Repo นี้ขึ้นมา แนวคิดคือ หากเจอ API (ซึ่งส่วนใหญ่จะถูก Call จาก Library ในไฟล์ .dll) ให้ทำการ Inject Comment ภาษาไทย
เข้าไปในเครื่องมือ Rizin 
เพราะว่า จะได้เห็นผลลัพธ์ที่หน้าจอตอน Reverse เลยว่า API นี้มีคำอธิบายว่าอะไร ภาษาไทยเน้นๆ

โดยใน Interface แบบ Command Line ล้วนของ Rizin ก็ต้องพึ่งพา Font Thai ที่เป็นรูปแบบ Monospace ด้วย จะได้แสดงผลได้เหมาะสมที่สุด กับ CLI นั่นเอง
ผมก็เลยแนบ SOV_Monomon เข้ามาใน repo ด้วย เพื่อที่จะได้ปรับ Shell ให้รองรับภาษาไทยจาก font นี้
ส่วนใครมีฟอนต์ภาษาไทยที่เป็น Monospace อื่นๆ แล้วอยากใช้ก็เต็มที่เลยครับ


## วิธีการใช้งาน
1. วางไฟล์ทั้งหมด ใน Directory เดียวกัน
2. ใช้ command : python3 rizin_API_Description_CommentInjectTH.py ไฟล์Malware.exe
3. API จะถูก ดึงออกมาอยู่ที่ไฟล์ pd_output.txt
4. และจะได้ไฟล์ comnent_inject_vX.rz มาซึ่งเป็นไฟล์ script ที่ใช้ใน rizin
5. เปิด rizin , ถ้าหากต้องการ inject ให้ทำการเพิ่ม comment file เข้าไปด้วยคำสั่งจุด . comment_inject_vX.rz
6. หลังจาก inject แล้ว จะมีคำอธิบายภาษาไทย ต่อท้าย API เพื่ออำนวยความสะดวกให้เราแปลผล
7. API ก็จะถูกแปลเรื่อยๆ ในไฟล์ api_comments_th.json นะครับ




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

