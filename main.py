import genshin
import asyncio
import checkin
import info
import notify
from datetime import datetime
import pytz
import os

ltuid = os.environ.get("ltuid")
ltoken = os.environ.get("ltoken")

list_ltuid = ltuid.split("#")
list_ltoken = ltoken.split("#")

async def main():
    desp = ""
    num_of_account = len(list_ltuid)
    tz = pytz.timezone("Singapore")
    datetoday = datetime.now(tz).strftime("%B %d, %Y")
    print(datetoday)
    for i in range (len(list_ltuid)):
        ltuid = list_ltuid[i]
        ltoken = list_ltoken[i]
        client = genshin.Client(game=genshin.Game.GENSHIN, region=genshin.Region.OVERSEAS)
        try:
            cookies = client.set_cookies({"ltuid": ltuid, "ltoken": ltoken}) # mapping
            nickname, server, ar, uid = await info.genshin_profile(client)
            print(f"Daily Checkin for {nickname} - {uid}")
            reward_name, reward_amount, signed, total_signed = await checkin.daily(client)
            if signed == True:
                signed = "OK"
            else:
                pass
            i+=1
            desp_add = f"""
            No.{i} Account:
            ###########{datetoday}###########

            {nickname} - {ar}
            [{server}] {uid}
            Today's rewards: {reward_name} x {reward_amount}
            Monthly Check-in count: {total_signed} days
            Check-in result: {signed}

            ###############################

            """
            desp += str(desp_add)

        except BaseException as e:
            # i+=1
            desp_add = f"""
            No.{i} Account:
            ###########{datetoday}###########

            {e}

            ###############################

            """
            print(e)
            desp += str(desp_add)
            continue
    await notify.discord(desp, num_of_account)
    

if __name__ == "__main__":
    asyncio.run(main())
    