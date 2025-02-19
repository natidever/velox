
import sys
import os

# Get the absolute path of the project root
ROOT_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(ROOT_DIR)

print(f'yelllow :{ROOT_DIR}')