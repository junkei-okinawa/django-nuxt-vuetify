from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
print('BASE_DIR:', BASE_DIR)
STATIC_ROOT = os.path.join(BASE_DIR, 'backend/static')
print('STATIC_ROOT:', STATIC_ROOT)