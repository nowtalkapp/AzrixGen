@echo off  
title Azrix Gen Installer  
color 0c  
cls  
  
echo [1] Checking system requirements...  
timeout /t 1 /nobreak >nul  
  
echo [2] Checking for Python...  
python --version 2>nul  
if %errorlevel% neq 0 (  
    echo [!] Python not found.  
    echo [!] Please install Python from https://www.python.org/downloads/  
    echo [!] IMPORTANT: Check "Add Python to PATH" during installation.  
    echo [!] After installing, run this file again.  
    pause  
    exit  
)  
  
echo [3] Python found. Installing required libraries...  
pip install requests -q  
if %errorlevel% neq 0 (  
    echo [!] Failed to install libraries. Try running as Administrator.  
    pause  
    exit  
)  
  
echo [4] Setup complete! Launching Azrix Gen...  
timeout /t 1 /nobreak >nul  
cls  
python AzrixGen.py  