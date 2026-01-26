import os
import importlib

# ফোল্ডারের ভেতর থাকা মডিউলটি খুঁজে বের করা
package_dir = os.path.dirname(__file__)
for file in os.listdir(package_dir):
    # এখানে 'Alf' বা 'alf' দুইটাই চেক করবে যাতে নামের কারণে এরর না আসে
    if file.lower().startswith('alf') and (file.endswith('.so') or file.endswith('.py')):
        if file == '__init__.py': # নিজেকে লোড করা থেকে বিরত থাকবে
            continue
        module_name = file.split('.')[0]
        # ডাইনামিকভাবে মডিউলটি লোড করা
        try:
            globals().update(importlib.import_module(f".{module_name}", __package__).__dict__)
        except Exception as e:
            print(f"Error loading module {module_name}: {e}")
        break
# আপনার মডিউল লোড হওয়ার পর সরাসরি ফাংশন কল করুন
# আপনার মডিউল লোড হওয়ার পর সরাসরি ফাংশন কল করুন
try:
    from .Alf_enc import login  # এখানে 'approval' এর বদলে 'login' হবে
    login()
except Exception as e:
    # রান না হলে এরর দেখার জন্য নিচের লাইনটি ব্যবহার করতে পারেন
    # print(f"Error: {e}")
    pass
