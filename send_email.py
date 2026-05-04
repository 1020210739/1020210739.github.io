#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

# E-posta ayarları
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "merdoviic@gmail.com"
# NOT: Gerçek şifre yerine Gmail App Password kullanın
SENDER_PASSWORD = os.environ.get('GMAIL_PASSWORD', "your_app_password_here")
RECIPIENT_EMAIL = "merdoviic@gmail.com"

@app.route('/send-message', methods=['POST'])
def send_message():
    try:
        data = request.get_json()
        
        name = data.get('name', '').strip()
        email = data.get('email', '').strip() or 'no-reply@example.com'
        message = data.get('message', '').strip()
        
        # Validasyon
        if not name or not message:
            return jsonify({'success': False, 'error': 'Ad ve mesaj zorunludur'}), 400
        
        # E-posta içeriği
        subject = f"Yeni İletişim: {name}"
        
        body = f"""
Yeni bir iletişim isteği aldınız:

Ad: {name}
E-posta: {email}
Tarih: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}

Mesaj:
{message}

---
Bu mesaj https://mertkucuk.com aracılığıyla gönderilmiştir.
        """
        
        # E-posta gönder
        try:
            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            
            msg = MIMEMultipart()
            msg['From'] = SENDER_EMAIL
            msg['To'] = RECIPIENT_EMAIL
            msg['Subject'] = subject
            
            msg.attach(MIMEText(body, 'plain', 'utf-8'))
            
            server.send_message(msg)
            server.quit()
            
            return jsonify({'success': True, 'message': 'Mesajınız gönderildi!'}), 200
        
        except Exception as email_error:
            print(f"E-posta gönderme hatası: {str(email_error)}")
            return jsonify({
                'success': False, 
                'error': 'E-posta gönderilirken hata oluştu'
            }), 500
    
    except Exception as e:
        print(f"Genel hata: {str(e)}")
        return jsonify({'success': False, 'error': 'Bir hata oluştu'}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'}), 200

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
