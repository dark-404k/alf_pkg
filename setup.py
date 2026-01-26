from setuptools import setup, find_packages
import subprocess
import sys

# অটো-ইনস্টল করার জন্য মডিউল লিস্ট
requirements = [
    'requests',
    'certifi',
    'openpyxl',
    'cryptography',
]

setup(
    name="alf_pkg", 
    version="1.0",
    author="dark-404k",
    description="Encrypted Alf Tool Package",
    packages=find_packages(),
    # এই অংশটি প্রয়োজনীয় মডিউল অটো ইনস্টল করবে
    install_requires=requirements,
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Android",
    ],
)

# সেটআপ শেষে ইউজারকে মেসেজ দিবে
print("\n[+] Alf Package Installed Successfully!")
print("[+] You can now run the tool using 'python run.py'\n")
