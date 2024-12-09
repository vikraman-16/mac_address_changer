import subprocess

interface = input("interface> ")
mac = input("mac> ")

try:
    print("[*] Bringing the interface down...")
    subprocess.check_call(["sudo", "ifconfig", interface, "down"])

    print("[*] Setting the MAC address...")
    subprocess.check_call(["sudo", "ifconfig", interface, "hw", "ether", mac])

    print("[*] Bringing the interface up...")
    subprocess.check_call(["sudo", "ifconfig", interface, "up"])

    print(f"[+] MAC address successfully changed to {mac}")
except subprocess.CalledProcessError as e:
    print(f"[-] Command failed: {e}")
except Exception as e:
    print(f"[-] An unexpected error occurred: {e}")
