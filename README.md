# KlayoutNetworkX
Klayout Routing with NetworkX
Utilizing Klayout and NetworkX to realize a basic router for Klayout

About Klayout 
KLayout - Your Mask Layout Friend
https://www.klayout.de/

About NetworkX
https://networkx.org/

NetworkX is a Python package for the creation,
manipulation, and study of the structure, 
dynamics, and functions of complex networks.


Following files and package are in this git
````
networkx
ArrayLabels.lym
decorator.py
NX_ROUTE.lym
Nx_Router.py
TGPcell.lym
tech.lyp
TestingRoute.gds
````

Copy networkx python package and decorator.py
to the following location of your Klayout Installation in Windows
C:\Users\your_path\AppData\Roaming\KLayout\lib\python3.7

For the Python and Ruby files you will need to install at these locations
Python goes into C:\Users\your_path\KLayout\pymacros
NX_ROUTE.lym
Nx_Router.py

Ruby goes into C:\Users\your_path\KLayout\macros
ArrayLabels.lym
TGPcell.lym

You will need to install Matthias great demo pdk
and copy it too C:\Users\your_path\KLayout\salt
Copy the tech.lyp file to C:\Users\your_path\KLayout\salt\si4all


Once all copied load Klayout if every thing is in place load
the GDS file TestingRoute.gds, on the Macro menu you should see the following
Macros
---> Create Label of Pins
---> Load Router

Create Label of Pins allows you to create array's of Text Pins in the layout
Load Router loads the Router and puts a Toolbar selection called NxRouter
The Pcell uses the 1000 marking layer as Pin targets , feel free to move the Pin's
around to test .

To route the demo TestingRoute.gds click the NxRouter in the toolbar
