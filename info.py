import re
from os import environ
id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default
# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = guve api #int(environ['API_ID'],give api)
API_HASH = 'give hash'#(environ['API_HASH'],'give hash')
BOT_TOKEN = 'Get It From Bot Father' #(environ['BOT_TOKEN'],'Replace Same')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))
PICS = (environ.get('PICS', 'https://i.postimg.cc/T3yy5TYG/ca142d0a-461e-45d8-90ee-899dc5e4576e.jpg')).split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '7727074651 1102431408').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', "GIVE CHANNEL IDS BY SPACES").split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', 'LEAVE EMPTY').split()]

AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL','give forcesub channel id')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel
AUTH_GROUPS = [int(admin) for admin in environ.get("AUTH_GROUPS", "").split()]

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "get it from mongodb")
DATABASE_NAME = environ.get('DATABASE_NAME', "Musicmechanics")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', 'log channel id'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', '')

CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "⚡<b>File uploaded by @TeluguMusicMechanics<b>⚡\n\n🎦 <b>File Name: </b> ➥  {file_caption} \n⚙️ <b>Size: </b><i>{file_size}</i>\n\n                ❤️<b>WE LOVE YOU</b>❤️\n🔥  ↭ <b>Join Now Mana Channel </b> ↭  🔥")
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "False")), False)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "⚡<b>File uploaded by @TeluguMusicMechanics<b>⚡\n\n🎦 <b>File Name: </b> ➥  {file_caption} \n⚙️ <b>Size: </b><i>{file_size}</i>\n\n                ❤️<b>WE LOVE YOU</b>❤️\n🔥  ↭ <b>Join Now Mana Channel </b> ↭  🔥")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "𝐇𝐞𝐲 {message.from_user.mention}, \n 𝐇𝐞𝐫𝐞 𝐢𝐬 𝐭𝐡𝐞 𝐫𝐞𝐬𝐮𝐥𝐭 𝐟𝐨𝐫 𝐲𝐨𝐮𝐫 {query} \n <b>🏷 𝐓𝐢𝐭𝐥𝐞</b>: <a href={url}>{title}</a> \n 📆 𝐘𝐞𝐚𝐫: <a href={url}/releaseinfo>{year}</a> \n 🌟 𝐑𝐚𝐭𝐢𝐧𝐠: <a href={url}/ratings>{rating}</a> / 10 (𝐛𝐚𝐬𝐞𝐝 𝐨𝐧 {votes} 𝐮𝐬𝐞𝐫 𝐫𝐚𝐭𝐢𝐧𝐠𝐬.) \n ☀️ 𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞𝐬 : <code>{languages}</code> \n 📀 𝐑𝐮𝐧𝐓𝐢𝐦𝐞: {runtime} 𝐌𝐢𝐧𝐮𝐭𝐞𝐬 \n 📆 𝐑𝐞𝐥𝐞𝐚𝐬𝐞 𝐈𝐧𝐟𝐨 : {release_date} \n 🎛 𝐂𝐨𝐮𝐧𝐭𝐫𝐢𝐞𝐬 : <code>{countries}</code> \n \n 🙋𝐑𝐞𝐪𝐮𝐞𝐬𝐭𝐞𝐝 𝐛𝐲 : {message.from_user.mention} \n 𝐖𝐢𝐭𝐡 𝐋𝐨𝐯𝐞 @𝐓𝐆_𝐌𝐨𝐯𝐢𝐞𝐬𝟒𝐮❤️")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "False")), False)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
