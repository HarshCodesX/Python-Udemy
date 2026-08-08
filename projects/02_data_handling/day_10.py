"""
 Challenge: Offline Notes Locker

Create a terminal-based app that allows users to save, view, and search personal notes securely in an encrypted file.

Your program should:
1. Let users add notes with title and content.
2. Automatically encrypt each note using Fernet (AES under the hood).
3. Store all encrypted notes in a single `.vault` file (JSON format).
4. Allow listing of titles and viewing/decrypting selected notes.
5. Support searching by title or keyword.

Bonus:
- Add timestamps to notes.
- Use a master password to unlock vault (optional).
"""

import json
import os
from cryptography.fernet import Fernet
from datetime import datetime

VAULT_FILE = "notes_vault.json"
KEY_FILE = "vault.key"

def load_or_create_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, 'wb') as f:
            f.write(key)
    else:
        with open(KEY_FILE, 'rb') as f:
            key = f.read()

    return Fernet(key)

fernet = load_or_create_key()

def load_vault():
    if not os.path.exists(VAULT_FILE):
        return []
    else:
        with open(VAULT_FILE, 'r', encoding="utf-8") as f:
            return json.load(f)

def save_vault(data):
    with open(VAULT_FILE, 'w', encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def add_note():
    title = input("Enter note title: ").strip()
    content = input("Enter note content: ").strip()

    encryptedContent = fernet.encrypt(content.encode()).decode()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = load_vault()
    data.append({
        "titile": title,
        "content": encryptedContent,
        "timestamp": timestamp
    })
    save_vault(data)
    print("Data Saved!")