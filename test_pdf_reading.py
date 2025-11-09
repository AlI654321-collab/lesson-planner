"""
اسکریپت تست برای بررسی خواندن PDF
"""
import PyPDF2
import sys

def test_pdf_reading(pdf_path):
    """تست خواندن فایل PDF"""
    try:
        print(f"📚 در حال خواندن: {pdf_path}")
        print("="*60)
        
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            
            total_pages = len(pdf_reader.pages)
            print(f"✓ تعداد صفحات: {total_pages}")
            
            # خواندن تمام صفحات
            all_text = ""
            for i, page in enumerate(pdf_reader.pages):
                page_text = page.extract_text()
                if page_text:
                    all_text += page_text + "\n"
                
                if (i + 1) % 10 == 0:
                    print(f"  ⏳ خوانده شد: {i + 1}/{total_pages}")
            
            print(f"\n✓ کل محتوای خوانده شده: {len(all_text)} کاراکتر")
            print(f"✓ تعداد کلمات تقریبی: {len(all_text.split())}")
            
            # نمایش 500 کاراکتر اول
            print("\n" + "="*60)
            print("📄 نمونه محتوا (500 کاراکتر اول):")
            print("="*60)
            print(all_text[:500])
            print("="*60)
            
            # بررسی کیفیت محتوا
            if len(all_text) < 100:
                print("\n⚠️ هشدار: محتوای خوانده شده خیلی کم است!")
                print("   احتمالاً PDF شامل تصاویر اسکن شده است")
            else:
                print("\n✓ محتوا با موفقیت خوانده شد")
            
            return all_text
            
    except Exception as e:
        print(f"\n✗ خطا: {e}")
        import traceback
        traceback.print_exc()
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("استفاده: python test_pdf_reading.py <path_to_pdf>")
        print("مثال: python test_pdf_reading.py book.pdf")
    else:
        test_pdf_reading(sys.argv[1])
