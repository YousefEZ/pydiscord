from discord.ext import commands

from src.handler import Handler
from utils import settings
from host import base
from responses import help

prefix = "!"
bot = commands.AutoShardedBot(command_prefix=prefix)

@bot.event
async def on_ready():
    print("*[CLIENT] ON READY, AWAITING COMMANDS")


@bot.command()
async def ping(ctx):
    await ctx.send("[RESPONSE] SUCCESSFUL")


@bot.command()
async def menu_test(ctx, *args):
    """generates an interactive menu that uses reactions to trigger functions.
       !menu_test ALLIANCE
       
    Args:
        ctx (object): metadata supplied by discord (automatic)
        file (str): path of the .ini file (absolute or relative)
        *args -> menu_name (str): name of the menu (title of the main menu)
    """

    try:
        menu_name = " ".join(args)
        player = base.DummyNation()  # Generates a simulated player.
        handler = Handler(ctx, bot, help.flows, player)  # Supplies the data to the handler
        menu = handler.retrieve_menu(menu_name)
        await menu.attach_numbers()  # Attach the reactions to change pages
        await menu.deploy_menu(ctx, bot)  # Sends the menu to the user.
    except Exception as e:
        print(f"!![MAIN][ERROR] {e}")
    print('*[CLIENT] EXITING MENU FUNCTION')


@bot.command()
async def embed_test(ctx, *args):
    """reads the contents from a .ini file and outputs the embedded version.
    example command: !embed_test TUTORIAL will run

    Args:
        ctx (object): metadata supplied by discord (automatic)
        file (str): contains the file relative to the bot's directory (e.g. "../data/command.ini")
        *args -> flow (str): contains the flow state that you wish to display (e.g. "SUCCESS")
    """

    try:
        flow = ' '.join(args)
        player = base.DummyNation()
        handler = Handler(ctx, bot, help.flows, player)
        await handler.display(flow)
    except Exception as e:
        print(f"!![MAIN][ERROR] {e}")
    print('*[CLIENT] EXITING EMBED FUNCTION')


@bot.event
async def on_message(message):
    if message.content.startswith('!'):
        await bot.process_commands(message)


if __name__ == "__main__":
    print("*[CLIENT] RUNNING BOT")
    bot.run(settings.TOKEN)
