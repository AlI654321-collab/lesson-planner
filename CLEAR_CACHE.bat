@echo off
chcp 65001 > nul
cls
echo.
echo ═══════════════════════════════════════════════════════════
echo 🔄 پاک کردن کش مرورگر
echo ═══════════════════════════════════════════════════════════
echo.
echo این اسکریپت کش مرورگرهای رایج را پاک می‌کند
echo.
echo ⚠️ توجه: مرورگرها باید بسته باشند
echo.
pause
echo.

echo 🌐 Chrome...
if exist "%LOCALAPPDATA%\Google\Chrome\User Data\Default\Cache" (
    rd /s /q "%LOCALAPPDATA%\Google\Chrome\User Data\Default\Cache" 2>nul
    echo   ✓ کش Chrome پاک شد
) else (
    echo   - Chrome یافت نشد
)

echo.
echo 🦊 Firefox...
if exist "%APPDATA%\Mozilla\Firefox\Profiles" (
    for /d %%i in ("%APPDATA%\Mozilla\Firefox\Profiles\*") do (
        if exist "%%i\cache2" rd /s /q "%%i\cache2" 2>nul
    )
    echo   ✓ کش Firefox پاک شد
) else (
    echo   - Firefox یافت نشد
)

echo.
echo 🌊 Edge...
if exist "%LOCALAPPDATA%\Microsoft\Edge\User Data\Default\Cache" (
    rd /s /q "%LOCALAPPDATA%\Microsoft\Edge\User Data\Default\Cache" 2>nul
    echo   ✓ کش Edge پاک شد
) else (
    echo   - Edge یافت نشد
)

echo.
echo ═══════════════════════════════════════════════════════════
echo ✅ تمام!
echo.
echo حالا:
echo 1. مرورگر را باز کنید
echo 2. به localhost:5000 بروید
echo 3. باید "نسخه 2.1 (با PDF)" را ببینید
echo 4. دکمه PDF باید نمایش داده شود
echo.
echo ═══════════════════════════════════════════════════════════
pause
