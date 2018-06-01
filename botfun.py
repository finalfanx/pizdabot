#Все импорты
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import datetime
import random
import os
import pickle
import time
import chalk

#Префикс бота
bot = commands.Bot(command_prefix='!!')

#Случайные картинки при обнятии
hug_pictures = ["https://i.redd.it/qjj7qsx9retz.gif", "https://pm1.narvii.com/6764/ed691277fa84d834857bcb6a3eab5b936c77cceev2_00.jpg", "https://d.wattpad.com/story_parts/542014250/images/151804f575f5fbc5716487997458.jpg", "https://i.redd.it/l3gplu55wo601.png", "https://cs8.pikabu.ru/post_img/2018/02/04/5/1517729932174476030.jpg", "https://scontent-ort2-1.cdninstagram.com/vp/36bd230f22148f3d92d5a15a774e0f63/5B670360/t51.2885-15/s480x480/e35/c2.0.745.745/30078066_183903425564699_5163070561223442432_n.jpg", "https://pm1.narvii.com/6709/c6f1dcca634f6684c7e5ae6b5c2f9f1360e7b87f_hq.jpg", "https://vignette.wikia.nocookie.net/doki-doki-literature-club/images/8/83/Protagonist.png/revision/latest?cb=20171203201107", "https://cdnb.artstation.com/p/assets/images/images/009/263/319/large/akang-buser-mn.jpg?1518003927", "https://pbs.twimg.com/media/DQrma4AW4AAQoJC.jpg", "https://i.pinimg.com/originals/0e/e4/81/0ee4819b2a03ad40140aeddb02cc2746.jpg", "https://t00.deviantart.net/o063ybxO9_mC2IM-n9071WDP1gE=/fit-in/700x350/filters:fixed_height(100,100):origin()/pre00/0cf3/th/pre/f/2018/029/5/7/yuri_and_natsuki_by_bluedonutillust-dc1k033.png", "https://i.pinimg.com/originals/d2/33/0b/d2330bd42dfc1575284165ac1aa6a580.jpg"]
kiss_pictures = ["https://pm1.narvii.com/6683/4b8ee9a067b71ed9e0ed4708c1ba08c72d5aaabb_hq.jpg", "https://i.redditmedia.com/lBeWiGcLhWVbFB9pYdZ_exTNME63dMj8jE7Da5i2rl8.png?w=800&s=c3e4e950182f6cc54c513be39c1a6639", "https://i.imgur.com/sZvclUA.jpg", "https://i.redditmedia.com/FI7k5hn1snHzzrlzI4cYL2EBIrEaubnx30seqwsEgZw.jpg?w=320&s=b455ec99dcd689cffe385adca68bc936", "https://img00.deviantart.net/679c/i/2017/302/c/a/yuri_x_monika___yuri_x_natsuki_by_guusagi-dbs2g4j.png", "https://lh3.googleusercontent.com/-aF4oIh5iwiQ/WpQAl3sFQbI/AAAAAAAAIwk/KOhjPdMJNAw3Xo65AhOt1kty-0QsCU8SACJoC/w530-h296-n/IMG_20180226_143908_433.JPG", "https://d.wattpad.com/story_parts/40/images/151ec4f6bd606814362631880501.jpg", "http://img1.joyreactor.cc/pics/post/full/Sayori-%28Doki-doki-Literature-club%29-Doki-doki-Literature-club-Foreign-VN-%D0%92%D0%B8%D0%B7%D1%83%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5-%D0%BD%D0%BE%D0%B2%D0%B5%D0%BB%D0%BB%D1%8B-4278115.jpeg", "https://sun1-1.userapi.com/c840420/v840420538/5b843/7LK6OFL6YTs.jpg", "https://cdn.discordapp.com/attachments/427168908693209089/443039621182652426/unknown.png", "https://pp.userapi.com/c846122/v846122756/2b6e3/xI8kGFgUynQ.jpg", "https://cdn.discordapp.com/attachments/427168908693209089/444789697319927818/Yilkp7ucgUQ.jpg", "https://t00.deviantart.net/-PJ3-10MgmeNFqp3AOVTwODSexs=/fit-in/700x350/filters:fixed_height(100,100):origin()/pre00/0c29/th/pre/f/2018/033/3/6/natsuki_x_yuri_digitized_and_colored_by_natsoni-dc1zyld.png", "https://pp.userapi.com/c824204/v824204865/b778a/X7E25wFmWCA.jpg"]
pat_pictures = ["https://pbs.twimg.com/media/DVDLueMVoAEWDA3.jpg", "http://i0.kym-cdn.com/photos/images/original/001/329/291/e77.gif"]
lick_pic = ["https://media.giphy.com/media/12MEJ2ArZc23cY/source.gif", "https://media1.tenor.com/images/0a2cdce1fc35a069cdcb992f89c8855b/tenor.gif?itemid=4859151", "http://gifimage.net/wp-content/uploads/2017/09/anime-lick-gif-11.gif", "http://gifimage.net/wp-content/uploads/2017/09/anime-lick-gif-9.gif", "https://media.giphy.com/media/E0bP09t5c9SDu/giphy.gif", "https://orig00.deviantart.net/17a5/f/2016/203/7/9/etotama_by_sadbalore-daay253.gif"]
payrespect_pic = ["https://sun1-3.userapi.com/c840625/v840625611/68cb5/Ds5kSGjew1s.jpg", "https://pp.userapi.com/c841325/v841325610/7b821/ET8jov3_a2g.jpg", "https://pp.userapi.com/c543105/v543105661/4d8ad/VNB1tlWTIiM.jpg", "https://pp.userapi.com/c543105/v543105450/3cbd4/LIPszk6rq4A.jpg", "https://pp.userapi.com/c845521/v845521837/4045b/UihjxCi9Hck.jpg", "https://sun1-4.userapi.com/c840529/v840529216/796e7/Xm1mrYPhO0U.jpg", "https://pp.userapi.com/c847017/v847017215/3ce32/HckV5WQzMJI.jpg", "https://cdn.discordapp.com/attachments/427168908693209089/443042585527713812/unknown.png", "https://cdn.discordapp.com/attachments/427168908693209089/443042691077505046/unknown.png", "https://cdn.discordapp.com/attachments/427168908693209089/443042775210917888/unknown.png", "https://cdn.discordapp.com/attachments/427168908693209089/443042871730372618/unknown.png", "https://cdn.discordapp.com/attachments/427168908693209089/443043030895820800/unknown.png", "https://cdn.discordapp.com/attachments/427168908693209089/443043123027902464/unknown.png", "https://cdn.discordapp.com/attachments/427168908693209089/443043247464644610/unknown.png", "https://cdn.discordapp.com/attachments/427168908693209089/445927120494133248/Epz67g5JhUE.png", "https://cdn.discordapp.com/attachments/427168908693209089/445927297917386752/q07SgmH1pps.png"]
kus_pic = ["https://cdn.discordapp.com/attachments/426343438968160257/444108475409367041/tumblr_nyw5qzKf4e1qbb4ago2_540.gif", "https://media1.tenor.com/images/a832fbb94fc69c07c96ea34c61568e76/tenor.gif?itemid=10216654", "https://memepedia.ru/wp-content/uploads/2017/09/%D0%BA%D1%83%D1%81%D1%8C1-6.jpg", "https://gph.is/2G2FN5D", "https://cdn.discordapp.com/attachments/427168908693209089/444111975409254420/anime-gif-Anime-Anime-Feet--3821999.gif", "https://cdn.discordapp.com/attachments/427168908693209089/444124544991494165/kus_5.gif", "https://cdn.discordapp.com/attachments/427168908693209089/444124527736127488/Kus_4.gif", "https://cdn.discordapp.com/attachments/427168908693209089/444124394990862346/kus_3.gif", "https://cdn.discordapp.com/attachments/427168908693209089/444124253470720000/Kus_1.gif", "https://cdn.discordapp.com/attachments/427168908693209089/444124234814586880/kus.gif"]
pat_pic = ["https://cdn.discordapp.com/attachments/427168908693209089/444122102388490241/Pat.gif", "https://cdn.discordapp.com/attachments/427168908693209089/444122245233770506/gladit_po_golove.gif", "https://cdn.discordapp.com/attachments/427168908693209089/444123035977383936/nezhno_glad_po_golove.gif", "https://cdn.discordapp.com/attachments/427168908693209089/444123008123142144/Kuroko_Momoi.gif", "https://cdn.discordapp.com/attachments/427168908693209089/444123371202936842/glazhu_po_golove.gif", "https://cdn.discordapp.com/attachments/427168908693209089/444123408469458956/Gladit_po_golove_2.gif", "https://cdn.discordapp.com/attachments/427168908693209089/444123425368178688/gladit_po_golove_3.gif", "https://cdn.discordapp.com/attachments/427168908693209089/444123717686001688/gladit-po-golove.gif", "https://cdn.discordapp.com/attachments/427168908693209089/444122534250807306/Glad-glad_po_golove.gif", "https://cdn.discordapp.com/attachments/427168908693209089/444122431217467402/Gladit_po_golove_1.gif"]
succ_pic = ["bjl008.gif", "bjl086.gif", "Bj_244.gif", "bjl155.gif", "Bj_083.gif", "Bj_177.gif", "Bj_099.gif", "bjl134.gif", "bjl183.gif", "bjl084.gif", "Bj_056.gif", "bjl084.gif", "bjl024.gif", "Bj_154.gif", "bjl140.gif", "bjl094.gif", "bjl153.gif", "bjl145.gif", "bjl082.gif", "Bj_119.gif", "Bj_105.gif", "bjl108.gif", "Bj_066.gif"]
eat_pic = ["https://media.giphy.com/media/11KzOet1ElBDz2/giphy.gif", "https://media.giphy.com/media/6rUFkGikou4GQ/giphy.gif", "https://media.giphy.com/media/RneIcLEosVuta/giphy.gif", "https://media.giphy.com/media/eSwGh3YK54JKU/giphy.gif", "https://media.giphy.com/media/TMruLY1JxyHvO/giphy.gif", "https://media.giphy.com/media/5ev3alRsskWA0/giphy.gif", "https://media.giphy.com/media/3eOlXFWf7K2MU/giphy.gif", "https://media.giphy.com/media/118Ue8iVVEYR5S/giphy.gif", "https://media.giphy.com/media/LU3uRsnett7gs/giphy.gif", "https://media.giphy.com/media/13LQZoCE0Nysr6/giphy.gif"]

slap_text = ["Получил по заслугам. Самый настоящий бака!", "Плохой пёсик!", "Будет знать. Бака!", "Что ты наделал?! Бака!", "Получил, бака?!"]

command1 = ["оценкавайфу", "!!оценкавайфу", "!оценкавайфу"]


#На старте
@bot.event
async def on_ready():
    print ("Бот запущен.")
    await bot.change_presence(game=discord.Game(name='!!помощь | TheOneTranslator'))

    #время
    currentweekDay = datetime.date.today().isoweekday()
    currentDay = datetime.date.today().day
    currentMonth = datetime.date.today().month

#При ошибке
@bot.event
async def on_errored():
    print ("Произошла ошибка. >_<")

#Команды бота
@bot.command(pass_context=True)
async def обнять(ctx, member : discord.Member):
    embed = discord.Embed(title = "{} ".format(ctx.message.author.name) + "обнял {0}".format(member.name), description = "Милота. ^_^", color = 0x00ff00)
    embed.set_thumbnail(url=random.choice(hug_pictures))
    await bot.say(embed=embed)
@bot.command(pass_context=True)
async def поцеловать(ctx, member : discord.Member):
    embed = discord.Embed(title = "{} ".format(ctx.message.author.name) + "поцеловал {0}".format(member.name), description = "Тьмок.", color = 0x00ff00)
    embed.set_thumbnail(url=random.choice(kiss_pictures))
    await bot.say(embed=embed)
@bot.command(pass_context=True)
async def чмок(ctx, member : discord.Member):
    embed = discord.Embed(title = "{} ".format(ctx.message.author.name) + "поцеловал {0}".format(member.name), description = "Тьмок.", color = 0x00ff00)
    embed.set_thumbnail(url=random.choice(kiss_pictures))
    await bot.say(embed=embed)
@bot.command(pass_context=True)
async def хлоп(ctx, member : discord.Member):
    embed = discord.Embed(title = "{} ".format(ctx.message.author.name) + "похлопал по голове {0}".format(member.name), description = "Хороший мальчик!", color = 0x00ff00)
    embed.set_thumbnail(url=random.choice(pat_pictures))
    await bot.say(embed=embed)
@bot.command(pass_context=True)
async def ударить(ctx, member : discord.Member):
    embed = discord.Embed(title = "{} ".format(ctx.message.author.name) + "ударил {0}".format(member.name), description = random.choice(slap_text), color = 0x00ff00)
    embed.set_thumbnail(url="http://i0.kym-cdn.com/photos/images/original/001/310/724/709.png")
    await bot.say(embed=embed)
@bot.command(pass_context=True)
async def тыщ(ctx, member : discord.Member):
    embed = discord.Embed(title = "{} ".format(ctx.message.author.name) + "ударил {0}".format(member.name), description = random.choice(slap_text), color = 0x00ff00)
    embed.set_thumbnail(url="http://i0.kym-cdn.com/photos/images/original/001/310/724/709.png")
    await bot.say(embed=embed)
@bot.command(pass_context=True)
async def облиз(ctx, member : discord.Member):
    embed = discord.Embed(title = "{} ".format(ctx.message.author.name) + "лизнул {0}  ( ͡° ͜ʖ ͡°)".format(member.name), description = "licklicklicklicklicklick", color = 0x00ff00)
    embed.set_thumbnail(url=random.choice(lick_pic))
    await bot.say(embed=embed)
@bot.command(pass_context=True)
async def облизать(ctx, member : discord.Member):
    embed = discord.Embed(title = "{} ".format(ctx.message.author.name) + "лизнул {0}  ( ͡° ͜ʖ ͡°)".format(member.name), description = "licklicklicklicklicklick", color = 0x00ff00)
    embed.set_thumbnail(url=random.choice(lick_pic))
    await bot.say(embed=embed)
@bot.command(pass_context=True)
async def шкаф(ctx, member : discord.Member):
    embed = discord.Embed(title = "Ебаный {0}".format(member.name) + "{}".format(member.name[0]) + "{}".format(member.name[0]) + "{}".format(member.name[0]) + "{}".format(member.name[0]) + "{}".format(member.name[0]) + "{}".format(member.name[0]) + "{}".format(member.name[0]) + "{}".format(member.name[0]) + "{}".format(member.name[0]) + "{}".format(member.name[0]) + "{}".format(member.name[0]) + "{}".format(member.name[0]) + "{}".format(member.name[0]) + "{}".format(member.name[0]) + "{}".format(member.name[0]) + "{}".format(member.name[0]) + "{}".format(member.name[0]) + "{}".format(member.name[0]), description = "", color = 0x00ff00)
    embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/doki-doki-literature-club/images/c/c9/Schoole.png/revision/latest/scale-to-width-down/480?cb=20171209190020")
    await bot.say(embed=embed)
@bot.command(pass_context=True)
async def инвайт(ctx):
    embed = discord.Embed(title = "Пригласить меня на свой сервер", description = "https://discordapp.com/oauth2/authorize?client_id=441553188898996235&permissions=0&scope=bot", color = 0x00ff00)
    embed.set_thumbnail(url="https://i.redd.it/uk5x9pftdlm01.png")
    await bot.say(embed=embed)
@bot.command(pass_context=True)
async def шип(ctx, member : discord.Member, member2 : discord.Member):
    embed = discord.Embed(title = "{0} x ".format(member.name) + "{0}".format(member2.name), description = "Какая милая парочка. Я шипперю их ^_^.", color = 0x00ff00)
    embed.set_thumbnail(url="http://pm1.narvii.com/6291/652383cfe314a5257de066ba5d192de4a4120dc9_00.jpg")
    await bot.say(embed=embed)
@bot.command(pass_context=True)
async def респект(ctx, member : discord.Member):
    embed = discord.Embed(title = "{} pays respects to ".format(ctx.message.author.name) + "{0}".format(member.name), description = "", color = 0x00ff00)
    embed.set_thumbnail(url=random.choice(payrespect_pic))
    await bot.say(embed=embed)
@bot.command(pass_context=True)
async def кусь(ctx, member : discord.Member):
    embed = discord.Embed(title = "{} сделал кусь ".format(ctx.message.author.name) + "{0}".format(member.name), description = "", color = 0x00ff00)
    embed.set_thumbnail(url=random.choice(kus_pic))
    await bot.say(embed=embed)
@bot.command(pass_context=True)
async def ласк(ctx, member : discord.Member):
    embed = discord.Embed(title = "{} погладил ".format(ctx.message.author.name) + "{0}".format(member.name), description = "", color = 0x00ff00)
    embed.set_thumbnail(url=random.choice(pat_pic))
    await bot.say(embed=embed)
@bot.command(pass_context=True)
async def погладить(ctx, member : discord.Member):
    embed = discord.Embed(title = "{} погладил ".format(ctx.message.author.name) + "{0}".format(member.name), description = "", color = 0x00ff00)
    embed.set_thumbnail(url=random.choice(pat_pic))
    await bot.say(embed=embed)
@bot.command(pass_context=True)
async def сас(ctx, member : discord.Member):
    if ctx.message.channel.name.startswith('♥-nsfw') or ctx.message.channel.name.startswith('nsfw') or ctx.message.channel.name.startswith('нсфв') or ctx.message.channel.name.startswith('-nsfw'):
        embed = discord.Embed(title = "{} отсосал ".format(ctx.message.author.name) + "{0}".format(member.name), description = "", color = 0x00ff00)
        embed.set_thumbnail(url="https://cdn.nekos.life/bj/" + random.choice(succ_pic))
        await bot.say(embed=embed)
    else:
        await bot.say("Название этого канала должно начинаться с ``nsfw`` или ``♥-nsfw``")
@bot.command(pass_context=True)
async def отсосать(ctx, member : discord.Member):
    if ctx.message.channel.name.startswith('♥-nsfw') or ctx.message.channel.name.startswith('nsfw') or ctx.message.channel.name.startswith('нсфв') or ctx.message.channel.name.startswith('-nsfw'):
        embed = discord.Embed(title = "{} отсосал ".format(ctx.message.author.name) + "{0}".format(member.name), description = "", color = 0x00ff00)
        embed.set_thumbnail(url="https://cdn.nekos.life/bj/" + random.choice(succ_pic))
        await bot.say(embed=embed)
    else:
        await bot.say("Название этого канала должно начинаться с ``nsfw`` или ``♥-nsfw``")
@bot.command(pass_context=True)
async def кончить(ctx, texts):
    embed = discord.Embed(title = "{} кончил на ".format(ctx.message.author.name) + "{0}".format(texts), description = "Фу, как мерзко.", color = 0x00ff00)
    embed.set_thumbnail(url="http://i0.kym-cdn.com/photos/images/newsfeed/001/303/625/b4b.png")
    await bot.say(embed=embed)
@bot.command(pass_context=True)
async def чкончить(ctx, member : discord.Member):
    embed = discord.Embed(title = "{} кончил на ".format(ctx.message.author.name) + "{0}".format(member.name), description = "Фу, как мерзко.", color = 0x00ff00)
    embed.set_thumbnail(url="http://i0.kym-cdn.com/photos/images/newsfeed/001/303/625/b4b.png")
    await bot.say(embed=embed)
@bot.command(pass_context=True)
async def съесть(ctx, member : discord.Member):
    embed = discord.Embed(title = "{} съел ".format(ctx.message.author.name) + "{0}".format(member.name), description = "Ням-ням-ням.", color = 0x00ff00)
    embed.set_thumbnail(url=random.choice(eat_pic))
    await bot.say(embed=embed)
@bot.command(pass_context=True)
async def послать(ctx, texter, member : discord.Member):
    embed = discord.Embed(title = "{} послал ".format(ctx.message.author.name) + "{0} ".format(texter) + "{0}".format(member.name), description = "", color = 0x00ff00)
    await bot.say(embed=embed)
@bot.command(pass_context=True)
async def расстрелять(ctx, member : discord.Member):
    if ctx.message.author == "426377105874616331":
        embed = discord.Embed(title = "{} расстрелял ".format(ctx.message.author.name) + "{0}".format(member.name), description = "", color = 0x00ff00)
        await bot.say(embed=embed)
    else:
        embed = discord.Embed(title = "Ты не Алекс.", description = "", color = 0x00ff00)
        await bot.say(embed=embed)
@bot.command(pass_context=True)
async def оценкавайфу(ctx, texter):
    procentcount = 0
    if texter[0].upper() == 'А':
        procentcount += 6
    elif texter[0].upper() == 'Б':
        procentcount += 15
    elif texter[0].upper() == 'В':
        procentcount += 9
    elif texter[0].upper() == 'Г':
        procentcount += 77
    elif texter[0].upper() == 'Д':
        procentcount += 11
    elif texter[0].upper() == 'Е':
        procentcount += 4
    elif texter[0].upper() == 'Ё':
        procentcount += 40
    elif texter[0].upper() == 'Ж':
        procentcount += 20
    elif texter[0].upper() == 'З':
        procentcount += 5
    elif texter[0].upper() == 'И':
        procentcount += 22
    elif texter[0].upper() == 'К':
        procentcount += 20
    elif texter[0].upper() == 'Л':
        procentcount += 2
    elif texter[0].upper() == 'М':
        procentcount += 30
    elif texter[0].upper() == 'Н':
        procentcount += 90
    elif texter[0].upper() == 'У':
        procentcount += 5
    elif texter[0].upper() == 'Ф':
        procentcount += 9
    elif texter[0].upper() == 'Х':
        procentcount += 19
    elif texter[0].upper() == 'Ц':
        procentcount += 70
    elif texter[0].upper() == 'Ч':
        procentcount += 8
    elif texter[0].upper() == 'Ш':
        procentcount += 61
    elif texter[0].upper() == 'Щ':
        procentcount += 14
    elif texter[0].upper() == 'Ы':
        procentcount += 10
    elif texter[0].upper() == 'Ъ':
        procentcount += 2
    elif texter[0].upper() == 'Э':
        procentcount += 26
    elif texter[0].upper() == 'Ю':
        procentcount += 32
    elif texter[0].upper() == 'Я':
        procentcount += 17

    if texter[1].upper() == 'А':
        procentcount -= 22
    elif texter[1].upper() == 'Б':
        procentcount += 5
    elif texter[1].upper() == 'В':
        procentcount += 11
    elif texter[1].upper() == 'Г':
        procentcount += 14
    elif texter[1].upper() == 'Д':
        procentcount += 13
    elif texter[1].upper() == 'Е':
        procentcount -= 33
    elif texter[1].upper() == 'Ё':
        procentcount += 40
    elif texter[1].upper() == 'Ж':
        procentcount += 5
    elif texter[1].upper() == 'З':
        procentcount -= 7
    elif texter[1].upper() == 'И':
        procentcount += 65
    elif texter[1].upper() == 'К':
        procentcount -= 20
    elif texter[1].upper() == 'Л':
        procentcount += 34
    elif texter[1].upper() == 'М':
        procentcount -= 21
    elif texter[1].upper() == 'Н':
        procentcount += 8
    elif texter[1].upper() == 'У':
        procentcount += 66
    elif texter[1].upper() == 'Ф':
        procentcount -= 12
    elif texter[1].upper() == 'Х':
        procentcount += 4
    elif texter[1].upper() == 'Ц':
        procentcount += 3
    elif texter[1].upper() == 'Ч':
        procentcount -= 20
    elif texter[1].upper() == 'Ш':
        procentcount += 31
    elif texter[1].upper() == 'Щ':
        procentcount += 54
    elif texter[1].upper() == 'Ы':
        procentcount += 17
    elif texter[1].upper() == 'Ъ':
        procentcount -= 12
    elif texter[1].upper() == 'Э':
        procentcount += 31
    elif texter[1].upper() == 'Ю':
        procentcount -= 32
    elif texter[1].upper() == 'Я':
        procentcount += 19
    elif texter[1].upper() == '':
        procentcount -= 5

    if texter[2].upper() == 'А':
        procentcount -= 2
    elif texter[2].upper() == 'Б':
        procentcount += 10
    elif texter[2].upper() == 'В':
        procentcount -= 11
    elif texter[2].upper() == 'Г':
        procentcount += 42
    elif texter[2].upper() == 'Д':
        procentcount -= 17
    elif texter[2].upper() == 'Е':
        procentcount += 53
    elif texter[2].upper() == 'Ё':
        procentcount -= 30
    elif texter[2].upper() == 'Ж':
        procentcount += 26
    elif texter[2].upper() == 'З':
        procentcount += 11
    elif texter[2].upper() == 'И':
        procentcount += 89
    elif texter[2].upper() == 'К':
        procentcount -= 42
    elif texter[2].upper() == 'Л':
        procentcount += 66
    elif texter[2].upper() == 'М':
        procentcount -= 24
    elif texter[2].upper() == 'Н':
        procentcount += 33
    elif texter[2].upper() == 'У':
        procentcount -= 91
    elif texter[2].upper() == 'Ф':
        procentcount += 15
    elif texter[2].upper() == 'Х':
        procentcount -= 13
    elif texter[2].upper() == 'Ц':
        procentcount -= 12
    elif texter[2].upper() == 'Ч':
        procentcount += 17
    elif texter[2].upper() == 'Ш':
        procentcount -= 37
    elif texter[2].upper() == 'Щ':
        procentcount += 22
    elif texter[2].upper() == 'Ы':
        procentcount += 23
    elif texter[2].upper() == 'Ъ':
        procentcount += 22
    elif texter[2].upper() == 'Э':
        procentcount -= 66
    elif texter[2].upper() == 'Ю':
        procentcount -= 11
    elif texter[2].upper() == 'Я':
        procentcount += 32
    elif texter[2].upper() == '':
        procentcount -= 63

    if texter[3].upper() == 'А':
        procentcount += 53
    elif texter[3].upper() == 'Б':
        procentcount -= 36
    elif texter[3].upper() == 'В':
        procentcount += 42
    elif texter[3].upper() == 'Г':
        procentcount -= 11
    elif texter[3].upper() == 'Д':
        procentcount -= 16
    elif texter[3].upper() == 'Е':
        procentcount += 23
    elif texter[3].upper() == 'Ё':
        procentcount -= 51
    elif texter[3].upper() == 'Ж':
        procentcount += 33
    elif texter[3].upper() == 'З':
        procentcount += 60
    elif texter[3].upper() == 'И':
        procentcount -= 12
    elif texter[3].upper() == 'К':
        procentcount -= 23
    elif texter[3].upper() == 'Л':
        procentcount += 55
    elif texter[3].upper() == 'М':
        procentcount -= 42
    elif texter[3].upper() == 'Н':
        procentcount -= 88
    elif texter[3].upper() == 'У':
        procentcount += 31
    elif texter[3].upper() == 'Ф':
        procentcount += 66
    elif texter[3].upper() == 'Х':
        procentcount += 41
    elif texter[3].upper() == 'Ц':
        procentcount -= 36
    elif texter[3].upper() == 'Ч':
        procentcount += 19
    elif texter[3].upper() == 'Ш':
        procentcount += 53
    elif texter[3].upper() == 'Щ':
        procentcount += 22
    elif texter[3].upper() == 'Ы':
        procentcount += 11
    elif texter[3].upper() == 'Ъ':
        procentcount += 62
    elif texter[3].upper() == 'Э':
        procentcount -= 77
    elif texter[3].upper() == 'Ю':
        procentcount += 26
    elif texter[3].upper() == 'Я':
        procentcount += 72
    elif texter[3].upper() == '':
        procentcount -= 11

    if procentcount > 100:
        procentcount = 100
    if procentcount < 0:
        procentcount = 0

    contents = ctx.message.content.split(" ") #contents is a list type
    for words in contents:
        if words.upper() not in command1:
            messagething = words

    embed = discord.Embed(title = "Думаю, что {} хорошая вайфу на".format(messagething) + " {0}%".format(procentcount), description = "", color = 0x00ff00)
    await bot.say(embed=embed)
@bot.command(pass_context=True)
async def выбор(ctx, texts, texts2):
    choosenanswer = random.randint(0,1)

    if texts == 'Моника':
        choosenanswer = 0

    if texts2 == 'Моника':
        choosenanswer = 1


    if choosenanswer == 0:
        await bot.say("Мне кажется, что ``{}``.".format(texts))
    else:
        await bot.say("Мне кажется, что ``{}``.".format(texts2))


    if texts == 'Моника':
        if texts2 == 'Моника':
            await bot.say("**ТОЛЬКО МОНИКА**")
    if texts == 'Моника':
        if texts2 != 'Моника':
            await bot.say("**ТОЛЬКО МОНИКА**")
    if texts != 'Моника':
        if texts2 == 'Моника':
            await bot.say("**ТОЛЬКО МОНИКА**")

@bot.command(pass_context=True)
async def помощь(ctx):
    embed = discord.Embed(title = "**Список команд этого бота:**", description = "версия v1.23", color = 0x00ff00)
    embed.add_field(name="!!помощь", value="Показывает полный список команд этого бота.", inline=True)
    embed.add_field(name="!!обнять [человек]", value="Обнять кого-нибудь.", inline=True)
    embed.add_field(name="!!поцеловать [человек]", value="Поцеловать кого-нибудь. !!чмок [человек]", inline=True)
    embed.add_field(name="!!хлоп [человек]", value="Похлопать кого-нибудь по голове.", inline=True)
    embed.add_field(name="!!ударить [человек]", value="Ударить кого-нибудь. Кратко: !!тыщ [человек]", inline=True)
    embed.add_field(name="!!облизать [человек]", value="Облизать кого-нибудь. Кратко: !!облиз [человек]", inline=True)
    embed.add_field(name="!!погладить [человек]", value="Погладить кого-нибудь. Кратко: !!ласк [человек]", inline=True)
    embed.add_field(name="!!отсосать [человек]", value="Ну вы поняли. ( ͡° ͜ʖ ͡°) Кратко: !!сас [человек]", inline=True)
    embed.add_field(name="!!кусь [человек]", value="Сделать кусь.", inline=True)
    embed.add_field(name="!!шкаф [человек]", value="Помочь Нацуки достать книгу с полки.", inline=True)
    embed.add_field(name="!!шип [человек] [2 человек]", value="Шипперить.", inline=True)
    embed.add_field(name="!!респект [человек]", value="Pay respects.", inline=True)
    embed.add_field(name="!!кончить [текст без пробелов]", value="Фу, как мерзко. *2 вариант: !!чкончить [человек]*", inline=True)
    embed.add_field(name="!!съесть [человек]", value="Съесть кого-нибудь.", inline=True)
    embed.add_field(name="!!послать [куда (текст без пробелов)] [человек (@Бот)]", value="Послать куда-то кого-то.", inline=True)
    embed.add_field(name="!!оценкавайфу [текст]", value="Оценить насколько (твоя) вайфу хороша. *P.S. Имена от 4 букв и без пробелов*", inline=True)
    embed.add_field(name="!!выбор [текст1] [текст2]", value="Я выберу первый или второй вариант.", inline=True)
    embed.add_field(name="!!инвайт", value="Пригласить меня на свой сервер.", inline=True)
    embed.set_thumbnail(url="https://orig00.deviantart.net/82d6/f/2017/330/b/a/yuri_by_crystalmyu-dbuwoyv.png")
    await bot.say(embed=embed)

bot.run(BOT_TOKEN)
