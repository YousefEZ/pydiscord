# discord-handler version 2

discord.py handler that gets data from python classes and produces embed &amp; menus

Run the following command into the terminal
```
pip3 install discord.py
```
to install discord.py API.

make a new .py file, and make a dictionary containing the flow name and its corresponding object
at the end of the file and call it `flows`.

change the responnse.help.flows to the name of your new response file, so if 
tutorial is the new response .py file then change it to response.tutorial.flows

__for embed tests__
```
!embed_test flow_type
```

__for menu tests__
```
!menu_test main_menu_title
```

CREATED BY: Yousef Zaher for SyberWatch (Discord Bot)
