import sys
from pathlib import Path

# Projenin kök dizinini Python path'ine ekle
root_path = str(Path(__file__).parent)
if root_path not in sys.path:
    sys.path.append(root_path) 