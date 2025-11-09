# راهنمای آپلود به Render.com

## مراحل آپلود:

### 1. آماده‌سازی GitHub
1. برو به [GitHub.com](https://github.com) و یک اکانت بساز (اگه نداری)
2. یک Repository جدید بساز (مثلاً `lesson-planner`)
3. کد رو آپلود کن:

```bash
cd lesson-planner
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/USERNAME/lesson-planner.git
git push -u origin main
```

### 2. آپلود به Render
1. برو به [Render.com](https://render.com)
2. ثبت‌نام کن (می‌تونی با GitHub لاگین کنی)
3. روی **"New +"** کلیک کن
4. **"Web Service"** رو انتخاب کن
5. Repository خودت رو وصل کن
6. تنظیمات:
   - **Name**: lesson-planner
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Plan**: Free

7. روی **"Create Web Service"** کلیک کن

### 3. منتظر بمون
- Render خودکار برنامه رو نصب و اجرا می‌کنه
- بعد از 2-3 دقیقه، لینک سایت آماده میشه
- مثلاً: `https://lesson-planner-xxxx.onrender.com`

## نکات مهم:

⚠️ **API Key امن نیست!**
- API Key تو کد هست، باید اون رو از کد حذف کنی
- بهتره از Environment Variables استفاده کنی

### برای امن کردن API Key:
1. تو Render، برو به **Environment**
2. یک متغیر جدید اضافه کن:
   - Key: `GEMINI_API_KEY`
   - Value: `AIzaSyCdRL9mQBAotXCLgyu_BNkaZVu_juL2yok`

3. تو `app.py` این خط رو تغییر بده:
```python
# قبل:
API_KEY = "AIzaSyCdRL9mQBAotXCLgyu_BNkaZVu_juL2yok"

# بعد:
import os
API_KEY = os.environ.get('GEMINI_API_KEY', 'YOUR_KEY_HERE')
```

## محدودیت‌های رایگان:
- 750 ساعت در ماه
- اگه 15 دقیقه استفاده نشه، خاموش میشه
- اولین بار که کسی میاد، 30 ثانیه طول می‌کشه تا روشن بشه

## مشکلات احتمالی:

### اگه خطای "Module not found" داد:
- چک کن که `requirements.txt` درست باشه
- Build logs رو بررسی کن

### اگه سایت باز نشد:
- چک کن که port درست باشه (Render خودش تنظیم می‌کنه)
- تو `app.py` این خط رو اضافه کن:
```python
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
```

## آلترناتیو‌های دیگه:
- **PythonAnywhere**: آسان‌تر ولی محدودیت بیشتر
- **Railway.app**: سریع‌تر ولی کمتر رایگان
- **Vercel**: برای Flask سخت‌تره

موفق باشی! 🚀
