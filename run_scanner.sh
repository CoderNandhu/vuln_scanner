#!/bin/bash

echo "[+] Activating virtual environment..."
source venv/bin/activate

echo "[+] Running Vulnerability Scanner..."
python3 scanner.py

echo "[+] Deactivating virtual environment..."
deactivate
