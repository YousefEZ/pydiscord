from discord.ext import commands

from src.handler import Handler
from utils import settings
from host import base
from responses import help as hp

prefix = "!"
bot = commands.AutoShardedBot(command_prefix=prefix)
bot.remove_command("help")

@bot.event
async def on_ready():
    print("*[CLIENT] ON READY, AWAITING COMMANDS")


@bot.command()
async def ping(ctx):
    await ctx.send("[RESPONSE] SUCCESSFUL")


@bot.command()
async def menu_test(ctx, *args):
    """generates an interactive menu that uses reactions to trigger functions.

    Args:
        ctx (object): metadata supplied by discord (automatic)
        file (str): path of the .ini file (absolute or relative)
        *args -> menu_name (str): name of the menu (title of the main menu)
    """


    menu_name = " ".join(args)
    player = base.DummyNation()  # Generates a simulated player.
    handler = Handler(ctx, bot, hp.flows)  # Supplies the data to the handler
    menu = handler.retrieve_menu(menu_name)
    print('*[CLIENT] RETRIEVED MENU')
    await menu.attach_numbers()  # Attach the reactions to change pages
    await menu.deploy_menu(player)  # Sends the menu to the user.

    print('*[CLIENT] EXITING MENU FUNCTION')

@bot.command()
async def help(ctx, request: str = None):

    if request is None:
        request = 'HELP'

    request = request.upper()
    handler = Handler(ctx, bot, hp.flows)
    await handler.display(request, None)


@bot.command()
async def embed_test(ctx, *args):
    """reads the contents from a .ini file and outputs the embedded version.
    example command: !embed_test ../data/example.ini EXAMPLE will run

    Args:
        ctx (object): metadata supplied by discord (automatic)
        file (str): contains the file relative to the bot's directory (e.g. "../data/command.ini")
        *args -> flow (str): contains the flow state that you wish to display (e.g. "SUCCESS")
    """

    flow = ' '.join(args)
    player = base.DummyNation()
    handler = Handler(ctx, bot, hp.flows)
    await handler.display(flow, player)
    print('*[CLIENT] EXITING EMBED FUNCTION')


@bot.event
async def on_message(message):
    if message.content.startswith('!'):
        await bot.process_commands(message)


if __name__ == "__main__":
    print("*[CLIENT] RUNNING BOT")
    bot.run(settings.TOKEN)
