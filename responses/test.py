import sys, inspect

class Tutorial:
    flow = "TUTORIAL"
    type = "embed"
    title = "__TUTORIAL HELP__"
    colour = "green"
    def __init__(self, player=None): 

        self.fields = (('Official Discord Server:',
                   '''
                   https://discord.com/invite/discord-developers
        
                   **-**`tutorial`: :mortar_board: A simple tutorial for how the bot works.
        
                   ''', False))
        self.footer_text = "\u00A9 2018 | Bot"
        self.footer_icon = "https://1000logos.net/wp-content/uploads/2020/10/Discord-emblem.jpg"
        self.thumbnail = ""
        self.image = ""
    pointer = None


class P1:
    flow = "p1"
    type = "menu"
    title = "Tutorial HELP CONT.__"
    colour = "blue"
    def __init__(self, player=None): 

        self.fields = (("https://discord.com/invite/discord-developers",
                   """
                   https://discord.com/invite/discord-developers                   """))
        self.footer_text = "\u00A9 2018 | Bot"
        self.footer_icon = "https://1000logos.net/wp-content/uploads/2020/10/Discord-emblem.jpg"
        self.thumbnail = "https://1000logos.net/wp-content/uploads/2020/10/Discord-emblem.jpg"
        self.image = ""
    pointer = None


class P2:
    flow = "p2"
    type = " main menu"
    title = "__Tutorial HELP__"
    colour = "blue"
    def __init__(self, player=None):

        self.fields = (("Official Discord Server:",
                   """
    
                   https://discord.com/invite/discord-developers
                   """))
        self.footer_text = "\u00A9 2018 | Bot"
        self.footer_icon = "https://1000logos.net/wp-content/uploads/2020/10/Discord-emblem.jpg"
        self.thumbnail = "https://1000logos.net/wp-content/uploads/2020/10/Discord-emblem.jpg"
        self.image = "https://1000logos.net/wp-content/uploads/2020/10/Discord-emblem.jpg"
    pointer = P1


# Automatically reads and assigns flows.
flows = {}
for a, obj in inspect.getmembers(sys.modules[__name__]):
    try:
        flows[obj.flow] = obj
    except AttributeError:
        pass
