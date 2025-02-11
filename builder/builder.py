import os
import package 
from logger import Logger, LoggerStatus
from builder.software import AurBuilder, FirefoxCustomize
from builder.drivers import GraphicDrivers
from builder.patches import PatchSystemBugs
from builder.daemons import Daemons

class SystemConfiguration:
    def start(*args):
        start_text = f"[+] Starting assemly. Options {args}"
        Logger.add_record(start_text, status=LoggerStatus.SUCCESS)
        if args[0]: SystemConfiguration.__start_option_1()
        if args[1]: SystemConfiguration.__start_option_2()
        if args[2]: SystemConfiguration.__start_option_3()
        if args[3]: SystemConfiguration.__start_option_4()
        if args[4]: GraphicDrivers.build()
        Daemons.enable_all_daemons()
        # PatchSystemBugs.enable_all_patches()
    def __start_option_1():

    def __create_default_folders__():
        Logger.add_record("[+] Create default directories", status=LoggerStatus.SUCCESS)
        os.system("mkdir -p ~/.config")