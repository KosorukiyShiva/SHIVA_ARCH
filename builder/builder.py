import os
import package 
from logger import Logger, LoggerStatus
from builder.software import AurBuilder, FirefoxCustomize
from builder.drivers import GraphicDrivers
from builder.patches import PatchSystemBugs
from builder.daemons import Daemons

class SystemConfiguration:
    @staticmethod
    def start(*args):
        start_text = f"[+] Starting assemly. Options {args}"
        Logger.add_record(start_text, status=LoggerStatus.SUCCESS)
        if args[0]: SystemConfiguration.__start_option_1()
        if args[1]: SystemConfiguration.__start_option_2()
        if args[2]: SystemConfiguration.__start_option_3()
        if args[3]: SystemConfiguration.__start_option_4()
        if args[4]: GraphicDrivers.build()
        Daemons.enable_all_daemons()
        PatchSystemBugs.enable_all_patches()
    # @staticmethod
    # def __start_option_1():
    
    @staticmethod
    # TODO: Make a universal function for installing packages
    # TODO: Catch errors if the software is not detected
    def __install_pacman_package(package_names: list):
        for package in package_names:
            os.system(f"sudo pacman -S --noconfirm {package}")
            Logger.add_record(f"Installed: {package}", status=LoggerStatus.SUCCESS)

    @staticmethod
    # TODO: Make a universal function for installing packages
    # TODO: Catch errors if the software is not detected
    def __install_aur_package(package_names: list):
        for package in package_names:
            os.system(f"yay -S --noconfirm {package}")
            Logger.add_record(f"Installed: {package}", status=LoggerStatus.SUCCESS)
    
    @staticmethod
    def __create_default_folders__():
        Logger.add_record("[+] Create default directories", status=LoggerStatus.SUCCESS)
        default_folders = "~/Videos ~/Documents ~/Downloads " + \
                          "~/Music ~/Desktop"
        os.system("mkdir -p ~/.config")
        os.system("mkdir -p {default_folders}")
        os.system("cp -r Images/ ~/")
    
    @staticmethod
    def __copy_hyprland_dotfiles():
        Logger.add_record("[+] Copy Dotfiles & GTK", status=LoggerStatus.SUCCESS)
        os.system("cp -r config/* ~/.config/")
        os.system("cp Xresources ~/.Xresources")
        # os.system("cp gtkrc-2.0 ~/.gtkrc-2.0")
        os.system("cp -r local ~/.local")
        os.system("cp -r themes ~/.themes")
        os.system("cp xinitrc ~/.xinitrc")
        os.system("cp -r bin/ ~/")