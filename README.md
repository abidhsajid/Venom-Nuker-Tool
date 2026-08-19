# Venom Nuke Tool v12  🚀

A modular, highly efficient Discord management and utility toolkit designed for administrative operations, server management, and automation tasks.



## 🌟 Features

*   **Member Management:** Bulk ban capabilities with permission handling and safety checks.
*   **Channel Operations:** Automated mass creation and complete channel deletion pipelines.
*   **Role Management:** Full role removal capabilities and instant `@everyone` administrative privilege granting.
*   **Emoji Management:** Clean, automated removal of server emojis.
*   **Server Customization:** Instant server name modification scripts.
*   **Interactive CLI Interface:** Aesthetic cross-platform terminal interface styled using `pystyle` and `colorama`.


## 📁 Project Structure

  text
├── main.py              # Central entry point and terminal dashboard
├── utili.py             # Shared utility functions, titles, and spinners
├── token.txt            # Stored Discord Bot Token configuration
├── server.txt           # Target Discord Server ID configuration
└── scripts/             # Core action execution modules
    ├── 1_BanAll.py
    ├── 2_EliminaCanali.py
    ├── 3_EliminaRuoli.py
    ├── 4_ModificaEveryone.py
    ├── 5_CreaCanali.py
    ├── 6_CambiaNomeServer.py
    └── 7_EliminaEmoji.py

🛠️ Installation & Setup
Clone the repository:

Bash


Install the required dependencies:

Bash
pip install nextcord colorama pystyle requests certifi

Configure the application:

Enter your bot token via Option 10 in the tool interface (or manually create a token.txt file).

Enter your target Server ID via Option 11 in the tool interface (or manually create a server.txt file).

🚀 Usage
Run the main dashboard script:

Bash

python3 Venom.py

or 

setup.bat

 Main Menu Overview

[1] Ban all members - Bulk bans all members in the target server.

[2] Delete all channels - Clears all text and voice channels.

[3] Delete all roles - Strips and deletes server roles.

[4] Give @everyone administrator - Grants administrator permissions to the default role.

[5] Create channels - Spams channel creation with preset names.

[6] Change server name - Instantly updates the server title.

[7] Delete server emojis - Purges custom emojis.


⚙️ Requirements

Python 3.8+

Packages: nextcord, colorama, pystyle, certifi, requests



Disclaimer: This tool is intended for educational purposes and authorized administrative testing. Use responsibly and in accordance with Discord's Terms of Service.
