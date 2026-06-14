# desktop-automation-bot
Telegram bot for remote PC management, app launching, and automation via Telebot. (pcbot.pyw)

A Python-based Telegram bot for remote Windows PC management and automation. It allows you to switch between work/relaxation modes, launch applications, open websites, kill processes, and shut down your PC using a clean, responsive reply keyboard.

It responds strictly with military discipline: *"Yes, sir!"* 

## Features

* **Smart Modes:**
  * 🍿 **Chill Mode** — Opens YouTube in Chrome and launches Telegram.
  * 👨‍💻 **Work Mode** — Launches Visual Studio, opens Gemini AI, and starts Telegram.
  * 🎉 **Guests Mode** — Directly launches a dedicated guest playlist on YouTube.
  * 🎮 **Game Mode** — Launches Steam instantly.
* **Quick Web Access:** One-click shortcuts for Simpsons UA and HD Rezka.
* **App Launchers:** Standalone buttons to launch Chrome, Telegram, or Visual Studio.
* **System Management:**
  * ❌ **Close All** — Forcefully kills running workspace processes (`taskkill`) to clean up your desktop.
  * 🛑 **Turn Off PC** — Triggers a safe system shutdown with a 5-second delay.
* **Hardened Security:** The bot strictly processes commands from the defined `ADMIN_ID`. Any unauthorized messages are completely ignored.

## Tech Stack

* **Language:** Python 3.x
* **Bot Framework:** `pyTelegramBotAPI` (telebot)
* **OS Interaction:** Built-in `subprocess` and `os` modules (Windows native execution).

## Setup & Installation

### 1. Prerequisites
Clone the repository and install the required Telegram bot dependency:
```bash
pip install pyTelegramBotAPI
```

### 2. Configuration
Open the script and update the configuration variables inside the `Settings` section:
* **`TOKEN`**: Your Telegram Bot token obtained from [@BotFather](https://t.me).
* **`ADMIN_ID`**: Your personal numeric Telegram Chat ID (can be fetched via [@userinfobot](https://t.me)).
* **Application Paths (`*_PATH`)**: Double-check and verify that the absolute paths to your `.exe` files match your system layout.
* **Links**: Replace `GUEST_PLAYLIST` with your custom YouTube playlist URL.

### 3. Execution
Run the script using your terminal or command prompt:
```bash
python main.py
```
Upon a successful connection, the bot will message you: *"Hello, sir! Ready to work"*.

---

## Running on Windows Startup (Background Mode)

To make the bot start automatically every time you turn on your PC and run invisibly in the background without keeping a black console window open, follow these steps:

### Step 1: Enable Background Mode
1. Change your script's file extension from `.py` to **`.pyw`** (e.g., rename `main.py` to `main.pyw`). This tells Windows to execute the script without opening a command prompt window.
2. Right-click on your `main.pyw` file and select **Create shortcut**.

### Step 2: Add to Windows Startup Folder
1. Press `Win + R` on your keyboard to open the **Run** dialog box.
2. Type `shell:startup` and press **Enter**. This opens your personal Windows Startup folder.
3. Move or copy the **Shortcut** you created in Step 1 into this folder.

Now, whenever Windows boots up, your bot will launch automatically and run silently in the background.

---

## Security Notice
Never commit your production file with the actual `TOKEN` or `ADMIN_ID` exposed to a public GitHub repository. It is highly recommended to migrate these sensitive credentials to an environment file (`.env`).

## License
This project is open-source and available under the [MIT License](LICENSE).
