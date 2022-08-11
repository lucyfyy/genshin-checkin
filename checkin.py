import genshin

async def daily(client):
    try:
        reward = await client.claim_daily_reward()
    except genshin.AlreadyClaimed:
        reward = await client.claimed_rewards()
        signed_in, claimed_rewards = await client.get_reward_info()
        signed_in="Traveler, you've already checked in today"
        print("Daily reward already claimed")
        return reward[0].name, reward[0].amount, signed_in, claimed_rewards
    else:
        print(f"Claimed {reward.amount}x {reward.name}")
        signed_in, claimed_rewards = await client.get_reward_info()
        return reward.amount, reward.name, signed_in, claimed_rewards