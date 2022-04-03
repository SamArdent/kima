import discord
import random
import os

TOKEN = os.environ.get('TOKEN')
MODMAIL_CHANNEL_ID = os.environ.get('MODMAIL_CHANNEL_ID')

Kima = discord.Bot()


def diceParser(dice):
    error = "Error. Please make sure you follow the format `/roll [1-200]d[1-100000]`."
    modifier = 0
    try:
        amountDomain = dice.split('d')
        amount = int(dice.split('d')[0])

        if "+" in dice:
            modifier = int(dice.split('+')[1])
            domain = int(dice.split('d')[1].split('+')[0])

        elif "-" in dice:
            modifier = int(dice.split('-')[1]) * -1
            domain = int(dice.split('d')[1].split('-')[0])

        else:
            domain = int(amountDomain[1])

        if amount < 1 or domain < 1 or amount > 200 or domain > 100000:
            return error

        rolls = []
        for diceToRoll in range(amount):
            result = random.randint(1, domain)
            rolls.append(result)
        total = sum(rolls) + modifier
        response = f"You rolled {amount}d{domain}{modifier}\n" \
                   f"Your rolls are: {rolls}\n" \
                   f"Your total is: {total}"
        return response

    except (ValueError, TypeError):
        return error


@Kima.event
async def on_ready():
    print(f"We have logged in as {Kima.user}")


@Kima.slash_command()
async def dice(ctx, input):
    print(input)
    output = diceParser(input)
    await ctx.respond(output)

@Kima.event
async def on_message(ctx):
    if ctx.channel.type == discord.ChannelType.private:
        channel = await Kima.fetch_channel(MODMAIL_CHANNEL_ID)
        await channel.send(ctx.content)


Kima.run(TOKEN)