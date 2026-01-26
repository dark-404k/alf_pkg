import os
import importlib

package_dir = os.path.dirname(__file__)
module_name = None

# .so ফাইল খুঁজে বের করা
for file in os.listdir(package_dir):
    if file.startswith('alf') and file.endswith('.so'):
        module_name = file.split('.')[0]
        # যদি পাইথন ভার্সনসহ নাম থাকে (যেমন: alf.cpython-311), তবে শুধু 'alf' নিন
        if '.' in module_name:
            module_name = module_name.split('.')[0]
        break

if module_name:
    try:
        # মডিউল লোড করা
        lib = importlib.import_module(f".{module_name}", __package__)
        # সরাসরি login ফাংশন কল করা
        if hasattr(lib, 'login'):
            lib.login()
        else:
            print(f"Error: 'login' function not found in {module_name}")
    except Exception as e:
        print(f"Failed to load .so module: {e}")
