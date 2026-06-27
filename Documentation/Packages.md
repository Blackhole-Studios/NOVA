This is a file to describe best practices when it comes to packages.
NOVA is unique when it comes to this, each instance comes with a wifi card and a scratchattach server.
If the OS you're using support this WIFI card, it can access the set server (.py found in /Programs)

With the future OS for the NOVA hardware, NOVA will use the /bin pkg.sh script to install packages found, here.
Therefore, you will be able to install packages from github on your machine.

So, what are packages?
Packages are sort of like plates of food at a restraunt, the Customer (or user in this case), asks the Waiter (or the pkgManager) for a dish of food on the menu
the Waiter then confirms it's a real dish by asking the chef (S.A. Server in this case), if it exists, the chef starts making the food (package) from ingredients (code)
This plate of food is then delivered to the Customer through the Waiter again for the Customer to consume (install/use), creating a way for users to install apps that didn't come with their OS

In NOVA, the 'ingredients' come from the /Packages folder in this GitHub Repository. When your 'waiter' asks the server, it checks that folder for the package you requested.
And because packages are AutoPulled with a worker from Pull Requests, the /packages folder is maintained by a community, without giving total acess to the users.

So, how do I write a package?
Well, the Auto Puller has some constraints, therefore you must abide by these rules:
lines 1, 2, and 3 must say as follows:

vThis is the file you added to the /packages folder, read up on git if you don't really grasp it, it's a DIFF
FileCreationPR: +FILE(pkgname) by user 'Blackhole-Studios'
Start File
```text
NAME='pkgname'
VERSION=1.0
AUTHORS='&ALL&'

--More Lines
```
This shows, whenever you create/modify a package, A: you must keep the NAME field for the package the exact same as the filename, else it's auto rejected, B: you should increment the Version each update, 
technichally it's not required but the users won't be able to update as it's already the most up to date, and C: the userfield must be consistent to your Github username
this is valid even though I am Blackhole-Studios, but the User field says 'ALL', because ALL means any user can update the code, this shouldn't be used too much, as it allows a seperate user to lock the file
then wipe it for example, if you want to add 2 maintainers, ie: both Me and ItsGraphax want to update a package at different times, I can do AUTHORS='&Blackhole-Studios&ItsGraphax&' to allow both of us. 

As of now, the packages don't really have a language, they're just files with that header, I'm still deciding to make them Assembly, Machine, but imo, it should be depdendent on the kernel, so if you want
you can add another line,
```text
--Header
#COMPATIBLE='all but xOS'

--More Lines
```
or
```text
--Header
# This package only works with the VS Cernel

--More Lines
```
this works as '#' means comment, so the line isn't parsed, the top 3 in the header are automatically removed. 
