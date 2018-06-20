# Environement Setup 

Follow the instructions carefully for completing the environement setup for MAC and Linux Users. 

1. git clone https://github.com/ByteAcademyIn/Environment_Setup.git
2. cd Environment_Setup
3. For Full Stack Web Development Track - ./environment_setup.sh FULL_STACK_WEB 
4. For Data Science Track - ./environment_setup.sh DATA_SCIENCE

You must see "Welcome to Byte Dev. Ready to Rock n Roll"

For Windows Users

## Windows

### Git

Download and install [Git for Windows](https://msysgit.github.io/), then open the new-installed Git Bash and follow the Git config instructions below.

### Python

You can follow [these instructions](http://docs.python-guide.org/en/latest/starting/install3/win/) to install Python and setuptools/pip on Windows.

To update your PATH without powershell (so it is easier to run Python scripts from the command line), follow these steps:

1. From your desktop/the start menu, right-click on Computer and choose Properties.
2. Select "Advanced System Settings" in the dialog box, and then "Environment Variables".
3. Edit the PATH statement in the User Variables section to add:
```
C:\Python36;C:\Python36\Lib\site-packages\;C:\Python36\Scripts\;
```

### Alternate approach: use a virtual machine

Another option for working on windows is to use a virtual machine like [VirtualBox](https://www.virtualbox.org/) and install Linux on it. VirtualBox is an "emulator" that runs a fake Linux machine on top of your Windows machine. If you've never used Linux before, we recommend using [Ubuntu](http://www.ubuntu.com/download/desktop).

Once you've installed VirtualBox and a Linux distribution, you can follow the Linux instructions.
