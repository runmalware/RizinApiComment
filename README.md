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
2. ใช้ command ....................


---

## 🔧 กลไกเบื้องต้นของโครงการนี้


---

## 🤝 แนวทางการ contribute

### 📌 หากคุณต้องการช่วยเพิ่มฐานข้อมูล API:
1. แก้ไขหรือเพิ่ม entry ใน `api_comments_th.json`
   ```json
   {
     "WinExec": "เรียกโปรเซสใหม่จากคำสั่งแบบดั้งเดิม",
     "VirtualAlloc": "จองหน่วยความจำใน virtual memory"
   }

