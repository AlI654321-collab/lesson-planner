@echo off
chcp 65001 > nul
cls
echo.
echo ═══════════════════════════════════════════════════════════
echo 🎓 سیستم تولید طرح درس هوشمند
echo ═══════════════════════════════════════════════════════════
echo.
echo 💡 نسخه 2.0 - با رفع مشکلات
echo.
echo ═══════════════════════════════════════════════════════════
echo.

:menu
echo لطفاً یکی از گزینه‌ها را انتخاب کنید:
echo.
echo   1. اجرای سرور (استفاده عادی)
echo   2. تست کامل سیستم
echo   3. تست خواندن فایل PDF
echo   4. مشاهده راهنمای رفع مشکلات
echo   5. خروج
echo.
set /p choice="انتخاب شما (1-5): "

if "%choice%"=="1" goto run_server
if "%choice%"=="2" goto test_system
if "%choice%"=="3" goto test_pdf
if "%choice%"=="4" goto show_help
if "%choice%"=="5" goto end

echo.
echo ⚠️ انتخاب نامعتبر! لطفاً دوباره تلاش کنید.
echo.
goto menu

:run_server
cls
echo.
echo ═══════════════════════════════════════════════════════════
echo 🚀 در حال اجرای سرور...
echo ═══════════════════════════════════════════════════════════
echo.
echo 💡 پس از اجرا، مرورگر را باز کنید:
echo    http://localhost:5000
echo.
echo 💡 برای توقف سرور: Ctrl+C
echo.
echo ═══════════════════════════════════════════════════════════
echo.
python app.py
goto end

:test_system
cls
echo.
echo ═══════════════════════════════════════════════════════════
echo 🧪 تست کامل سیستم
echo ═══════════════════════════════════════════════════════════
echo.
python test_system.py
echo.
echo.
pause
cls
goto menu

:test_pdf
cls
echo.
echo ═══════════════════════════════════════════════════════════
echo 📄 تست خواندن فایل PDF
echo ═══════════════════════════════════════════════════════════
echo.
set /p pdf_path="مسیر فایل PDF را وارد کنید: "
echo.
python test_pdf_reading.py "%pdf_path%"
echo.
echo.
pause
cls
goto menu

:show_help
cls
echo.
type راهنمای_رفع_مشکلات.txt
echo.
echo.
pause
cls
goto menu

:end
echo.
echo 👋 خداحافظ!
echo.
