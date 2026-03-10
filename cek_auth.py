import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

# Mencoba membaca file yang baru Anda pindahkan
try:
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json', 
        scopes=['https://www.googleapis.com/auth/drive.metadata.readonly']
    )
    print("✅ File credentials.json berhasil terbaca!")
except Exception as e:
    print(f"❌ Ada masalah: {e}")

