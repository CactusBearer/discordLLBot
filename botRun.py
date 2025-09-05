#discord testBot
import discord, random

class LoveLetter:
    global LLPlayers, LLPlayerDict, LLChats
    active = False
    players = 0
    activePlayer = 0
    firstPlayer = 0
    deck = []
    pointsToWin = 10
    setAside = -1

    def __init__(self, playerID, threadID, name):
        self.name = name
        self.playerID = playerID
        self.threadID = threadID
        self.holdCard = -1
        self.drawCard = -1
        self.points = 0
        self.seatNum = -1
        self.discarded = []
        self.chancellorCards = []
        self.alive = True
        self.shielded = False
        LLPlayers.append(self)
        LLChats.append(threadID)
        LLPlayerDict[name] = self

    def setupSeats(playerList):
        LoveLetter.players = len(playerList)
        if LoveLetter.players == 6:
            LoveLetter.pointsToWin = 3
        else:
            LoveLetter.pointsToWin = 8 - LoveLetter.players
        i = 0
        random.shuffle(playerList)
        for randomPlayer in playerList:
            randomPlayer.seatNum = i
            i+=1
        LoveLetter.firstPlayer = 0
        print("set up seats")
        LoveLetter.resetRound()

    def endRound():
        whoScored = [[], "Nobody"]
        alivePlayers = []
        spyHavers = []
        for player in LLPlayers:
            if player.alive:
                alivePlayers.append(player)
            for card in player.discarded:
                if card == 0:
                    spyHavers.append(player)
        if len(alivePlayers) == 1:
            alivePlayers[0].points += 1
            whoScored[0].append(alivePlayers[0].name)
        else:
            maxVal = alivePlayers[0].holdCard
            for count in range(len(alivePlayers)):
                maxVal = max(alivePlayers[count].holdCard, maxVal)
            for player in alivePlayers:
                if player.holdCard == maxVal:
                    player.points += 1
                    whoScored[0].append(player.name)
        if len(spyHavers) == 1:
            spyHavers[0].points += 1
            whoScored[1] = spyHavers[0].name
        elif len(spyHavers) == 2:
            if spyHavers[0].name == spyHavers[1].name:
                spyHavers[0].points += 1
                whoScored[1] = spyHavers[0].name

        return whoScored
        

    def nextTurn():
        for count in range(1, LoveLetter.players):
            checkSeat = (LoveLetter.activePlayer + count) % LoveLetter.players
            if LLPlayers[checkSeat].alive:
                LoveLetter.activePlayer = checkSeat
                LLPlayers[checkSeat].shielded = False
                LLPlayers[checkSeat].drawCard = LoveLetter.deck.pop(0)
                return
        

    def resetRound():
        if random.randint(1,1000)<=999:
            LoveLetter.deck = [0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 8, 9]
        else:
            print("used a fake deck!")
            LoveLetter.deck = [0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 8, 9]   #shenanigans
        #LoveLetter.deck = [0, 1, 6, 6, 6, 6] #test deck
        random.shuffle(LoveLetter.deck)
        LoveLetter.setAside = LoveLetter.deck.pop(0)
        for player in LLPlayers:
            player.discarded = []
            player.holdCard = LoveLetter.deck.pop(0)
            player.alive = True
        LoveLetter.activePlayer = LoveLetter.firstPlayer
        LoveLetter.firstPlayer = (LoveLetter.firstPlayer + 1) % LoveLetter.players
        LLPlayers[LoveLetter.activePlayer].drawCard = LoveLetter.deck.pop(0)
        print("reset round")
        #LoveLetter.updateRound()

    '''
    @classmethod
    def updateRound(cls):
        if len(cls.deck) == 0:
            return
        for player in LLPlayers:
            if player.seatNum == cls.activePlayer:
                player.drawCard = cls.deck.pop(0)
                
            else:
    '''

    def lmao():
        print("lol")

LEO_ID = 242373818138492928
ETHAN_ID = 303324041257943044
IANNOUNCEMENTS_ID = 1017218720264896584
PRIMARY_ID = 1038587578212958260 #1126268259205922877 1038587578212958260
VANNOUNCEMENTS_ID = 1103455141451014154

ANNOUNCEMENT = "beep boop it's weekly scheduling time :]\n\n\
Please react to the day of the week in which you would like to play board games! Tentative plan is always for them to played on the third floor of the student union but if YOU would rather play them somewhere else, just say and make plans otherwise! I'm here to determine availability :]\n\n\
As always, feel free to bring your own games or suggest ones that we play. You are also free to bring along new people, announced or otherwise\n\n\
Plan is to have board games up to two times this week, likely once during, once on the weekend. For your availability, please react with\n\
:regional_indicator_m: for Monday, :regional_indicator_t: for Tuesday, :regional_indicator_w: for Wednesday, <:_h:1108892121332711536> for Thursday, :regional_indicator_f: for Friday, :regional_indicator_s: for Saturday, and :sunny: for Sunday, or :thumbsdown: if you can't make it."

REQUEST = "If you have particular interest in a specific game or type of game, please react as appropriately below:\n \
No particular interest: :thumbsup:\n\
Longer-form board games: :hourglass:\n\
Shorter-form board games/party games: :tada:\n\
Settlers of Catan: :sheep:\n\
Scythe: :crossed_swords:\n\
Cloak and Blaster: :gun:\n"


global sentPrimary, LLPlayerIDs, LLPlayers, LLStartMessageID, LLPlayerDict, LLCardDict

sentPrimary = False
LLNeedsPing = ["luminouswisp", "ethan_thisguy"]
LLChats = []
LLPlayerIDs = []
LLPlayers = []
LLPlayerDict = {}
LLMentionDict = {}
LLCardDict = {0:"Spy(0)", 1:"Guard(1)", 2:"Priest(2)", 3:"Baron(3)", 4:"Handmaid(4)", \
              5:"Prince(5)", 6:"Chancellor(6)", 7:"King(7)", 8:"Countess(8)", 9:"Princess(9)",
              '0':"Spy(0)", '1':"Guard(1)", '2':"Priest(2)", '3':"Baron(3)", '4':"Handmaid(4)", \
              '5':"Prince(5)", '6':"Chancellor(6)", '7':"King(7)", '8':"Countess(8)", '9':"Princess(9)"}
LLStartMessageID = 0
BLACKLIST = [695718586433404948]


intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents, allowed_mentions = discord.AllowedMentions.all())

#LEO_USER = client.get_user(242373818138492928)
#ETHAN_USER = client.get_user(303324041257943044)
#IANNOUNCEMENTS_CHANNEL = client.get_channel(1017218720264896584)
#PRIMARY_CHANNEL = client.get_channel(1038587578212958260)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    LoveLetter.lmao()
    #await client.get_user(LEO_ID).send("I will h you")

@client.event
async def on_message_edit(before, after):
    if after.channel.id != IANNOUNCEMENTS_ID and after.channel.id != VANNOUNCEMENTS_ID:
        if before.mention_everyone and not after.mention_everyone:
            await after.channel.send(":face_with_raised_eyebrow: oh so removing a ping are we? hmmm", reference = after, mention_author=False)
        elif not before.mention_everyone and after.mention_everyone:
            await after.channel.send("editing *IN* a ping. now that's something", reference = after, mention_author=False)
        return

#log deleted messages. hope to not need to uncomment
#@client.event
#async def on_message_delete(message):
    #await client.get_user(LEO_ID).send(message.author.name+"("+str(message.author.id)+") deleted \""+message.content +"\" from "+message.channel.name, silent=True)
    #return

@client.event
async def on_reaction_add(reaction, user):
    global LLPlayerIDs, LLPlayers, LLStartMessageID, LLPlayerDict, LLChats, LLNeedsPing, LLMentionDict
    #print("saw a reaction\n"+str(LLStartMessageID)+"\n"+str(reaction.message.id))
    if reaction.emoji == "🍬":
        print("threading")
        #await (await reaction.message.channel.create_thread(name = "public-loveletter-thread", type = discord.ChannelType.public_thread)).send("Wow a whole dedicated chat. Maybe you people will stop spamming \
                                                    #primary now. Probably not.")
        
    if reaction.message.id == LLStartMessageID and reaction.emoji == '✅':
        for alreadyIn in LLPlayerIDs:
            if user.id == alreadyIn:
                await reaction.message.channel.send(user.name+" you're already in the game, chill")
                return
        if LLPlayerIDs[0] == -1:
            LLPlayerIDs.append(user.id)
            LLMentionDict[user.name] = user.mention
                
            if len(LLPlayerIDs) == 7:
                
                LLPlayerIDs.pop(0)
            await reaction.message.edit(content = reaction.message.content+"\n"+str(len(LLPlayerIDs))+". "+user.name)

        else:
            await reaction.message.channel.send("Not currently accepting players")
            
    elif reaction.message.id == LLStartMessageID and reaction.emoji == '👎' and \
         (((LLPlayerIDs[0] == user.id) or (LLPlayerIDs[1] == user.id and LLPlayerIDs[0] == -1) and not LoveLetter.active) or LEO_ID == user.id):
        await reaction.message.channel.send("Cancelling !loveletter request. Feel free to try again")

        for finalPlayer in LLPlayers:
            await client.get_channel(finalPlayer.threadID).delete()
                            
        LoveLetter.active = False
        LoveLetter.players = 0
        LoveLetter.activePlayer = 0
        LoveLetter.firstPlayer = 0
        LoveLetter.deck = []
        LoveLetter.pointsToWin = 10
        LoveLetter.setAside = -1

        LLPlayerIDs = []
        LLPlayers = []
        LLChats = []
        LLPlayerDict = {}
        LLMentionDict = {}
        LLStartMessageID = 0

    elif reaction.message.id == LLStartMessageID and reaction.emoji == '👂' and LoveLetter.active:
        await client.get_channel(LLChats[0]).add_user(user)

            
    elif reaction.message.id == LLStartMessageID and reaction.emoji == '👍' and (LLPlayerIDs[0] == user.id or (LLPlayerIDs[1] == user.id and LLPlayerIDs[0] == -1)):
        if len(LLPlayerIDs) < 3:#4:
            await reaction.message.channel.send("Not enough players")
            return
        if LLPlayerIDs[0] == -1:
            LLPlayerIDs.pop(0)
        #create six threads
        await reaction.message.edit(content = reaction.message.content+"\nGAME HAS BEGUN\n\nPlease react to this message with a :ear: to join the public thread")
        LLChats.append((await reaction.message.channel.create_thread(name = "public-loveletter-thread")).id)
        await client.get_channel(LLChats[0]).send("Wow a whole dedicated chat. Maybe you people will stop spamming #primary now. Probably not.")
        for playerID in LLPlayerIDs:
            playerName = client.get_user(playerID).name
            LoveLetter(playerID, (await reaction.message.channel.create_thread(name=(playerName+"s-thread"), invitable=False)).id, playerName)
        LoveLetter.setupSeats(LLPlayers)
        boardState = "The board state is as follows"
        for player in LLPlayers:
            await client.get_channel(player.threadID).add_user(client.get_user(player.playerID))
            await client.get_channel(LLChats[0]).add_user(client.get_user(player.playerID))
            boardState += "\n"+ player.name + ('(💌' if player.alive else '(😵') + "): ["
            tempDiscards=''
            for disCard in player.discarded:
                tempDiscards+=str(disCard)+", "
            tempDiscards = tempDiscards.rstrip(" ,")
            boardState+=tempDiscards+"]"
            #print("finished first loop")
        boardStateAlt = boardState + "\nIt is "
        boardState += "\nIt is " + LLPlayers[LoveLetter.activePlayer].name+"'s turn"
        if True:
            boardStateAlt += LLMentionDict[LLPlayers[LoveLetter.activePlayer].name] + "'s turn"
        else:
             boardStateAlt +=LLPlayers[LoveLetter.activePlayer].name+"'s turn"
        boardState += "\nThere are "+str(len(LoveLetter.deck))+" cards left in the deck (and 1 set aside)"
        boardStateAlt += "\nThere are "+str(len(LoveLetter.deck))+" cards left in the deck (and 1 set aside)"
        for player in LLPlayers:
            #print("entered second loop")
            if player.seatNum == LoveLetter.activePlayer:
                specificStuff = "\n\nYou drew a " + LLCardDict[player.drawCard]+"\nYour cards are a "+LLCardDict[player.holdCard]+", and a "+LLCardDict[player.drawCard]
                specificStuff += "\nPlease format your response as <#> <targetName as found above> <guess # (for guard)>"
            else:
                specificStuff = "\n\nYour card is a "+LLCardDict[player.holdCard]
            #print(boardState+specificStuff)
            await client.get_channel(player.threadID).send(boardState + specificStuff)
        await client.get_channel(LLChats[0]).send(boardStateAlt)
            
        
        return


@client.event
async def on_message(message):
    global sentPrimary, LLPlayerIDs, LLPlayers, LLStartMessageID, LLPlayerDict, LLCardDict, LLMentionDict, LLChats, LLNeedsPing
    if message.author == client.user:
        return
    contents = message.content.split()
    smolContents = []
    for string in contents:
        smolContents.append(string.lower())
    endWord = contents[len(contents)-1].strip("_*,.!;'/\\?)("+'"')

    for player in LLPlayers:
        if message.channel.id == player.threadID and LoveLetter.active:
            if player.seatNum == LoveLetter.activePlayer:
                #check if valid play
                if len(player.chancellorCards) > 0:
                    destructibleCopy = player.chancellorCards.copy()
                    validInputs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
                    invalidCards = []
                    if len(contents) != (len(player.chancellorCards)-1):
                        await message.channel.send("Expected "+str(len(player.chancellorCards)-1)+" arguments, "+str(len(contents))+" provided")
                        return
                    if not contents[0] in validInputs:
                        errorSendBack = contents[0]
                        if len(contents) == 2 and (not contents[1] in validInputs):
                            errorSendBack += " and "+contents[1]
                        await message.channel.send(errorSendBack+" is not valid format for your cards. Please type just the number seperated by a space if necessary")
                        return
                    elif len(contents) == 2 and (not contents[1] in validInputs):
                        await message.channel.send(contents[1]+" is not a valid format for your cards. Please type just the number seperated by a space if necessary")
                        return
                    validPlay = True
                    for i in range(len(player.chancellorCards)-1):
                        if int(contents[i]) in destructibleCopy:
                            destructibleCopy.remove(int(contents[i]))
                        else:
                            validPlay = False
                            invalidCards.append(contents[i])
                    if validPlay:
                        player.holdCard = destructibleCopy[0]
                        toSelf = "You hold onto the "+LLCardDict[player.holdCard]+", putting the " +LLCardDict[contents[0]]
                        LoveLetter.deck.append(int(contents[0]))
                        if len(contents)==2:
                            toSelf += " as the penultimate card in the deck, and the "+LLCardDict[contents[1]]
                            LoveLetter.deck.append(int(contents[1]))
                        toSelf +=" as the final card"
                        await message.channel.send(toSelf)
                        player.chancellorCards = []
                        for textchannel in LLChats:
                            await client.get_channel(textchannel).send(player.name+"'s Chancellor(6) finished their administrative business with the deck")
                        contents[0] = -2
                    else:
                        toSendBack = invalidCards[0]
                        if len(invalidCards) == 2:
                            toSendBack += " and "+invalidCards[1]
                        await message.channel.send("You do not have access to "+toSendBack)
                        return
                    
                else:
                    targetCards = ["1", "2", "3", "5", "7"]
                    validGuess = ['0', '2', '3', '4', '5', '6', '7', '8', '9']
                    cards = [str(player.holdCard), str(player.drawCard)]
                    if not (contents[0] in cards):
                        await message.channel.send(contents[0]+" is not one of your cards.")
                        return
                    if contents[0] in targetCards:
                        validTargets = []
                        for activePlayer in LLPlayers:
                            if activePlayer.alive and not activePlayer.shielded:
                                validTargets.append(activePlayer.name)
                        if len(contents) < 2 or (len(contents) < 3 and contents[0] == '1'):
                            if not (len(validTargets) == 1 and contents[0] != '5'):
                                await message.channel.send("Too few arguments.")
                                return
                        if (cards.count('8') == 1 and (contents[0] == '5' or contents[0] == '7')):
                            await message.channel.send("Cannot play "+LLCardDict[contents[0]]+" with a Countess(8) in hand")
                            return
                        
                        if len(contents) == 1 and len(validTargets) == 1 and contents[0] != '5':
                            if cards.index(contents[0]) == 0:
                                player.holdCard = player.drawCard
                            player.drawCard = -1
                            player.discarded.append(int(contents[0]))
                            for allPlayers in LLPlayers:
                                await client.get_channel(allPlayers.threadID).send(player.name+" played their "+LLCardDict[contents[0]]+", but with no valid targets, nothing happened")
                                
                            contents[0] = '-1'
                            
                        else:
                            print('"'+contents[1]+'" "'+player.name+'"')
                            if contents[1] == "self":
                                contents[1] == player.name
                            if validTargets.count(contents[1]) == 0:
                                await message.channel.send(contents[1]+" is not a valid target.\n(If not a Prince(5), and no valid targets, retry without a target. Prince can target self)")
                                return
                            if contents[0] != '5' and contents[1] == player.name:
                                await message.channel.send("Cannot target yourself with a "+LLCardDict[contents[0]])
                                return
                            if contents[0] == '1' and contents[2] == '1':
                                await message.channel.send("Guards(1) cannot inspect other guards")
                                return
                            if contents[0] == '1' and not (contents[2] in validGuess):
                                await message.channel.send(contents[2]+" is not a valid guess")
                                return
                    
                print("successfully got past validity check")
                match contents[0]:
                    case '0':
                        if cards.index('0') == 0:
                            player.holdCard = player.drawCard
                        player.drawCard = -1
                        player.discarded.append(0)
                        for chats in LLChats:
                            await client.get_channel(chats).send(player.name+" played a Spy(0)")
                    case '1':
                        if cards.index('1') == 0:
                            player.holdCard = player.drawCard
                        player.drawCard = -1
                        player.discarded.append(1)
                        target = LLPlayerDict[contents[1]]
                        toSend = player.name+" played a Guard(1) on "+target.name+", attempting to seize a letter from a "+LLCardDict[contents[2]]+"."
                        if contents[2] == str(target.holdCard):
                            target.discarded.append(target.holdCard)
                            target.holdCard = -1
                            target.alive = False
                            await client.get_channel(target.threadID).send("A Guard(1) seized your letter!")
                            toSend +="\nThe Guard(1) found their target! "+target.name+" is out"
                        else:
                            toSend+="\nBut the Guard didn't find the letter"
                        for chats in LLChats:
                            await client.get_channel(chats).send(toSend)
                        
                    case '2':
                        if cards.index('2') == 0:
                            player.holdCard = player.drawCard
                        player.drawCard = -1
                        player.discarded.append(2)
                        target = LLPlayerDict[contents[1]]
                        await message.channel.send("The Priest(2) lets slip that "+target.name+"'s letter is being carried by a "+LLCardDict[target.holdCard])
                        await client.get_channel(target.threadID).send("Your "+LLCardDict[target.holdCard]+" remembers they told "+\
                                                                       player.name+"'s Priest(2) they were carrying your letter. Oops")
                        for chat in LLChats:
                            await client.get_channel(chat).send(player.name+" played a Priest(2) on "+contents[1]+", dicovering their card")
                    case '3':
                        if cards.index('3') == 0:
                            player.holdCard = player.drawCard
                        player.drawCard = -1
                        player.discarded.append(3)
                        target = LLPlayerDict[contents[1]]
                        toTarget = player.name+"'s Baron(3) confronts your letter carrier"
                        toSelf = "Your Baron(3) confronts "+target.name+"'s letter carrier"
                        toAll = player.name+" played a Baron(3) on "+target.name
                        compare = int(player.holdCard)-int(target.holdCard)
                        if compare < 0:
                            toSelf+="\nBut your "+LLCardDict[player.holdCard]+" was no match for their "+LLCardDict[target.holdCard]+"!"
                            toTarget+="\nBut your "+LLCardDict[target.holdCard]+" made quick work of their "+LLCardDict[player.holdCard]+"!"
                            toAll+="\nBut "+target.name+" made quick work of "+player.name+"'s "+LLCardDict[player.holdCard]+"! "+player.name+" is out"
                            player.discarded.append(player.holdCard)
                            player.holdCard = -1
                            player.alive = False
                        elif compare > 0:
                            toTarget+="\nBut your "+LLCardDict[target.holdCard]+" was no match for their "+LLCardDict[player.holdCard]+"!"
                            toSelf+="\nBut your "+LLCardDict[player.holdCard]+" made quick work of their"+LLCardDict[target.holdCard]+"!"
                            toAll+="\n"+target.name+"'s "+LLCardDict[target.holdCard]+" was no match for "+player.name+"! "+target.name+" is out"
                            target.discarded.append(target.holdCard)
                            target.holdCard = -1
                            target.alive = False
                        else:
                            toTarget+="\nBut your "+LLCardDict[player.holdCard]+"s were equally matched!"
                            toSelf+="\nBut your "+LLCardDict[player.holdCard]+"s were equally matched!"
                            toAll+="\nBut they were equally matched!"
                        for allPlayers in LLPlayers:
                            if allPlayers == player:
                                await client.get_channel(allPlayers.threadID).send(toSelf)
                            elif allPlayers == target:
                                await client.get_channel(allPlayers.threadID).send(toTarget)
                        for chat in LLChats:
                            await client.get_channel(chat).send(toAll)
                            
                        
                    case '4':
                        if cards.index('4') == 0:
                            player.holdCard = player.drawCard
                        player.drawCard = -1
                        player.discarded.append(4)
                        player.shielded = True
                        for chat in LLChats:
                            await client.get_channel(chat).send(player.name+" played a Handmaid(4), and cannot be targeted until their next turn")
                    case '5':
                        if cards.index('5') == 0:
                            player.holdCard = player.drawCard
                        player.drawCard = -1
                        player.discarded.append(5)
                        target = LLPlayerDict[contents[1]]
                        cardGon = LLCardDict[target.holdCard]
                        target.discarded.append(target.holdCard)
                        target.holdCard = -1
                        if cardGon == 'Princess(9)':
                            await client.get_channel(target.threadID).send("A Prince(5) made you discard your "+cardGon+\
                                                                           "! Siblings, right?")
                            target.alive = False
                            cardGon+= ", brutal. "+target.name+" is out"
                        elif len(LoveLetter.deck) == 0:
                            target.holdCard = LoveLetter.setAside
                            await client.get_channel(target.threadID).send("A Prince(5) made you discard your "+cardGon+\
                                                                     "!. You've drawn the set-aside card, a "+LLCardDict[target.holdCard])
                        else:
                            target.holdCard = LoveLetter.deck.pop(0)
                            await client.get_channel(target.threadID).send("A Prince(5) made you discard your "+cardGon+\
                                                                     "!. You've drawn a "+LLCardDict[target.holdCard])
                        for chat in LLChats:
                            await client.get_channel(chat).send(player.name+" played a Prince(5) on "+contents[1]+\
                                                                               ", discarding their "+cardGon)
                    case '6':
                        if cards.index('6') == 0:
                            player.holdCard = player.drawCard
                        player.drawCard = -1
                        player.discarded.append(6)
                        if len(LoveLetter.deck) == 0:
                            for chat in LLChats:
                                await client.get_channel(chat).send(player.name+" played a Chancellor(6), but with the empty deck, nothing happens")
                        elif len(LoveLetter.deck) == 1:
                            for chat in LLChats:
                                await client.get_channel(chat).send(player.name+" played a Chancellor(6), drawing the last remaining card in the deck. "+\
                                                                                   "They'll put one card back into the deck")
                            player.chancellorCards.append(player.holdCard)
                            player.chancellorCards.append(LoveLetter.deck.pop(0))
                            toPlayer = 'Your cards, of which you need to specify one to back to become the deck, are a '+\
                                       LLCardDict[player.chancellorCards[0]]+" and a "+LLCardDict[player.chancellorCards[1]]+"."
                            await message.channel.send(toPlayer)
                            return
                        else:
                            for chat in LLChats:
                                await client.get_channel(chat).send(player.name+" played a Chancellor(6), drawing an additional two cards. "+\
                                                                                   "They'll put two cards back at the bottom of deck in the order they choose")
                            player.chancellorCards.append(player.holdCard)
                            player.chancellorCards.append(LoveLetter.deck.pop(0))
                            player.chancellorCards.append(LoveLetter.deck.pop(0))
                            toPlayer = 'Your cards, of which you need to specify 2 to send back in the order "<# of 2nd to bottom> <# of bottom>", are a '+\
                                       LLCardDict[player.chancellorCards[0]]+", a "+LLCardDict[player.chancellorCards[1]]+", and a "+\
                                       LLCardDict[player.chancellorCards[2]]+"."
                            await message.channel.send(toPlayer)
                            return
                    case '7':
                        if cards.index('7') == 0:
                            player.holdCard = player.drawCard
                        player.drawCard = -1
                        temp = player.holdCard
                        for otherPlayer in LLPlayers:
                            if otherPlayer.name == contents[1]:
                                target = otherPlayer
                                player.holdCard = otherPlayer.holdCard
                                otherPlayer.holdCard = temp
                        player.discarded.append(7)
                        await client.get_channel(target.threadID).send(player.name+"'s King swapped your "+ LLCardDict[player.holdCard] +" with their "+ LLCardDict[target.holdCard]+"!")
                        await message.channel.send("Your King swapped your "+ LLCardDict[target.holdCard] +" with "+target.name +"'s "+LLCardDict[player.holdCard]+"!")
                        for chat in LLChats:
                            await client.get_channel(chat).send(player.name+" played the King(7) on "+contents[1]+", swapping their hands!")
                    case '8':
                        if cards.index('8') == 0:
                            player.holdCard = player.drawCard
                        player.drawCard = -1
                        player.discarded.append(8)
                        for chat in LLChats:
                            await client.get_channel(chat).send(player.name+" played the Countess(8)")
                    case '9':
                        player.discarded.append(player.drawCard)
                        player.drawCard = -1
                        player.discarded.append(player.holdCard)
                        player.holdCard = -1
                        player.alive = False
                        for chat in LLChats:
                            await client.get_channel(chat).send(player.name+" played the Princess(9)\nBold strategy, we'll see if it pays off")
                        
                alive = 0
                for aliveCheck in LLPlayers:
                    if aliveCheck.alive:
                        alive+=1
                if alive == 1 or len(LoveLetter.deck) == 0:
                    boardState = "The final board state was as follows"
                    for boardPlayer in LLPlayers:
                        boardState += "\n"+ boardPlayer.name + ('( **'+str(boardPlayer.holdCard)+'**: 💌' if boardPlayer.alive else '(😵') + "): ["
                        tempDiscards=''
                        for disCard in boardPlayer.discarded:
                            tempDiscards+=str(disCard)+", "
                        boardState+=tempDiscards.rstrip(" ,")+"]"
                    winReport = LoveLetter.endRound()
                    winner = False
                    for winCheck in LLPlayers:
                        if winCheck.points >= LoveLetter.pointsToWin:
                            winner = True
                    if winner:
                        print("crazy how someone just won")
                        finalToSend = "This game of loveletter has concluded! The # of favor tokens to win was "+str(LoveLetter.pointsToWin)
                        finalToSend += "\n\nIn the final round, the winner(s) were "+" and ".join(winReport[0])
                        finalToSend += "\n"+winReport[1]+" got a point for being the only one with a spy discarded\n\nThe final scores were as follows:"
                        for finalPlayer in LLPlayers:
                            finalToSend += "\n"+finalPlayer.name+": "+"🔴"*finalPlayer.points
                            await client.get_channel(finalPlayer.threadID).delete()
                        await client.get_channel(LLChats[0]).send(finalToSend)
                        await client.get_channel(LLChats[0]).edit(locked = True)
                        await client.get_channel(PRIMARY_ID).send(finalToSend)
                            
                        LoveLetter.active = False
                        LoveLetter.players = 0
                        LoveLetter.activePlayer = 0
                        LoveLetter.firstPlayer = 0
                        LoveLetter.deck = []
                        LoveLetter.pointsToWin = 10
                        LoveLetter.setAside = -1

                        LLPlayerIDs = []
                        LLPlayers = []
                        LLChats = []
                        LLPlayerDict = {}
                        LLMentionDict = {}
                        LLStartMessageID = 0
                        
                        
                        #print results to #primary
                        #reset arrays
                        #set active to false
                        #delete threads
                        return
                    else:
                        stringWinReport = "\n\nThe Winner(s) of that round were "+" and ".join(winReport[0])
                        stringWinReport += "\n"+winReport[1]+" got a point for being the only one with a spy discarded"
                        stringWinReport +="\n\nThe scores are as follow, with "+str(LoveLetter.pointsToWin)+" points required to win"
                        for pointPlayers in LLPlayers:
                            stringWinReport +="\n"+pointPlayers.name+": "+"🔴"*pointPlayers.points
                            pointPlayers.shielded = False
                        for chat in LLChats:
                            await client.get_channel(chat).send(boardState+stringWinReport)
                        LoveLetter.resetRound()
                else:
                    LoveLetter.nextTurn()
                #print board state
                boardState = ('-----'*10+"\n")*4+"The board state is as follows"
                for turnPlayer in LLPlayers:
                    boardState += "\n"+ turnPlayer.name + ('(💌' if turnPlayer.alive else '(😵') + "): ["
                    tempDiscards=''
                    for disCard in turnPlayer.discarded:
                        tempDiscards+=str(disCard)+", "
                    tempDiscards = tempDiscards.rstrip(" ,")
                    boardState+=tempDiscards+"]"
                boardStateAlt = boardState + "\nIt is "
                boardState += "\nIt is " + LLPlayers[LoveLetter.activePlayer].name+"'s turn"
                boardState += "\nThere are "+str(len(LoveLetter.deck))+" cards left in the deck (and 1 set aside)"
                
                if True:
                    boardStateAlt += LLMentionDict[LLPlayers[LoveLetter.activePlayer].name] + "'s turn"
                else:
                    boardStateAlt +=LLPlayers[LoveLetter.activePlayer].name+"'s turn"
                boardStateAlt += "\nThere are "+str(len(LoveLetter.deck))+" cards left in the deck (and 1 set aside)"   
                for turnPlayer in LLPlayers:
                    #print("entered second loop")
                    if turnPlayer.seatNum == LoveLetter.activePlayer:
                        specificStuff = "\n\nYou drew a " + str(turnPlayer.drawCard)+"\nYour cards are a "+str(turnPlayer.holdCard)+", and a "+str(turnPlayer.drawCard)
                        specificStuff += "\nPlease format your response as <#> <targetName as found above> <guess # (for guard)>"
                    elif turnPlayer.alive:
                        specificStuff = "\n\nYour card is a "+str(turnPlayer.holdCard)
                    else:
                        specificStuff = "\n\nYour letter's seal was broken, and are out for this round"
                    #print(boardState+specificStuff)
                    await client.get_channel(turnPlayer.threadID).send(boardState + specificStuff)
                await client.get_channel(LLChats[0]).send(boardStateAlt)
                
                #check if round over IF alive == 1 or len(deck) == 0
                    #check if game over
            else:
                await message.channel.send("Not your turn stfu")
            return
    for blacklisted in BLACKLIST:
        if message.author.id == blacklisted:
            print("didn't respond :)")
            return
    
    if contents[0].startswith('!') and message.channel == client.get_channel(PRIMARY_ID):
        if contents[0] == '!primary':
            auth = False
            for role in message.author.roles:
                if role.name == "bot wrangler":
                    auth = True
            if auth:
                if sentPrimary:
                    await message.channel.send("already sent primary message")
                    return
                justSent = await client.get_channel(IANNOUNCEMENTS_ID).send(ANNOUNCEMENT)
                await justSent.add_reaction('🇲')
                await justSent.add_reaction('🇹')
                await justSent.add_reaction('🇼')
                h_emoji = discord.utils.get(message.guild.emojis, name='_h')
                await justSent.add_reaction(h_emoji)
                await justSent.add_reaction('🇫')
                await justSent.add_reaction('🇸')
                await justSent.add_reaction('☀')
                await justSent.add_reaction('👎')
                contents.pop(0)
                sentPrimary = True
                while len(contents) > 0:
                    curr = contents.pop()
                    if curr == 'gameRequest':
                        justSent = await client.get_channel(IANNOUNCEMENTS_ID).send(REQUEST)
                        await justSent.add_reaction('👍')
                        await justSent.add_reaction('⌛')
                        await justSent.add_reaction('🎉')
                        await justSent.add_reaction('🐑')
                        await justSent.add_reaction('⚔️')
                        await justSent.add_reaction('🔫')
                    elif curr == 'ooga':
                        await message.channel.send("booga")
                return
            
            else:
                await message.channel.send("not authorized sorry bozo :(")
                return
                
        elif contents[0] == '!secondary':
            await message.channel.send("oh we've got a wise-guy I see")
            return

        elif contents[0] == '!commands' or contents[0] == '!help':
            await message.channel.send("figure them out yourself, bozo")

        elif contents[0] == '!please???':
            await message.channel.send("alright alright. You did ask nicely. You can re-send !primary")
            sentPrimary = False
            return

        elif contents[0] == '!loveletter':
            if message.author.id == ETHAN_ID:
                await message.channel.send("h")
            
            if not LoveLetter.active:
                LLPlayerIDs.append(-1)
                LLPlayerIDs.append(message.author.id)
                LLMentionDict[message.author.name] = message.author.mention
                LLStartMessage =  (await message.channel.send("A game of *Love Letter* is starting! If you would like to join (2 to 6 players), "+\
                                                                "please react with a \"✅\". Host (person who ran !loveletter): please react with a \"👍\" to"+\
                                                                " begin the game (or \"👎\" to cancel)\n1. "+message.author.name))
                await LLStartMessage.add_reaction('✅')
                await LLStartMessage.add_reaction('👍')

                LLStartMessageID = LLStartMessage.id
                LoveLetter.active = True

                Rules = discord.Embed(title = "Love Letter Rules", description = "Use this to figure out what exactly your #s do, since it isn't otherwise apparent",url="https://images.zmangames.com/filer_public/5b/6c/5b6c17d7-7e0e-4b70-a311-9a6c32066010/ll-rulebook.pdf")
                await message.channel.send(embed=Rules)
                return
            else:
                await message.channel.send("busy with another game atm")

        elif contents[0] == '!LLjoin' and LoveLetter.active:
            await message.channel.send(":)")
        
        else:
            await message.channel.send('"'+contents[0]+'" is not a recognized command')
            return
        
    if endWord == 'L' and message.channel.id != IANNOUNCEMENTS_ID and message.channel.id != VANNOUNCEMENTS_ID:
        if message.author == client.get_user(ETHAN_ID) and random.randint(0,5) < 2:
            await message.channel.send("bro *really* thought I'd help him ratio. stfu", reference=message, mention_author=False)
            return
        await message.channel.send("+ ratio",reference=message,mention_author=False)
        return

    if endWord == 'h' and message.channel.id != IANNOUNCEMENTS_ID and message.channel.id != VANNOUNCEMENTS_ID:
        #await message.channel.send("h")
        await message.channel.send("<:_h:1108892121332711536>")
        #await message.add_reaction(discord.utils.get(message.guild.emojis, name='_h'))
        return

    if endWord == 'H' and message.channel.id != IANNOUNCEMENTS_ID and message.channel.id != VANNOUNCEMENTS_ID:
        #await message.channel.send("**h.**", reference=message)
        await message.channel.send("<:stareIHardly:1126000789320630362>", reference=message)
        await message.channel.send("**h.**")
        #await message.add_reaction(discord.utils.get(message.guild.emojis, name='stareIHardly'))
        return

    if len(contents) == 3 and contents[0] == 'L' and contents[1] == "+" and contents[2] == "ratio" and message.author.id == ETHAN_ID:
        #await message.channel.send("@cactusbearer")
        return

    if len(contents) == 3 and contents[0] == "shut" and contents[1] == "up" and contents[2] == "leobot":
        await message.channel.send(":(")
        return

    if len(contents) == 2 and contents[0].lower() == "good" and (contents[1].lower() == "bot" or contents[1].lower().strip("?") == "leobot") and message.author.id == LEO_ID:
        await message.channel.send(":smile:")

    if ((endWord.lower().endswith("er") or endWord.lower().endswith("or") or endWord.lower().endswith("re") or endWord.lower().endswith("ur") or endWord.lower().endswith("ar"))\
       and random.randint(0,49)<23) or random.randint(1,250) == 1:
        await message.channel.send(endWord+"?? I hardly know 'er!")
        return
    



#bot do thing
client.run(NotTheRealKey)




    
