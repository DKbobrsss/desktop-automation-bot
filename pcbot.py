import telebot
import os
import subprocess
from telebot import types

# Settings
TOKEN = 'Bot_Token'
ADMIN_ID = 123456789 # chat id in telegram 

# Path to applications (update these paths to match your system)
CHROME_PATH = r"your path to chrome.exe"
TG_PATH = r"your path to Telegram.exe"
VS_CODE_PATH = r"your path to Visual Studio.exe"
STEAM_PATH = r"your path to Steam.exe"

GUEST_PLAYLIST = "link to youtube playlist for guests"
SIMPSONS_URL = "https://simpsonsua.tv/" 
REZKA_URL = "https://rezka.ag/"        

# list of apps to close when "Close All" is pressed (make sure these match the actual process names in Task Manager)
APPS_TO_CLOSE = ["chrome.exe", "Telegram.exe", "devenv.exe", "steam.exe"]


bot = telebot.TeleBot(TOKEN)

def main_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    
    # Modes
    btn_chill = types.KeyboardButton("🍿 Chill")
    btn_work = types.KeyboardButton("👨‍💻 Work")
    btn_guests = types.KeyboardButton("🎉 Guests")
    btn_game = types.KeyboardButton("🎮 Game Mode")
    
    # Sites
    btn_simpsons = types.KeyboardButton("🍩 Simpsons UA")
    btn_rezka = types.KeyboardButton("🎬 HD Rezka")
    
    # Individual apps
    btn_chrome = types.KeyboardButton("🌐 Chrome")
    btn_tg = types.KeyboardButton("✈️ Telegram")
    btn_vs = types.KeyboardButton("💻 Visual Studio")
    
    # Management
    btn_close_all = types.KeyboardButton("❌ Close All")
    btn_off = types.KeyboardButton("🛑 Turn Off PC")
    
    markup.add(btn_chill, btn_work, btn_guests, btn_game)
    markup.add(btn_simpsons, btn_rezka)
    markup.add(btn_chrome, btn_tg, btn_vs)
    markup.add(btn_close_all, btn_off)
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    if message.from_user.id == ADMIN_ID:
        bot.send_message(ADMIN_ID, "Yes, sir!", reply_markup=main_keyboard())

@bot.message_handler(func=lambda message: True)
def handle_commands(message):
    if message.from_user.id != ADMIN_ID:
        return

    # Modes
    if message.text == "🍿 Chill":
        subprocess.Popen([CHROME_PATH, "--profile-directory=Default", "https://www.youtube.com"])
        os.startfile(TG_PATH)
        bot.send_message(ADMIN_ID, "Relax, sir! Chill mode activated.")

    elif message.text == "👨‍💻 Work":
        os.startfile(VS_CODE_PATH)
        subprocess.Popen([CHROME_PATH, "--profile-directory=Default", "https://gemini.google.com"])
        os.startfile(TG_PATH)
        bot.send_message(ADMIN_ID, "Happy coding, sir! Work mode activated.")

    elif message.text == "🎉 Guests":
        subprocess.Popen([CHROME_PATH, "--profile-directory=Default", GUEST_PLAYLIST])
        bot.send_message(ADMIN_ID, "Have fun, sir! Guests mode activated.")

    elif message.text == "🎮 Game Mode":
        os.startfile(STEAM_PATH)
        bot.send_message(ADMIN_ID, "Happy gaming, sir! Steam launched.")

    # --- САЙТЫ ---
    elif message.text == "🍩 Simpsons UA":
        subprocess.Popen([CHROME_PATH, "--profile-directory=Default", SIMPSONS_URL])

    elif message.text == "🎬 HD Rezka":
        subprocess.Popen([CHROME_PATH, "--profile-directory=Default", REZKA_URL])

    # --- КНОПКИ ПРОГРАММ ---
    elif message.text == "🌐 Chrome":
        subprocess.Popen([CHROME_PATH, "--profile-directory=Default"])

    elif message.text == "✈️ Telegram":
        os.startfile(TG_PATH)

    elif message.text == "💻 Visual Studio":
        os.startfile(VS_CODE_PATH)

    # management
    elif message.text == "❌ Close All":
        bot.send_message(ADMIN_ID, "Cleaning workspace... 🧹")
        for app in APPS_TO_CLOSE:
            os.system(f"taskkill /f /im {app} /t")
        bot.send_message(ADMIN_ID, "Ready, sir! Clean desk.")

    elif message.text == "🛑 Turn Off PC":
        bot.send_message(ADMIN_ID, "Shutting down...")
        os.system("shutdown /s /t 5")

# send startup message to admin
try:
    bot.send_message(ADMIN_ID, "Hello, sir! Ready to work", reply_markup=main_keyboard())
except Exception as e:
    print(f"Error sending startup message: {e}")

bot.polling(none_stop=True)
