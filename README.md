# Ten Thousand Project
”นโยบาย Digital wallet 10,000 บาท ใช้จ่ายในรัศมี 4 กม. บรรเทาปัญหาปากท้องและกระตุ้นเศรษฐกิจครั้งใหญ่“ คือคำกล่าวที่ทำให้พวกเราได้เกิดข้อสงสัยขึ้น ว่าในรัศมีที่ดังกล่าวมีร้านค้าอะไรบ้าง จึงเกิดเป็นโครงงานนี้ขึ้นมา

## Features
### Sign In / Sign Up
ระบบจดจำผู้ใช้งานและเก็บไว้ในฐานข้อมูล

### Location Selection
การระบุตำแหน่งผู้ใช้ทั้งที่อยู่ปัจจุบันและที่กำหนดเอง

### Pathfinding
แสดงแผ่นที่ร้านค้าพร้อมด้วยระบบนำทาง

### Profile
อัลกอริทึมที่คำนวณจำนวนเงินคงเหลือพร้อมทั้งประวัติการใช้งาน

## Backend
If you can't run you need to install Django and mysql. For Django, run:
```bash
pip install django
```

For MySQL, download MySQL and MySQL Workspace from the official website: 
https://dev.mysql.com/downloads/mysql/
https://dev.mysql.com/downloads/workbench/

Once that's done, run:
```bash
pip install mysql-connector-python
```

Then create setting.py in "Backend\tenthousand_project\tenthousand_project\settings.py" 
and api.py in "Backend\tenthousand_project\app_main_content\api.py"

Finally, to properly start the server, run the manage.py file in "Backend\tenthousand_project\":
```bash
python manage.py migrate
python manage.py runserver
```

If there are any issues, try installing mysql-connector-python and django again in a virtual environment.
```bash
# Create a new virtual environment
python -m venv env

# On Unix or MacOS
source env/bin/activate

# Activate the virtual environment
# On Windows
env\Scripts\activate
```