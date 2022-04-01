import discord
import random
import os

Kima = discord.Bot()


def diceParser(dice):
    error = "Error. Please make sure you enter the format `/roll [1-750]d[1-100000]`."
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

        if amount < 1 or domain < 1 or amount > 750 or domain > 100000:
            return error

        rolls = []
        for diceToRoll in range(amount):
            result = random.randint(1, domain)
            rolls.append(result)
        total = sum(rolls) + modifier
        response = f"Your rolled: {dice}\n" \
                   f"Your rolls are: {rolls}\n" \
                   f"Your total is: {total}"
        return response

    except (ValueError, TypeError):
        return error


@Kima.event
async def on_ready():
    print(f"We have logged in as {Kima.user}")


@Kima.slash_command()
async def roll(ctx, dice):
    print(dice)
    output = diceParser(dice)
    await ctx.respond(output)

TOKEN = os.environ.get('TOKEN')
Kima.run(TOKEN)