# utils/gdrive_upload.py
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import os

SERVICE_ACCOUNT_FILE = "v1\credentials.json"  # your JSON
SCOPES = ['https://www.googleapis.com/auth/drive']


def get_or_create_folder(service, folder_name, parent_id=None):
    query = f"name='{folder_name}' and mimeType='application/vnd.google-apps.folder' and trashed=false"
    
    if parent_id:
        query += f" and '{parent_id}' in parents"

    results = service.files().list(q=query, fields="files(id, name)").execute()
    files = results.get('files', [])

    if files:
        return files[0]['id']

    PARENT_FOLDER_ID = "1ggshC6NtuA5FxWnnAMdMgsMTbyNr2J_T"


    file_metadata = {
        'name': folder_name,
        'mimeType': 'application/vnd.google-apps.folder',
        'parents': [PARENT_FOLDER_ID]
    }

    folder = service.files().create(body=file_metadata, fields='id').execute()
    return folder.get('id')

def upload_with_structure(file_path, main_folder="Recordings", sub_folder=None):
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )
    service = build('drive', 'v3', credentials=creds)

    # Root folder
    root_id = get_or_create_folder(service, main_folder)

    # Subfolder (endpoint-based)
    if sub_folder:
        sub_id = get_or_create_folder(service, sub_folder, root_id)
    else:
        sub_id = root_id

    file_name = os.path.basename(file_path)

    PARENT_FOLDER_ID = "1ggshC6NtuA5FxWnnAMdMgsMTbyNr2J_T"

    file_metadata = {
        'name': file_name,
        'parents': [PARENT_FOLDER_ID]
    }

    media = MediaFileUpload(file_path, resumable=True)

    service.files().create(
        body=file_metadata,
        media_body=media
    ).execute()

    print(f"[Drive] Uploaded to {main_folder}/{sub_folder}")