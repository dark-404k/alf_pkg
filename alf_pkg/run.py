import os
import alcm_pkg
if not os.path.exists("Confirm_Acc_List.txt"):
    open("Confirm_Acc_List.txt", "w").close()

print("[*] টুলটি চালু হচ্ছে...")
try:
    # যদি __init__ কাজ করে তবে সরাসরি কল হবে
    alcm_pkg.autom_main()
except AttributeError:
    # বিকল্প উপায়
    from alcm_pkg import alcm
    alcm.autom_main()
