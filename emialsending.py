import numpy as np
from PIL import Image
import requests
import time
import os
import smtplib
from email.message import EmailMessage

# ESP32-CAM capture URL (⚠️ Remove the space)
esp32_url = 'http://192.168.1.9/capture'

# Image resolution (replace with your actual size)
width = 320
height = 240

# File save path
save_folder = r'C:\Users\HP\Desktop\image_Wrong'

if not os.path.exists(save_folder):
    os.makedirs(save_folder)

print("📡 System is running. Waiting for ESP32-CAM to allow capture...")

def send_email_with_image(image_path):
    # Email Configuration
    sender_email = "aymansiddique234386@gmail.com"
    sender_password = "tblf vajo qkvz ykpm"  # Use app password for Gmail
    receiver_email = "aymansiddique13@gmail.com"
    
    subject = "Intruder Alert - Image Captured"
    body = "The system detected an intruder. Image is attached."

    msg = EmailMessage()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.set_content(body)

    # Attach the image
    with open(image_path, 'rb') as f:
        file_data = f.read()
        file_name = os.path.basename(image_path)

    msg.add_attachment(file_data, maintype='image', subtype='jpeg', filename=file_name)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, sender_password)
            smtp.send_message(msg)
        print(f"📨 Email sent successfully to {receiver_email}")
    except Exception as e:
        print(f"⚡ Error sending email: {e}")

while True:
    try:
        response = requests.get(esp32_url, timeout=10)

        if response.status_code == 200:
            raw_data = response.content
            print(f"✅ Image data received. Size: {len(raw_data)} bytes")

            expected_size = width * height * 2  # 2 bytes per pixel for RGB565
            if len(raw_data) != expected_size:
                print("❌ Received data size does not match expected size!")
                time.sleep(2)
                continue

            # Convert raw data to numpy array of uint8
            byte_array = np.frombuffer(raw_data, dtype=np.uint8)

            # Swap bytes to correct byte order
            swapped = byte_array.reshape((-1, 2))[:, ::-1].flatten()

            # Convert to uint16
            img_array = np.frombuffer(swapped.tobytes(), dtype=np.uint16).reshape((height, width))

            # Extract R, G, B components
            r = ((img_array >> 11) & 0x1F) * 255 // 31
            g = ((img_array >> 5) & 0x3F) * 255 // 63
            b = (img_array & 0x1F) * 255 // 31

            rgb_array = np.dstack((r, g, b)).astype(np.uint8)

            # Save image with timestamp
            file_name = f"Intruder_{int(time.time())}.jpg"
            save_path = os.path.join(save_folder, file_name)

            image = Image.fromarray(rgb_array)
            image.save(save_path)
            print(f"✅ Image saved successfully to {save_path}")
            image.show()

            # Send the captured image to email
            send_email_with_image(save_path)

        elif response.status_code == 403:
            print("⏳ Capture not allowed yet. Waiting for Arduino trigger...")
            time.sleep(2)  # Polling delay

        else:
            print(f"❌ Unexpected response: {response.status_code}")
            print(f"Response content: {response.text[:200]}...")
            time.sleep(2)

    except Exception as e:
        print(f"⚡ Error: {e}")
        time.sleep(2)
