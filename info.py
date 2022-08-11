async def genshin_profile(client):
    info = await client.get_record_cards()
    return info[0].nickname, info[0].level, info[0].server_name, info[0].uid
