import time,os,random
from telethon import TelegramClient
from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
print("</>  </> ")
ch = "@JOKER_CHKBOT"
api_id = '15372008'
api_hash = 'ed85c35370cffb1e2cf050e44e635d26'
client = TelegramClient('session', api_id, api_hash)
client.start()
for cc in open("F4.txt").read().split("\n"):
    try:
        client.send_message(ch ,f"/chk {cc}")
        time.sleep(random.randint(22,25))
        mssag = client.get_messages(ch, limit=1)
        if "ANTI_SPAM" in str(mssag[0].message):
            t = str(mssag[0].message).split("again after ")[1]
            t = t.split("seconds")[0]
            t = int(t)
            print(f"Done Sleep : {t+2}")
            time.sleep(t+2)
        print(mssag[0].message)
        time.sleep(1)
    except:
        print(False)
