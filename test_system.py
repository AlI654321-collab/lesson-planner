"""
تست کامل سیستم تولید طرح درس
"""
import os
import sys

def check_python():
    """بررسی نسخه Python"""
    print("🐍 بررسی Python...")
    version = sys.version_info
    print(f"   نسخه: {version.major}.{version.minor}.{version.micro}")
    if version.major >= 3 and version.minor >= 7:
        print("   ✓ نسخه مناسب است")
        return True
    else:
        print("   ✗ نسخه Python باید 3.7 یا بالاتر باشد")
        return False

def check_libraries():
    """بررسی کتابخانه‌های مورد نیاز"""
    print("\n📚 بررسی کتابخانه‌ها...")
    
    required = {
        'flask': 'Flask',
        'google.generativeai': 'google-generativeai',
        'PyPDF2': 'PyPDF2',
        'docx': 'python-docx',
        'openpyxl': 'openpyxl',
        'markdown': 'markdown'
    }
    
    missing = []
    
    for module, package in required.items():
        try:
            __import__(module)
            print(f"   ✓ {package}")
        except ImportError:
            print(f"   ✗ {package} نصب نیست")
            missing.append(package)
    
    if missing:
        print(f"\n⚠️ کتابخانه‌های زیر نصب نیستند:")
        print(f"   pip install {' '.join(missing)}")
        return False
    
    return True

def check_api_key():
    """بررسی API Key"""
    print("\n🔑 بررسی API Key...")
    
    try:
        with open('app.py', 'r', encoding='utf-8') as f:
            content = f.read()
            
        if 'AIzaSy' in content:
            print("   ✓ API Key پیدا شد")
            
            # هشدار امنیتی
            if 'AIzaSyBTobLaZGosMgvrWDHporthVqo5_fKOqbM' in content:
                print("   ⚠️ توجه: API Key پیش‌فرض است")
                print("   💡 برای استفاده واقعی، API Key خود را جایگزین کنید")
            
            return True
        else:
            print("   ✗ API Key پیدا نشد")
            return False
    except Exception as e:
        print(f"   ✗ خطا: {e}")
        return False

def check_files():
    """بررسی فایل‌های مورد نیاز"""
    print("\n📁 بررسی فایل‌ها...")
    
    required_files = ['app.py', 'chatbot.html']
    
    all_exist = True
    for file in required_files:
        if os.path.exists(file):
            print(f"   ✓ {file}")
        else:
            print(f"   ✗ {file} پیدا نشد")
            all_exist = False
    
    return all_exist

def check_folders():
    """بررسی و ایجاد پوشه‌های مورد نیاز"""
    print("\n📂 بررسی پوشه‌ها...")
    
    if not os.path.exists('generated'):
        os.makedirs('generated')
        print("   ✓ پوشه generated ایجاد شد")
    else:
        print("   ✓ پوشه generated موجود است")
    
    return True

def test_pdf_library():
    """تست کتابخانه PDF"""
    print("\n📄 تست کتابخانه PDF...")
    
    try:
        import PyPDF2
        print("   ✓ PyPDF2 قابل استفاده است")
        return True
    except Exception as e:
        print(f"   ✗ خطا: {e}")
        return False

def test_ai_connection():
    """تست اتصال به Gemini AI"""
    print("\n🤖 تست اتصال به Gemini AI...")
    
    try:
        import google.generativeai as genai
        
        # خواندن API Key از فایل
        with open('app.py', 'r', encoding='utf-8') as f:
            content = f.read()
            
        import re
        match = re.search(r'API_KEY = ["\']([^"\']+)["\']', content)
        
        if not match:
            print("   ✗ API Key پیدا نشد")
            return False
        
        api_key = match.group(1)
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-2.0-flash')
        
        print("   ⏳ در حال ارسال درخواست تست...")
        response = model.generate_content("سلام، این یک تست است. فقط بگو: تست موفق")
        
        if response.text:
            print(f"   ✓ اتصال موفق - پاسخ: {response.text[:50]}")
            return True
        else:
            print("   ✗ پاسخ دریافت نشد")
            return False
            
    except Exception as e:
        print(f"   ✗ خطا: {e}")
        print("   💡 ممکن است API Key نامعتبر باشد")
        return False

def main():
    """اجرای تمام تست‌ها"""
    print("="*60)
    print("🧪 تست سیستم تولید طرح درس")
    print("="*60)
    
    results = []
    
    results.append(("Python", check_python()))
    results.append(("کتابخانه‌ها", check_libraries()))
    results.append(("API Key", check_api_key()))
    results.append(("فایل‌ها", check_files()))
    results.append(("پوشه‌ها", check_folders()))
    results.append(("کتابخانه PDF", test_pdf_library()))
    
    # تست اتصال AI فقط اگر همه چیز دیگر OK بود
    if all(r[1] for r in results):
        results.append(("اتصال AI", test_ai_connection()))
    
    print("\n" + "="*60)
    print("📊 خلاصه نتایج:")
    print("="*60)
    
    for name, status in results:
        icon = "✓" if status else "✗"
        print(f"   {icon} {name}")
    
    print("="*60)
    
    if all(r[1] for r in results):
        print("\n🎉 همه چیز آماده است!")
        print("💡 برای اجرا: python app.py")
    else:
        print("\n⚠️ برخی مشکلات وجود دارد")
        print("💡 لطفاً مشکلات بالا را برطرف کنید")

if __name__ == "__main__":
    main()
