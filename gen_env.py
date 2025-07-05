import os

# .env dosyasının oluşturulacağı dizin ve dosya adı
ENV_FILE_PATH = "D:\\courses_detailed\\generative_ai_for_beginners\\generative-ai-for-beginners\\.env"

# Kullanıcıdan GitHub token'ını al
github_token = input("Lütfen GitHub token'ınızı girin: ")

# .env dosyasının içeriği
env_content = f"GITHUB_TOKEN={github_token}\n"

# Dosyanın zaten var olup olmadığını kontrol et
if os.path.exists(ENV_FILE_PATH):
    print(f"Uyarı: {ENV_FILE_PATH} zaten mevcut. Üzerine yazmak ister misiniz? (e/h)")
    choice = input().lower()
    if choice != 'e':
        print("Dosya oluşturulmadı, mevcut dosya korundu.")
        exit()

# .env dosyasını oluştur
try:
    with open(ENV_FILE_PATH, "w", encoding="utf-8") as env_file:
        env_file.write(env_content)
    print(f".env dosyası başarıyla oluşturuldu: {ENV_FILE_PATH}")
except Exception as e:
    print(f"Hata: .env dosyası oluşturulurken bir sorun oluştu: {e}")