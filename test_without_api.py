"""
تست سیستم بدون نیاز به API
این اسکریپت فقط قسمت خواندن PDF را تست می‌کند
"""
import PyPDF2
import io
import os

def test_pdf_upload_simulation():
    """شبیه‌سازی آپلود و خواندن PDF"""
    print("="*60)
    print("🧪 تست خواندن PDF (بدون نیاز به API)")
    print("="*60)
    print()
    
    # درخواست مسیر فایل
    pdf_path = input("📁 مسیر فایل PDF را وارد کنید: ").strip('"')
    
    if not os.path.exists(pdf_path):
        print(f"❌ فایل پیدا نشد: {pdf_path}")
        return
    
    print()
    print("📚 در حال خواندن فایل...")
    print("-"*60)
    
    try:
        # خواندن فایل
        with open(pdf_path, 'rb') as file:
            pdf_data = file.read()
            pdf_file = io.BytesIO(pdf_data)
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            
            total_pages = len(pdf_reader.pages)
            print(f"✓ تعداد صفحات: {total_pages}")
            
            # خواندن تمام صفحات
            all_text = ""
            for i, page in enumerate(pdf_reader.pages):
                page_text = page.extract_text()
                if page_text:
                    all_text += page_text + "\n"
                
                if (i + 1) % 20 == 0:
                    print(f"  ⏳ خوانده شد: {i + 1}/{total_pages}")
            
            print(f"✓ کل محتوای خوانده شده: {len(all_text)} کاراکتر")
            print(f"✓ تعداد کلمات تقریبی: {len(all_text.split())}")
            
            # بررسی کیفیت
            print()
            print("-"*60)
            if len(all_text) < 100:
                print("⚠️ هشدار: محتوای خوانده شده خیلی کم است!")
                print("   احتمالاً PDF شامل تصاویر اسکن شده است")
                print("   💡 از OCR استفاده کنید یا فایل را به Word تبدیل کنید")
            else:
                print("✅ محتوا با موفقیت خوانده شد!")
                print()
                print("📄 نمونه محتوا (500 کاراکتر اول):")
                print("-"*60)
                print(all_text[:500])
                print("-"*60)
                
                # شبیه‌سازی تحلیل
                print()
                print("🔍 تحلیل خودکار محتوا:")
                print("-"*60)
                
                # استخراج اطلاعات ساده
                lines = all_text.split('\n')
                non_empty_lines = [l.strip() for l in lines if l.strip()]
                
                print(f"✓ تعداد خطوط: {len(non_empty_lines)}")
                print(f"✓ اولین خط: {non_empty_lines[0] if non_empty_lines else 'خالی'}")
                
                # جستجوی کلمات کلیدی
                keywords = ['فصل', 'درس', 'پایه', 'ریاضی', 'علوم', 'فارسی', 'انگلیسی']
                found_keywords = [kw for kw in keywords if kw in all_text]
                
                if found_keywords:
                    print(f"✓ کلمات کلیدی یافت شده: {', '.join(found_keywords)}")
                
                print()
                print("="*60)
                print("✅ تست موفقیت‌آمیز بود!")
                print()
                print("💡 برای استفاده کامل:")
                print("   1. API Key معتبر دریافت کنید")
                print("   2. در فایل app.py جایگزین کنید")
                print("   3. سرور را اجرا کنید: python app.py")
                print("="*60)
                
    except Exception as e:
        print(f"❌ خطا: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_pdf_upload_simulation()
    print()
    input("Press Enter to exit...")
