import pdb
import logging
import platform
import undetected_chromedriver as uc
from ladderbot.gui import show_gui
from ladderbot import controllers
import importlib.resources
#-----------------------------------------------
def bot():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filename=str(importlib.resources.files("ladderbot")) + "\\debug.log",
        filemode='w'
    )
    # Create logger
    logger = logging.getLogger()
    show_gui()
    # Set the options for the Chrome driver
    chrome_options = uc.ChromeOptions()
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    # Set the window position
    chrome_options.add_argument("--window-position=-5,695")
    chrome_options.add_experimental_option("prefs", prefs)
    # Check the system's operating system
    platform_name = platform.system()
    logger.info(f"Running on {platform_name}")
    driver = uc.Chrome(options=chrome_options)
    # Set the window size
    driver.set_window_size(900, 705)
    # Initialize all controllers before interacting with the driver or driver de-sync can occur
    login_controller = controllers.LoginController(driver, logger)
    player_controller = controllers.PlayerController(driver, logger)
    leveling_controller = controllers.LevelingController(driver, logger)
    inventory_controller = controllers.InventoryController(driver, logger)
    transmute_controller = controllers.TransmuteController(driver, logger)
    market = controllers.MarketController(driver, logger, gold_password='temp')
    vault = controllers.VaultController(driver, logger)
    # Create Login instance and boot the game
    login = controllers.Login(login_controller)
    login.run(character_name='kdasje5465131')
    # Create Player and Inventory instances to maintain game data
    inventory = controllers.Inventory(inventory_controller)
    player = controllers.Player(logger, player_controller, inventory)
    while True:
            # try:
                leveling_controller.run()
                player.update_health()
                player.update_transmute_rank()
                player.inventory.load()
                player.do_master_quest()
                pdb.set_trace()
                # transmute_controller.transmute_equipment(player.transmute_rank, player.inventory.equipment)
                # vault.deposit_equipment(player.inventory.equipment)
                # market.sell_equipment(player.inventory.equipment)
            # except:
            #     driver.close()
            #     return
#-----------------------------------------------