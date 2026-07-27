# Proje Adı

Bu proje yerel bir sunucu üzerinde çalışan bir web sayfasıdır. İnternet üzerinden erişilebilir hale getirmek için **ngrok** kullanılır.

## Gereksinimler

- Programı çalıştırmak için gerekli ortam (Python, Node.js vb. – projenize göre)
- [ngrok](https://ngrok.com) hesabı (ücretsiz)

## 1. ngrok Kurulumu

### Hesap Oluşturma
1. [https://ngrok.com](https://ngrok.com) adresine gidin ve ücretsiz hesap oluşturun.
2. Giriş yaptıktan sonra **Dashboard** → **Your Authtoken** bölümünden authtoken’inizi kopyalayın.

### ngrok’u Yükleme

**Windows:**
- [ngrok indirme sayfası](https://ngrok.com/download)ndan Windows sürümünü indirin.
- Zip dosyasını açın ve `ngrok.exe` dosyasını istediğiniz bir klasöre koyun.

**macOS:**
```bash
brew install ngrok
