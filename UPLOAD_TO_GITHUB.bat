@echo off
chcp 65001 >nul
echo ═══════════════════════════════════════════════════════════
echo 🚀 آپلود به GitHub
echo ═══════════════════════════════════════════════════════════
echo.

echo ⚠️ قبل از اجرا، مطمئن شو که:
echo    1. Git نصب کردی (https://git-scm.com)
echo    2. یک Repository در GitHub ساختی
echo    3. نام کاربری و Repository رو آماده داری
echo.
pause

echo.
echo 📝 لطفاً نام کاربری GitHub خودت رو وارد کن:
set /p USERNAME="نام کاربری: "

echo.
echo 📝 لطفاً نام Repository رو وارد کن (مثلاً lesson-planner):
set /p REPO="نام Repository: "

echo.
echo ═══════════════════════════════════════════════════════════
echo 🔄 در حال آماده‌سازی...
echo ═══════════════════════════════════════════════════════════

git init
if errorlevel 1 (
    echo ❌ خطا: Git نصب نیست! برو به https://git-scm.com و نصب کن
    pause
    exit /b 1
)

echo ✓ Git آماده شد

git add .
echo ✓ فایل‌ها اضافه شدند

git commit -m "اولین نسخه - طرح درس ساز"
echo ✓ Commit انجام شد

git branch -M main
echo ✓ Branch اصلی تنظیم شد

git remote add origin https://github.com/%USERNAME%/%REPO%.git
echo ✓ Remote اضافه شد

echo.
echo ═══════════════════════════════════════════════════════════
echo 📤 در حال آپلود به GitHub...
echo ═══════════════════════════════════════════════════════════
echo.
echo ⚠️ ممکنه از تو نام کاربری و رمز عبور بخواد
echo.

git push -u origin main

if errorlevel 1 (
    echo.
    echo ❌ خطا در آپلود!
    echo.
    echo راه‌حل‌های احتمالی:
    echo 1. مطمئن شو که Repository رو در GitHub ساختی
    echo 2. نام کاربری و Repository رو درست وارد کردی
    echo 3. اگه خطای authentication داد، از Personal Access Token استفاده کن
    echo    (Settings → Developer settings → Personal access tokens)
    echo.
    pause
    exit /b 1
)

echo.
echo ═══════════════════════════════════════════════════════════
echo ✅ موفقیت! کد به GitHub آپلود شد
echo ═══════════════════════════════════════════════════════════
echo.
echo 🔗 لینک Repository:
echo https://github.com/%USERNAME%/%REPO%
echo.
echo 📋 مرحله بعدی:
echo 1. برو به https://render.com
echo 2. با GitHub لاگین کن
echo 3. یک Web Service جدید بساز
echo 4. Repository خودت رو وصل کن
echo.
echo راهنمای کامل رو در فایل "راهنمای_آپلود.txt" بخون
echo.
pause
