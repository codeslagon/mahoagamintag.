# Botunu aşağıdaki link'e belirt veya configs e BOT_USERNAME şeklinde belirt keyfine göre yeğenim :) 
# Telegram da beni bulmak için @Mahoaga die arat sizlere yardımcı olabilirim. 
# Sadece hobi amaçlı yapılan bir deneme projesidir. 

from Plugins import Maho
from telethon import events, Button
from telethon.tl.types import ChannelParticipantsAdmins

@Maho.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  if event.is_private:
    async for usr in Maho.iter_participants(event.chat_id):
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
     await Maho.send_message(-1001682572190, f"ℹ️ **Start Veren Kullanıcı -** {ad}")
     return await event.reply("** 🇹🇷 ᴋᴏᴍᴜᴛʟᴀʀ ʙᴜᴛᴏɴᴜɴᴀ ᴛɪᴋʟᴀʏɪɴ ᴠᴇ ᴋᴏᴍᴜᴛʟᴀʀɪ ᴏɢʀᴇɴɪɴ . . .\n🇫🇴 ᴄʟɪᴄᴋ ᴄᴏᴍᴍᴀɴᴅs ʙᴜᴛᴛᴏɴ ᴀɴᴅ ʟᴇᴀʀɴ ᴄᴏᴍᴍᴀɴᴅs . . .\n\n⚡ɴᴇᴡ ᴍᴇɴᴛɪᴏɴ ʙᴏᴛ**",
                    buttons=(
                      [
                        Button.url('🎉ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜ ɢʀᴏᴜᴘ🎉', 'https://t.me/NewMentionTagBot?startgroup=a')
                        ],
                      [
                       Button.url('🇹🇷 ᴋᴏᴍᴜᴛʟᴀʀ  ', 'https://t.me/newmentionsupport/106'),
                       Button.inline("⚙️ ʀᴇᴘᴏ", data="repo"),
                       Button.url('🇫🇴 ᴄᴏᴍᴍᴀɴᴅ  ', 'https://t.me/newmentionsupport/107'),
                      ],
                      [
                        Button.url('🌟 ᴍᴜᴢɪᴋ ʙᴏᴛ ', 'https://t.me/tqmuzikbot')
                        ],
                    ),
                    link_preview=False
                   )






# Başlanğıc Button
@Maho.on(events.callbackquery.CallbackQuery(data="repo"))
async def handler(event):
    async for usr in Maho.iter_participants(event.chat_id):
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
     await event.edit(f"**📋ɴᴏᴛ » ʀᴇᴘᴏ ᴜᴄʀᴇᴛʟɪᴅɪʀ ᴋᴜʀᴜʟᴜᴍᴅᴀ ʏᴀʀᴅɪᴍ ᴇᴅᴇʀɪᴢ\n💸ʀᴇᴘᴏ ᴜᴄʀᴇᴛɪ » 30 TL**", buttons=(

                      [
                       Button.url('⚡ ɪʟᴇᴛɪsɪᴍ ', 'https://t.me/QuitBRO'),
                       Button.url('🌟 ᴍᴜᴢɪᴋ ʙᴏᴛ ', 'https://t.me/tqmuzikbot'),
                      ],
                      [
                       Button.url('🎉ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜ ɢʀᴏᴜᴘ🎉', 'https://t.me/NewMentionTagBot?startgroup=a'),
                       Button.inline("↩️ ʙᴀᴄᴋ / ɢᴇʀɪ ↪️", data="komutlar"),
                      ],
                    ),
                    link_preview=False)

# Maho aga
@Maho.on(events.callbackquery.CallbackQuery(data="komutlar"))
async def handler(event):
    await event.edit(f"** 🇹🇷 ᴋᴏᴍᴜᴛʟᴀʀ ʙᴜᴛᴏɴᴜɴᴀ ᴛɪᴋʟᴀʏɪɴ ᴠᴇ ᴋᴏᴍᴜᴛʟᴀʀɪ ᴏɢʀᴇɴɪɴ . . .\n🇫🇴 ᴄʟɪᴄᴋ ᴄᴏᴍᴍᴀɴᴅs ʙᴜᴛᴛᴏɴ ᴀɴᴅ ʟᴇᴀʀɴ ᴄᴏᴍᴍᴀɴᴅs . . .\n\n⚡ɴᴇᴡ ᴍᴇɴᴛɪᴏɴ ʙᴏᴛ**",
                      buttons=(
                      [
                        Button.url('🎉ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜ ɢʀᴏᴜᴘ🎉', 'https://t.me/NewMentionTagBot?startgroup=a')
                        ],
                      [
                       Button.url('🇹🇷 ᴋᴏᴍᴜᴛʟᴀʀ  ', 'https://t.me/newmentionsupport/106'),
                       Button.inline("⚙️ ʀᴇᴘᴏ", data="repo"),
                       Button.url('🇫🇴 ᴄᴏᴍᴍᴀɴᴅ  ', 'https://t.me/newmentionsupport/107'),
                      ],
                      [
                        Button.url('🌟 ᴍᴜᴢɪᴋ ʙᴏᴛ ', 'https://t.me/tqmuzikbot')
                        ],
                    ),
                    link_preview=False
                   )
