import os
import importlib

# ফোল্ডারের ভেতর থাকা মডিউলটি খুঁজে বের করা
package_dir = os.path.dirname(__file__)
for file in os.listdir(package_dir):
    if file.startswith('alf') and (file.endswith('.so') or file.endswith('.py')):
        module_name = file.split('.')[0]
        # ডাইনামিকভাবে মডিউলটি লোড করা
        globals().update(importlib.import_module(f".{module_name}", __package__).__dict__)
        break

