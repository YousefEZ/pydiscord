import sys, inspect

class Tutorial:
    flow = "TUTORIAL"
    type = "embed"
    title = "__TUTORIAL HELP__"
    colour = "green"
    def __init__(self, player=None): 

        self.fields = (('Official Discord Server:',
                   '''
                   https://discord.gg/YDSDuHg
        
                   **-**`tutorial`: :mortar_board: A simple tutorial for how the League of Nations bot works.
        
                   ''', False))
        self.footer_text = "\u00A9 2018 | LoN Bot"
        self.footer_icon = "https://cdn.discordapp.com/avatars/449719890312691715/f4ed4549080d4925f4954cf5077620b1.png"
        self.thumbnail = ""
        self.image = ""
    pointer = None


class P1:
    flow = "p1"
    type = "menu"
    title = "__ALLIANCE HELP CONT.__"
    colour = "blue"
    def __init__(self, player=None): 

        self.fields = (("https://discord.gg/YDSDuHg",
                   """
                   \u200b
                   **-**`alliance set flag <url>`: :flag_fr: Sets the flag for your alliance. (Requires __leadingstate__ permissions).
        
                   **-**`alliance promote @mention <role>`: :arrow_up: Promote a member in the alliance to that specific role. (Requires __coleadingstate__ permissions or above).
        
                   **-**`alliance demote @mention <role>`: :arrow_down: Demote a member in the alliance from that specific role. (Requires __coleadingstate__ permissions or above).
        
                   **-**`alliance sanction nation @mention`: :x: Sanction a nation preventing them from __trading__ & __aiding__ with the alliance members. (Requires __coleadingstate__ permissions or above).
        
                   **-**`alliance sanction lift nation @mention`: :ballot_box_with_check: Remove a sanction from a nation.
        
                   **-**`alliance leave`: :warning: Leave an alliance (__confirm__ afterwards).
        
                   __***Notes***__: Alliance roles include the following - __leadingstate__, __coleadingstate__, __bankingstate__, __peacekeepingstate__ and __inventationalstate__.
        
                   """))
        self.footer_text = "\u00A9 2018 | LoN Bot"
        self.footer_icon = "https://cdn.discordapp.com/avatars/449719890312691715/f4ed4549080d4925f4954cf5077620b1.png"
        self.thumbnail = "https://cdn.discordapp.com/attachments/729711470773797016/749779020174065674/Untitled.png"
        self.image = ""
    pointer = None


class Alliance:
    flow = "ALLIANCE"
    type = " main menu"
    title = "__ALLIANCE HELP__"
    colour = "blue"
    def __init__(self, player=None):

        self.fields = (("Official Discord Server:",
                   """
    
                   https://discord.gg/YDSDuHg
    
                   **-**`alliance create`: :beginner: Create an in game alliance. (Specify __alliance name__ and __confirm__ afterwords. Alliance creation costs `12.5 Million`).
    
                   **-**`alliance invite @mention`: :white_check_mark: Invite someone into your alliance. (Requires __invitationalstate__ permissions or above).
    
                   **-**`alliance view <alliance name>`: :family_mwg: View members in an alliance.
    
                   **-**`alliance view bank`: :pound: View alliance funds. (Requires __bankingstate__ permissions or higher). You can withdraw up to a maximum of `10 Million` per withdrawal, but this maximum decreases as your tech level/amount rises. You accept the alliance aid package via the **-**`aid` command.
    
                   **-**`alliance view invites`: :information_source: View your current alliance invites.
    
                   **-**`alliance contribute funds <# amount>`: :moneybag: Contribute money into your alliance.
    
                   **-**`alliance set flag <url>`: :flag_hm: Sets the flag for your alliance. (Requires __leadingstate__ permissions).
    
                   """))
        self.footer_text = "\u00A9 2018 | LoN Bot"
        self.footer_icon = "https://cdn.discordapp.com/avatars/449719890312691715/f4ed4549080d4925f4954cf5077620b1.png"
        self.thumbnail = "https://cdn.discordapp.com/attachments/729711470773797016/749779020174065674/Untitled.png"
        self.image = "https://cdn.discordapp.com/attachments/729711470773797016/794636506802946078/rsz_logo.png"
    pointer = P1


# Automatically reads and assigns flows.
flows = {}
for a, obj in inspect.getmembers(sys.modules[__name__]):
    try:
        flows[obj.flow] = obj
    except AttributeError:
        pass
