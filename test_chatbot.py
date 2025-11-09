import requests
import time

BASE_URL = "http://127.0.0.1:5000"

print("=" * 60)
print("تست چت‌بات تولید طرح درس")
print("=" * 60)

# مرحله 1: آپلود فایل‌ها
print("\n[1] آپلود فایل‌ها...")
files = {
    'syllabus': open('sample_syllabus.pdf', 'rb'),
    'book': open('sample_book.pdf', 'rb')
}

try:
    response = requests.post(f"{BASE_URL}/upload", files=files)
    if response.status_code == 200:
        result = response.json()
        print(f"✓ وضعیت: {result.get('status')}")
        print(f"✓ طرح درس: {result.get('syllabus_name')}")
        print(f"✓ کتاب: {result.get('book_name')}")
        print(f"✓ پیام: {result.get('message')}")
    else:
        print(f"✗ خطا: {response.status_code}")
        print(response.text)
except Exception as e:
    print(f"✗ خطا در آپلود: {e}")

# مرحله 2: ارسال پیام به چت‌بات
print("\n[2] ارسال درخواست به چت‌بات...")
message = "یک طرح درس سالانه برای درس جوشکاری E1 پایه دهم بساز"

try:
    response = requests.post(
        f"{BASE_URL}/chat",
        json={'message': message},
        headers={'Content-Type': 'application/json'}
    )
    
    if response.status_code == 200:
        result = response.json()
        chat_response = result.get('response', '')
        print(f"✓ پاسخ دریافت شد ({len(chat_response)} کاراکتر)")
        print("\n--- نمونه پاسخ (500 کاراکتر اول) ---")
        print(chat_response[:500])
        print("...")
    else:
        print(f"✗ خطا: {response.status_code}")
        print(response.text)
except Exception as e:
    print(f"✗ خطا در چت: {e}")

# مرحله 3: تولید فایل Word
print("\n[3] تولید فایل Word...")
time.sleep(2)

try:
    response = requests.post(
        f"{BASE_URL}/generate_word",
        json={'message': message},
        headers={'Content-Type': 'application/json'}
    )
    
    if response.status_code == 200:
        result = response.json()
        if result.get('status') == 'success':
            filename = result.get('filename')
            print(f"✓ فایل تولید شد: {filename}")
            print(f"✓ پیام: {result.get('message')}")
            print(f"\n✓ لینک دانلود: {BASE_URL}/download/{filename}")
        else:
            print(f"✗ خطا: {result.get('message')}")
    else:
        print(f"✗ خطا: {response.status_code}")
        print(response.text)
except Exception as e:
    print(f"✗ خطا در تولید Word: {e}")

print("\n" + "=" * 60)
print("تست کامل شد!")
print("=" * 60)
