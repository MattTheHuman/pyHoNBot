# captures nicks and ids and builds dicts for both nick2id and id2nick
#
from hon.packets import ID
from hon.honutils import normalize_nick
import re

def GetClanTag(nick):
    match = re.match(r'\[(.*)\](.*)', nick)
    return match and match.group(1) or ""

def joined_channel(bot,origin,data):
    print("Joined " + data[0])
    bot.chan2id[data[0].lower()] = data[1]
    bot.id2chan[data[1]] = data[0].lower()
    for m in data[-1]:
        bot.id2clan[m[1]] = GetClanTag(m[0])
        m[0] = normalize_nick(m[0])
        bot.nick2clan[m[0]] = bot.id2clan[m[1]]
        bot.nick2id[m[0]] = m[1]
        bot.id2nick[m[1]] = m[0]
        bot.user_status[m[1]] = m[2]
joined_channel.event = [ID.HON_SC_CHANGED_CHANNEL]
joined_channel.priority = 'high'
joined_channel.thread = False

def user_joined_channel(bot,origin,data):
    nick = normalize_nick(data[0])
    bot.id2clan[data[1]] = GetClanTag(data[0])
    bot.nick2clan[nick] = bot.id2clan[data[1]]
    bot.nick2id[nick] = data[1]
    bot.id2nick[data[1]] = nick
    bot.user_status[data[1]] = data[3]
user_joined_channel.event = [ID.HON_SC_JOINED_CHANNEL]
user_joined_channel.priority = 'high'
user_joined_channel.thread = False

def name_change(bot,origin,data):
    nick = normalize_nick(data[1])
    bot.nick2id[nick] = data[0]
    bot.id2nick[data[0]] = nick
name_change.event = [ID.HON_SC_NAME_CHANGE]
name_change.priority = 'high'
name_change.thread = False

def update_status(bot, origin, data):
    bot.user_status[data[0]] = data[1]
update_status.event = [ID.HON_SC_UPDATE_STATUS]

def user_left_channel(bot, origin, data):
    nick = bot.id2nick[data[0]]
    bot.write_packet(ID.HON_CS_USER_INFO, nick)
user_left_channel.event = [ID.HON_SC_LEFT_CHANNEL]

def user_offline(bot, origin, data):
    if data[0] in bot.nick2id:
        id = bot.nick2id[data[0]]
        del(bot.nick2id[data[0]])
        if id in bot.id2nick:
            del(bot.id2nick[id])
user_offline.event = [ID.HON_SC_USER_INFO_OFFLINE, ID.HON_SC_USER_INFO_NO_EXIST]