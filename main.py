import json
import os
import sys
from subprocess import Popen
from time import sleep


def helpmenu():
    with open("setupInfo/help.txt", "r") as fh:
        menu = fh.read()

    print(menu)
    input("\nPress a key to go back...")
    start()
    sys.exit()


# Menu for working with live configs
def live_config_menu():
    # Print the menu and wait for a choice
    selection = input("\n\n____________________________________\n\n"
                      "[1] List Configurations\n"
                      "[2] Add Configuration Manually\n"
                      "[3] Upload Existing Configuration\n\n> ")

    # List Configurations from both directories
    if selection == "1":

        # Set the paths
        path_live_config_binance = "Passiv-25/live_settings/binance"
        path_live_config_bybit = "Passiv-25/live_settings/bybit"

        # List Configs Binance
        i = 0
        print("\n_____________________________")
        while i < len(os.listdir(path_live_config_binance)):
            print("\nBinance Configuration " + str(i + 1) + " .... " + os.listdir(path_live_config_binance)[i][:-5])
            i = i + 1
        # List Configs Bybit
        i = 0
        while i < len(os.listdir(path_live_config_bybit)):
            print("\nBybit Configuration " + str(i + 1) + " .... " + os.listdir(path_live_config_bybit)[i][:-5])
            i = i + 1
        # Wait for input then break
        input("\n > Press Any Key To Continue...\n")

    # Add Live Configuration Manually
    elif selection == "2":

        # Select exchange to add configuration for
        sel_ex = input("\n\n____________________________________\n\n"
                       "[1] Binance Live Configuration\n"
                       "[2] ByBit Live Configuration\n"
                       "[3] <-- Back\n\n> ")

        # Create Binance Live Configuration
        if sel_ex == "1":

            # Gather input for configuration name
            configName = str(input("\n...\n\nEnter a configuration name (this can be anything you like):\n\n> "))

            # Print warning
            print("\nBE CAREFUL Editing these values. If you do not know what they are, consult the wiki:\n"
                  "https://github.com/enarjord/passivbot_futures/wiki/Live-Bot-Configuration\n")

            tradingSymbol = str(input("\n__________________________________\n"
                                      "Enter 'symbol':\n> "))

            logLevel = int(input("\n__________________________________\n"
                                 "Enter 'logging_level' (Enter '0' for default):\n\n> "))

            crossMode = bool(input("\n__________________________________\n"
                                   "Enter 'cross_mode':\n\n> "))

            balPct = float(input("\n__________________________________\n"
                                 "Enter 'balance_pct':\n\n> "))

            ddownFactor = float(input("\n__________________________________\n"
                                      "Enter 'ddown_factor':"))

            entryQtyPct = float(input("\n__________________________________\n"
                                      "Enter 'entry_qty_pct':\n\n> "))

            minCloseQtyMultiplier = float(input("\n__________________________________\n"
                                                "Enter 'min_close_qty_multiplier':\n\n> "))
            leverage = int(input("\n__________________________________\n"
                                 "Enter 'leverage':\n\n> "))

            nEntryOrders = int(input("\n__________________________________\n"
                                     "Enter 'n_entry_orders':\n\n> "))

            nCloseOrders = int(input("\n__________________________________\n"
                                     "Enter 'n_close_orders':\n\n> "))

            gridSpacing = float(input("\n__________________________________\n"
                                      "Enter 'grid_spacing':\n\n> "))

            gridCoeff = float(input("\n__________________________________\n"
                                    "Enter 'grid_coefficient':\n\n> "))

            minMarkup = float(input("\n__________________________________\n"
                                    "Enter 'min_markup':\n\n> "))

            maxMarkup = float(input("\n__________________________________\n"
                                    "Enter 'max_markup':\n\n> "))

            doLong = bool(input("\n__________________________________\n"
                                "Enter 'do_long':\n\n> "))

            doShrt = bool(input("\n__________________________________\n"
                                "Enter 'do_shrt':\n\n> "))

            fundingFeeCollectMode = bool(input("\n__________________________________\n"
                                               "Enter 'funding_fee_collect_mode':\n\n> "))

            emaSpan = float(input("\n__________________________________\n"
                                  "Enter 'span' for 'tick_ema':\n\n> "))

            emaSpread = float(input("\n__________________________________\n"
                                    "Enter 'spread' for 'tick_ema':\n\n> "))

            marketStopLoss = bool(input("\n__________________________________\n"
                                        "Enter 'market_stop_loss':\n\n> "))

            stopLossLiqDiff = float(input("\n__________________________________\n"
                                          "Enter 'stop_loss_liq_diff':\n\n> "))

            stopLossPosPriceDiff = float(input("\n__________________________________\n"
                                               "Enter 'stop_loss_pos_price_diff':\n\n> "))

            stopLossPosRed = float(input("\n__________________________________\n"
                                         "Enter 'stop_loss_pos_price_reduction':\n\n> "))

            # Define Configuration File Format
            api_config_format_binance = {
                "config_name": configName,
                "symbol": tradingSymbol,
                "logging_level": logLevel,
                "cross_mode": crossMode,

                "balance_pct": balPct,
                "ddown_factor": ddownFactor,
                "entry_qty_pct": entryQtyPct,
                "min_close_qty_multiplier": minCloseQtyMultiplier,
                "leverage": leverage,
                "n_entry_orders": nEntryOrders,
                "n_close_orders": nCloseOrders,

                "grid_spacing": gridSpacing,
                "grid_coefficient": gridCoeff,
                "min_markup": minMarkup,
                "max_markup": maxMarkup,

                "indicator_settings": {
                    "do_long": doLong,
                    "do_shrt": doShrt,
                    "funding_fee_collect_mode": fundingFeeCollectMode,
                    "tick_ema": {
                        "span": emaSpan,
                        "spread": emaSpread
                    }
                },

                "market_stop_loss": marketStopLoss,
                "stop_loss_liq_diff": stopLossLiqDiff,
                "stop_loss_pos_price_diff": stopLossPosPriceDiff,
                "stop_loss_pos_reduction": stopLossPosRed
            }

            print(api_config_format_binance)

            # Dump keys to file
            with open("Passiv-25/live_settings/binance/" + configName + ".json", "w") as write_file:
                json.dump(api_config_format_binance, write_file)

            print("\n...\n\nBinance Configuration Generated Successfully!\n")

            input("Waiting...")

        elif sel_ex == "2":

            # Gather input for configuration name
            configName = str(input("\n...\n\nEnter a configuration name (this can be anything you like):\n\n> "))

            # Print warning
            print("\nBE CAREFUL Editing these values. If you do not know what they are, consult the wiki:\n"
                  "https://github.com/enarjord/passivbot_futures/wiki/Live-Bot-Configuration\n")

            tradingSymbol = str(input("\n__________________________________\n"
                                      "Enter 'symbol':\n> "))

            logLevel = int(input("\n__________________________________\n"
                                 "Enter 'logging_level' (Enter '0' for default):\n\n> "))

            crossMode = bool(input("\n__________________________________\n"
                                   "Enter 'cross_mode':\n\n> "))

            balPct = float(input("\n__________________________________\n"
                                 "Enter 'balance_pct':\n\n> "))

            ddownFactor = float(input("\n__________________________________\n"
                                      "Enter 'ddown_factor':"))

            entryQtyPct = float(input("\n__________________________________\n"
                                      "Enter 'entry_qty_pct':\n\n> "))

            minCloseQtyMultiplier = float(input("\n__________________________________\n"
                                                "Enter 'min_close_qty_multiplier':\n\n> "))
            leverage = int(input("\n__________________________________\n"
                                 "Enter 'leverage':\n\n> "))

            nEntryOrders = int(input("\n__________________________________\n"
                                     "Enter 'n_entry_orders':\n\n> "))

            nCloseOrders = int(input("\n__________________________________\n"
                                     "Enter 'n_close_orders':\n\n> "))

            gridSpacing = float(input("\n__________________________________\n"
                                      "Enter 'grid_spacing':\n\n> "))

            gridCoeff = float(input("\n__________________________________\n"
                                    "Enter 'grid_coefficient':\n\n> "))

            minMarkup = float(input("\n__________________________________\n"
                                    "Enter 'min_markup':\n\n> "))

            maxMarkup = float(input("\n__________________________________\n"
                                    "Enter 'max_markup':\n\n> "))

            doLong = bool(input("\n__________________________________\n"
                                "Enter 'do_long':\n\n> "))

            doShrt = bool(input("\n__________________________________\n"
                                "Enter 'do_shrt':\n\n> "))

            fundingFeeCollectMode = bool(input("\n__________________________________\n"
                                               "Enter 'funding_fee_collect_mode':\n\n> "))

            nPeriods = float(input("\n__________________________________\n"
                                   "Enter 'n_periods' for 'ohlcv_rsi':\n\n> "))

            periodMs = float(input("\n__________________________________\n"
                                   "Enter 'period_ms' for 'ohlcv_rsi':\n\n> "))

            emaSpan = float(input("\n__________________________________\n"
                                  "Enter 'span' for 'tick_ema':\n\n> "))

            emaSpread = float(input("\n__________________________________\n"
                                    "Enter 'spread' for 'tick_ema':\n\n> "))

            marketStopLoss = bool(input("\n__________________________________\n"
                                        "Enter 'market_stop_loss':\n\n> "))

            stopLossLiqDiff = float(input("\n__________________________________\n"
                                          "Enter 'stop_loss_liq_diff':\n\n> "))

            stopLossPosPriceDiff = float(input("\n__________________________________\n"
                                               "Enter 'stop_loss_pos_price_diff':\n\n> "))

            stopLossPosRed = float(input("\n__________________________________\n"
                                         "Enter 'stop_loss_pos_price_reduction':\n\n> "))

            # Define Configuration File Format
            api_config_format_bybit = {
                "config_name": configName,
                "symbol": tradingSymbol,
                "logging_level": logLevel,
                "cross_mode": crossMode,

                "balance_pct": balPct,
                "ddown_factor": ddownFactor,
                "entry_qty_pct": entryQtyPct,
                "min_close_qty_multiplier": minCloseQtyMultiplier,
                "leverage": leverage,
                "n_entry_orders": nEntryOrders,
                "n_close_orders": nCloseOrders,

                "grid_spacing": gridSpacing,
                "grid_coefficient": gridCoeff,
                "min_markup": minMarkup,
                "max_markup": maxMarkup,

                "indicator_settings": {
                    "do_long": doLong,
                    "do_shrt": doShrt,
                    "funding_fee_collect_mode": fundingFeeCollectMode,
                    "ohlcv_rsi": {
                        "n_periods": nPeriods,
                        "period_ms": periodMs
                    },
                    "tick_ema": {
                        "span": emaSpan,
                        "spread": emaSpread
                    }
                },

                "market_stop_loss": marketStopLoss,
                "stop_loss_liq_diff": stopLossLiqDiff,
                "stop_loss_pos_price_diff": stopLossPosPriceDiff,
                "stop_loss_pos_reduction": stopLossPosRed,
            }

            print(api_config_format_bybit)

            # Dump keys to file
            with open("Passiv-25/live_settings/bybit/" + configName + ".json", "w") as write_file:
                json.dump(api_config_format_bybit, write_file)

            print("\n...\n\nBybit Configuration Generated Successfully!\n")

            input("Waiting...")
        elif sel_ex == "3":
            start()
            sys.exit()

    elif selection == "3":
        CURR_DIR_binance = os.path.dirname(os.path.realpath(__file__)) + "/Passiv-25/live_settings/binance"
        CURR_DIR_bybit = os.path.dirname(os.path.realpath(__file__)) + "/Passiv-25/live_settings/bybit"
        print("\n____________________________________\n\n"
              "Upload your configuration as a .hjson file (with any name) to the corresponding directory, "
              "then restart:\n\n "
              + CURR_DIR_binance + " <-- For BINANCE Keys!\n"
              + CURR_DIR_bybit + " <-- For BYBIT Keys!\n\n"
                                 "If you use FTP, SCP or something similar; this is the "
                                 "folder to target on the machine.\n")
        input("> Press Any Key To Continue...")


# Menu for working with backtesting configs
def test_config_menu():
    backtest_dir = os.path.dirname(os.path.realpath(__file__)) + "/Passiv-25/backtest_configs/"
    print("\n____________________________________\n\n"
          "To adjust your backtesting settings, open the default hjson file located at:\n" +
          backtest_dir + "\n\nThe CLI currently does not include a backtesting configuration editor.")


# Menu for working with API keys
def api_menu():
    path_API_keys = "Passiv-25/live_settings/binance"

    selection = input("\n...\n\n"
                      "[1] Add API Key\n"
                      "[2] View Keys\n\n> ")
    if selection == "1":
        sel_2 = input("\n...\n\n"
                      "[1] Add Key Manually (Recommended)\n"
                      "[2] Upload Existing Keyfile\n\n> ")
        if sel_2 == "1":
            sel_3 = input("\n...\n\n"
                          "[1] Add Binance API Key\n"
                          "[2] Add Bybit API Key\n\n> ")
            if sel_3 == "1":
                add_api_binance()
            elif sel_3 == "2":
                add_api_bybit()
            else:
                start()
        elif sel_2 == "2":
            CURR_DIR_binance = os.path.dirname(
                os.path.realpath(__file__)) + "/Passiv-25/api_key_secrets/binance"
            CURR_DIR_bybit = os.path.dirname(os.path.realpath(__file__)) + "/exchanges/Settings/api_key_secrets/bybit"
            print("\n____________________________________\n\n"
                  "Upload your KeyFile as a .json file (with any name) to the corresponding directory, "
                  "then restart:\n\n "
                  + CURR_DIR_binance + " <-- For BINANCE Keys!\n"
                  + CURR_DIR_bybit + " <-- For BYBIT Keys!\n\n"
                                     "If you use FTP, SCP or something similar; this is the "
                                     "folder to target on the machine.\n")
            input(" > Press Any Key To Continue...")
            sys.exit()
    elif selection == "2":
        # List Users
        i = 0
        print("\n_____________________________")
        while i < len(os.listdir(path_API_keys)):
            print("\nUser " + str(i + 1) + " .... " + os.listdir(path_API_keys)[i][:-5])
            i = i + 1
        input("\n > Press Any Key To Continue...")
        start()
    else:
        print("Invalid Selection. Exiting.")
        sys.exit()


# Adding an API Keyfile
def add_api_binance():
    # Define API keyfile format
    api_keyfile_format = ["EXAMPLE_KEY", "EXAMPLE_SECRET"]

    # Gather input for username
    username = input("\n...\n\nEnter a KeyFile name (This should be the same name as your configuration):\n\n> ")

    # Create a new json file with the username as the filename
    with open("Passiv-25/api_key_secrets/binance/" + username + ".json", "w") as write_file:
        json.dump(api_keyfile_format, write_file)

    # Load generated file
    keyfile = json.load(open(f'Passiv-25/api_key_secrets/binance/{username}.json'))

    # Gather input for key and secret key
    keyfile[0] = input("\n...\n\nEnter your API Key for Binance.com:\n\n> ")
    keyfile[1] = input("\n...\n\nEnter your Secret Key for Binance.com:\n\n> ")

    # Confirm the input
    print("\n...\n\nAre the following keys correct?\n")
    print("API - " + keyfile[0])
    print("SK - " + keyfile[1])

    # Dump keys to file
    with open("Passiv-25/api_key_secrets/binance/" + username + ".json", "w") as write_file:
        json.dump(keyfile, write_file)
    print("\n...\n\nAPI KeyFile Generated Successfully! Make sure to update your API access to 'allow' futures.\n")


def add_api_bybit():
    # Define API keyfile format
    api_keyfile_format = ["EXAMPLE_KEY", "EXAMPLE_SECRET"]

    # Gather input for username
    username = input("\n...\n\nEnter a username (This should be the same name as your configuration):\n\n> ")

    # Create a new json file with the username as the filename
    with open("Passiv-25/api_key_secrets/bybit/" + username + ".json", "w") as write_file:
        json.dump(api_keyfile_format, write_file)

    # Load generated file
    keyfile = json.load(open(f'Passiv-25/api_key_secrets/bybit/{username}.json'))

    # Gather input for key and secret key
    keyfile[0] = input("\n...\n\nEnter your API Key for Bybit.com:\n\n> ")
    keyfile[1] = input("\n...\n\nEnter your Secret Key for Bybit.com:\n\n> ")

    # Confirm the input
    print("\n...\n\nAre the following keys correct?\n")
    print("API - " + keyfile[0])
    print("SK - " + keyfile[1])

    # Dump keys to file
    with open("Passiv-25/api_key_secrets/bybit/" + username + ".json", "w") as write_file:
        json.dump(keyfile, write_file)
    print("\n...\n\nAPI KeyFile Generated Successfully! Make sure to update your API access to 'allow' futures.\n")


def launch_bybit():
    # Find how many files are in the API keys folder (save the example_user.json)
    path = "Passiv-25/api_key_secrets/bybit"
    path_configs = "Passiv-25/live_settings/bybit"
    files = next(os.walk(path))[2]
    userCount = str(len(files) - 1)

    # Determine if there is an existing user or not, then prompt the user to setup an account.
    # Alternatively, loop if the user doesn't want to add one right now.
    if userCount < "1":

        api_go = 'y'
        api_goC = 'Y'
        api_no = 'n'
        api_noC = 'N'
        api_sel = input("\n...\n\nThere are no API keys configured. Would you like to add an API Key? (y/n)\n\n> ")

        # Call the function to add an API KeyFile
        if api_go == api_sel:
            add_api_bybit()
            start()
        elif api_goC == api_sel:
            add_api_bybit()
            start()
        elif api_no == api_sel:
            start()
        elif api_noC == api_sel:
            start()
        else:
            start()

    # If there are existing users, list them and allow the user to select one.
    elif userCount >= "1":

        # List Users
        i = 0
        print("\n_____________________________\n")
        while i < len(os.listdir(path_configs)):
            print("\nConfiguration " + str(i + 1) + " .... " + os.listdir(path_configs)[i][:-5])
            i = i + 1

        # Gather input for configuration selection
        config_selection = input("\n_____________________________\n"
                                 "Type the name of the configuration you'd like to use.\n"
                                 "Ex: 'default'.\n"
                                 "Don't have one? Use the setup to generate or upload a config!\n\n> ")

        # Launch the bot with the selected parameters
        max_n_restarts = 30

        restart_k = 0

        while True:
            try:
                print(f"\nInitializing on Bybit using: {config_selection}")
                p = Popen(f"python3 bybit.py {config_selection}", shell=True, cwd='Passiv-25/')
                p.wait()
                restart_k += 1
                if restart_k > max_n_restarts:
                    print('30 Attempts to restart have been made... Aborting.')
                    break
                for k in range(30 - 1, -1, -1):
                    print(f"\rBot stopped, attempting to restart in {k} seconds", end='   ')
                    sleep(1)
            except KeyboardInterrupt:
                break


# Starting an instance of PassivBot running on Binance
def launch_binance():
    # Find how many files are in the API keys folder (save the example_user.json)
    path = "Passiv-25/api_key_secrets/binance"
    path_configs = "Passiv-25/live_settings/binance"
    files = next(os.walk(path))[2]
    userCount = str(len(files) - 1)

    # Determine if there is an existing user or not, then prompt the user to setup an account.
    # Alternatively, loop if the user doesn't want to add one right now.
    if userCount < "1":

        api_go = 'y'
        api_goC = 'Y'
        api_no = 'n'
        api_noC = 'N'
        api_sel = input("\n...\n\nThere are no API keys configured. Would you like to add an API Key? (y/n)\n\n> ")

        # Call the function to add an API KeyFile
        if api_go == api_sel:
            add_api_binance()
            start()
        elif api_goC == api_sel:
            add_api_binance()
            start()
        elif api_no == api_sel:
            start()
        elif api_noC == api_sel:
            start()
        else:
            start()

    # If there are existing users, list them and allow the user to select one.
    elif userCount >= "1":

        # List Users
        i = 0
        print("\n_____________________________\n")
        while i < len(os.listdir(path_configs)):
            print("\nConfiguration " + str(i + 1) + " .... " + os.listdir(path_configs)[i][:-5])
            i = i + 1

        # Gather input for configuration selection
        config_selection = input("\n_____________________________\n"
                                 "Type the name of the configuration you'd like to use.\n"
                                 "Ex: 'default'.\n"
                                 "Don't have one? Use the setup to generate or upload a config!\n\n> ")

        # Launch the bot with the selected parameters
        max_n_restarts = 30

        restart_k = 0

        while True:
            try:
                print(f"\nInitializing on Binance using: {config_selection}")
                p = Popen(f"python3 binance.py {config_selection}", shell=True, cwd='Passiv-25/')
                p.wait()
                restart_k += 1
                if restart_k > max_n_restarts:
                    print('30 Attempts to restart have been made... Aborting.')
                    break
                for k in range(30 - 1, -1, -1):
                    print(f"\rBot stopped, attempting to restart in {k} seconds", end='   ')
                    sleep(1)
            except KeyboardInterrupt:
                break


def settings():
    selection = input("\n\n...\n\nWhat settings would you like to adjust?\n"
                      "__________________________________________________\n\n"
                      "[1] API Keys (Users)\n"
                      "[2] Live Configurations\n"
                      "[3] Backtesting Configurations\n"
                      "[4] <- Back\n> ")
    if selection == "1":
        # API key logic
        api_menu()
    elif selection == "2":
        # Live Config Logic
        live_config_menu()
    elif selection == "3":
        # Backtest config logic
        print("hi")
    elif selection == "4":
        sys.exit()


def start():
    # Read in the menu from menu.txt
    with open("setupInfo/menu.txt", "r") as fh:
        menu = fh.read()

    menu_bool = True
    while menu_bool:

        # Print the menu, and wait for an input from the user to capture
        selection = input("Initialized" + menu + "\n\n> ")
        # Binance Live Bot
        if selection == "1":
            menu_bool = False
            launch_binance()
        # ByBit Live Bot
        elif selection == "2":
            menu_bool = False
            launch_bybit()
            sys.exit()
        # Backtest
        elif selection == "3":
            menu_bool = False
            test_config_menu()
        # Settings
        elif selection == "4":
            settings()
            start()
            menu_bool = False
        # Help
        elif selection == "5":
            menu_bool = False
            helpmenu()
        # Exit
        elif selection == "6":
            menu_bool = False
            print("Exiting")
            sys.exit()
        # Otherwise...
        else:
            print("Invalid Selection: " + str(selection))
            start()


if __name__ == "__main__":
    start()
