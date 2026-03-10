from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']

# Menggunakan flow manual agar tidak mencoba membuka browser otomatis
flow = InstalledAppFlow.from_client_secrets_file(
    'credentials.json', 
    scopes=SCOPES
)

# Perintah ini akan memunculkan link untuk disalin manual 
creds = flow.run_local_server(port=0, open_browser=False)


service = build('drive', 'v3', credentials=creds)
results = service.files().list(pageSize=10).execute()
items = results.get('files', [])

if not items:
    print('Drive kosong.')
else:
    print('✅ Berhasil! 10 File Terakhir Anda:')
    for item in items:
        print(f"- {item['name']}")

