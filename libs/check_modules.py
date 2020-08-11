# coding=utf-8
#!/usr/bin/env python3

import sys

def check_modules():
    try:
        import requests
    except:
        print("[-] 'requests' package not installed!")
        print("[*] For install 'pip install requests[socks]' !")
        sys.exit(0)

    try:
        import colorama
    except Exception as e:
        print("[-] 'colorama' package not installed!")
        print("[*] For install 'pip install colorama' !")
        print(e)
        sys.exit(0)

    try:
        import asyncio
    except:
        print("[-] 'asyncio' package not installed!")
        print("[*] For install 'pip install asyncio' !")
        sys.exit(0)

    try:
        import warnings
    except:
        print("[-] 'warnings' package not installed!")
        print("[*] For install 'pip install warnings' !")
        sys.exit(0)

    import warnings
    warnings.filterwarnings("ignore")

    from colorama import init
    init()
