import os
[os.rename(f, f.replace('di', 'xi')) for f in os.listdir('.') if not f.startswith('.')]
