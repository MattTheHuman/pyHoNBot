#!/usr/bin/env python
"""
"""

from hon.packets import ID

def apply(bot, input):
	"""Check if you application has been successful"""
	if not input.admin: return
	try:
		if not bot.vb.Login(bot.config.forumuser,bot.config.forumpassword):
			bot.reply('Unable to check application at this time')
			print("Forum credentials are invaid")
			return
		traineeApps = bot.vb.GetThreads(34, 30)
		for threadinfo in traineeApps:
			thread = threadinfo['thread']
			if thread['preview'].lower().find(input.nick.lower()) > 0:
				if thread['prefix_rich'].find("APPROVED"):
					bot.reply("Welcome to Project Epoch, %s! Inviting now." % input.nick)
					if not input.account_id in bot.clan_roster:
						bot.write_packet(ID.HON_CS_CLAN_ADD_MEMBER, input.nick)
						bot.reply("Invited!")
						bot.vb.NewPost( thread['threadid'], "Invited", "Player has been invited to the clan.")
					else:
						bot.reply("You're already in the clan?!")
						bot.vb.NewPost( thread['threadid'], "Invited", "Player has been invited to the clan. (By someone else)")
					bot.vb.MoveThread( thread['threadid'], 36 )
				else:
					bot.reply("Your application is still pending.")
				return
		mentorApps = bot.vb.GetThreads(35, 30)
		for threadinfo in mentorApps:
			thread = threadinfo['thread']
			if thread['preview'].lower().find(input.nick.lower()) > 0:
				if thread['prefix_rich'].find("APPROVED"):
					bot.reply("Welcome to Project Epoch, %s!" % input.nick)
					if not input.account_id in bot.clan_roster:
						bot.write_packet(ID.HON_CS_CLAN_ADD_MEMBER, input.nick)
						bot.reply("Invited!")
						bot.vb.NewPost( thread['threadid'], "Invited", "Player has been invited to the clan.")
					else:
						bot.reply("You're already in the clan?!")
						bot.vb.NewPost( thread['threadid'], "Invited", "Player has been invited to the clan. (By someone else)")
					bot.vb.MoveThread( thread['threadid'], 38 )
				else:
					bot.reply("Your application is still pending.")
				return
		bot.reply("No application found for your username.")
	except Exception as inst:
		print(inst)
		bot.reply('Unable to check application at this time')
apply.commands = ['apply']

if __name__ == '__main__': 
    print __doc__.strip()