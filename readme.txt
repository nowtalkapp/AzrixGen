   __    ____  ____  ____  _  _     ___  ____  _  _   
  /__\  (_   )(  _ \(_  _)( \/ )   / __)( ___)( \( )  
 /(__)\  / /_  )   / _)(_  )  (   ( (_-. )__)  )  (   
(__)(__)(____)(_)\_)(____)(_/\_)   \___/(____)(_)\_)()

⚠️ WARNING: HIGH PERFORMANCE TOOL ⚠️

THIS IS NOT A STANDARD SCRIPT. This tool utilizes multi-threaded asynchronous networking to generate and verify codes at speeds unreachable by traditional batch files.
USE RESPONSIBLY. Aggressive usage may trigger Discord's rate-limiting protections.

🛑 WHAT IS THIS?
Azrix Gen is an advanced, command-line utility designed for security researchers and developers to test the validity of Discord Nitro promotion URLs.
✅ Real HTTP Verification: Sends actual requests to Discord servers.
✅ Multi-Threaded Engine: Checks multiple codes simultaneously for maximum speed.
✅ Secure Generation: Uses cryptographically secure random number generation.
✅ Auto-Saving: Automatically logs any valid codes to valid_codes.txt.
✅ Human Verification: Includes an integrated CAPTCHA-like challenge to prevent automated abuse.

⚙️ SYSTEM REQUIREMENTS
Before running, ensure you have the following:
Windows OS (7, 8, 10, 11).
Python 3.x installed.
Internet Connection (Required for verification).

🔴 CRITICAL: If you do not have Python installed, the tool will not work. This is a high-level script, not a simple batch file.

📥 INSTALLATION & SETUP
Follow these steps exactly. Skipping steps will cause errors.
Step 1: Download the Source
Clone this repository or download the source code as a ZIP file.
Bash

Copy
git clone https://github.com/coolschool/AzrixGen.git
Step 2: Install Dependencies
This tool requires the requests library. Open your terminal/command prompt and run:
Bash

Copy
pip install requests
(If you get an error, ensure Python is added to your PATH).
Step 3: Run the Tool
Navigate to the folder and execute the main script:
Bash

Copy
python AzrixGen.py

📖 HOW TO USE
Launch the tool. You will see the red-themed interface.
Human Verification: You must solve a mathematical challenge to proceed. This prevents basic automated abuse.
Input Quantity: Enter the number of codes you wish to generate.
Warning: Generating large quantities (100+) may result in your IP being temporarily rate-limited by Discord.
Wait: The tool will attempt to generate and verify codes.
RED TEXT: Invalid code.
GREEN TEXT: VALID CODE FOUND! (This will also be saved to valid_codes.txt).


📜 DISCLAIMER & TERMS OF USE

⚠️ LEGAL DISCLAIMER: This tool is for educational and security research purposes only.
The probability of generating a valid, unused Discord Nitro code is statistically negligible.
This tool does not "hack" Discord; it randomly generates strings and checks if they exist.
Do not use this tool for malicious intent.
The creator (Azrix) is not responsible for any IP bans, account restrictions, or legal issues arising from the misuse of this software.
Discord is a trademark of Discord Inc. This tool is not affiliated with, endorsed by, or supported by Discord Inc.

🆘 TRROUBLESHOOTING
"ModuleNotFoundError: No module named 'requests'"
You did not install the required library. Run pip install requests.
"Python is not recognized"
Python is not installed or not added to your system PATH. Reinstall Python and check "Add to PATH".
"Error (Rate Limit)"
You are sending too many requests too fast. Discord has blocked your IP temporarily. Wait 1-24 hours before trying again.

📬 CONTACT
Developed by Azrix. For issues or questions, open an issue on this GitHub repository.
DO NOT USE FOR COMMERCIAL PURPOSES.
© 2026 Azrix. All Rights Reserved.