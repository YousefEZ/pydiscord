# pydiscord

discord.py handler that gets data from python classes and produces embed &amp; menus

make a new .py file, and make a dictionary containing the flow name and its corresponding object
at the end of the file and call it `flows`.

import the response file so if the new response file is tutorial.py (placed in responses dir)
then its
```
from responses import tutorial
```

change the test.flows to the name of your new response file, so if 
tutorial is the new response .py file then change it to tutorial.flows

__for embed tests__
```
!embed_test flow_type
```

__for menu tests__
```
!menu_test main_menu_title
```
