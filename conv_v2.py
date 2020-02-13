import vk,time
tokenlist = input("TOKEN LINK:")
token1 = tokenlist.rsplit("access_token=")
token2 = token1[1].rsplit("&")
token = token2[0]
idconv = int(input("Conversation ID:"))
peerid=(2000000000+idconv)
sess = vk.Session(access_token=token)
api = vk.API(sess,v='5.103',lang='ru')
allmembers = str(api.messages.getConversationMembers(peer_id=peerid,fields='online'))
members1=allmembers.rsplit(" {'id': ")
members1[0]=members1[1]
memberslen = len(members1)
members1ids = []
members1name = []
message = "Онлайн сейчас:\n"

for n in range(1,memberslen):
	if "'online': 1" in members1[n]:
		members1name0=members1[n].rsplit("'first_name': '")
		members1name1=members1name0[1].rsplit("', 'l")
		members1name.append(members1name1[0])
		members1ids0=members1[n].rsplit(", 'f")
		members1ids.append(members1ids0[0])
names1len=len(members1name)
print(names1len)
print(members1ids)
for n in range(0,names1len):
	message+=("[id"+members1ids[n]+"|"+members1name[n]+"] ")

try(api.messages.send(random_id=int(time.time()*388),peer_id=peerid,message=str(message)))