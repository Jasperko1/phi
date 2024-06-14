import subprocess
import sys
subprocess.check_call([sys.executable, "-m", "pip", "install", "nltk"])
import nltk
nltk.download("popular")
