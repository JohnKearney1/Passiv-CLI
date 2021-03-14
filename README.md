# [Passiv X](https://github.com/JohnKearney1/Passiv-X)

___
## Abstract

Passiv-X is a python implementation of a grid-style trading framework for algorithm generation, analysis, and market making.
It supports trading on [Binance Perpetual Futures (USDs-T)](https://www.binance.com/en/futures)
and [Bybit Inverse Perpetual Futures](https://www.bybit.com/en-US/contract-rules).
Passiv-X is maintained by [@JohnKearney1](https://github.com/johnkearney1) with additional
ease of use features, and will expand to include monitoring tools for your
Passiv instances. Passiv-X also includes a refactor of the package structure
for easier setup, packaging, and distribution along with multi-version support.

**Version:** [*A.001  {Alpha 001}*](https://github.com/JohnKearney1/Passiv-X/wiki)   
**Note:** *Passiv X was borne from a fork of [passivbot_futures](https://github.com/enarjord/passivbot_futures) v2.1.3 by [@enarjord](https://github.com/enarjord).*  
**Warning:** *Use at your own risk. You alone are liable for your usage of this tool. There may be bugs.*  

**Wiki**: https://github.com/JohnKearney1/Passiv-X/wiki  
*The Wiki contains detailed setup and usage instructions, as well as a detailed overview, FAQ and more!*

#### Live Mode

Passiv-X's purpose is to accumulate Bitcoin (or another coin) on ByBit Inverse Futures and USDs-T Perpetual Futures. It is a market maker bot, creating multiple post-only limit orders above and below a given price, and uses an augmented martingale strategy to average into positions before closing at a specified profit percentage. It listens to a live websocket stream of trades using your API Keys, and updates its orders continuously based upon to the exchange's per-second rate limit. When there is no position, it enters either long or short depending on indicator settings if any are being used. This is done to scalp ambiguous price action and profit from indecision or market noise in between larger trades. Passiv-X may eventually contain multiple versions of itself, and some versions may utilize differing mechanics to trade. As such, they may require separate configuration, or additional setup. The manner in which the bot trades is defined largely by configuration files, containing key information on how Passiv should act in a given situation. These configurations can be downloaded from the [Configuration Repo](https://github.com/JohnKearney1/PassivBot-Configurations) or generated using the backtester.


If there is a long position, it creates re-entry bids below the position price, and reduce-only asks above position price using the following formula:

`reentry_bid_price = pos_price * (1 - grid_spacing * (1 + (position_margin / wallet_balance) * grid_coefficient))`


If there is a short position, Passiv-X creates re-entry asks above the position price, and reduce-only closing bids below position price using the inverse formula:  

`reentry_ask_price = pos_price * (1 + grid_spacing * (1 + (position_margin / wallet_balance) * grid_coefficient))`

#### Backtester

Passiv-X's backtester allows users to generate new configurations for the bot and save relevant test data. These backtested configurations can then be analyzed using [Jupyter-Lab](https://jupyter.org/) and the included `.ipynb` files. The backtester takes a variety of parameters from the user to help specify risk level, volatility tolerance, loss tolerance, average daily gain and more. The backtester will iterate through random settings, building a list of 'candidates' that fit your criteria. Jackrabbit, the engine for improving configurations, will slowly decrease the ranges for the best candidates until better ones are found that still fit your parameters. These iterations repeat up to a specified amount, and a `best_settings.json` configuration file is returned at the end. If no profitable configurations are found that meet your criteria, nothing is returned. In this case, you can re-test, or adjust your `backtesting_settings.hjson` to be more lenient. Note that your `backtesting_configs/backtesting_settings` is an hjson, while your `live_settings/{exchange}/live_settings.json` is a standard json file. This is done to accelerate the speed of backtesting, where **numpy** is used to speed up mathematical calculations.

Jackrabbit ("JR") is a pet name given to the simple algorithm for optimizing the bot's settings. JR iterates many backtests in succession, for each iteration, settings are mutated to new values within given a range defined in your backtesting_settings configuration file.If the new candidate's backtest yields a higher gain than best candidate's backtest, the superior settings becomes the parent of the next candidate.
The mutation coefficient `m` determines the mutation range, and is inversely proportional to `k`, which is a simple counter for JR iterations. At first, new candidates will vary wildly from the best settings, while large ranges are 'scanned' for good results. Towards the end of the backtest (as `k` approaches `n_jackrabbit_iterations`) they begin will vary less, essentially "fine tuning" the parameters.

#### Backtesting Data Analysis

[Jupyter-Lab](https://jupyter.org/) is used to analyze the results of a given backtest in detail. After completion, open `backtest_notes.ipynb` inside of Jupyter, using *`Passiv-X/Passiv-25/`* as your current working directory. In cell **[5]** edit the variable `backtest_config_name = 'YOURCONFIGHERE'` to match your backtest configuration file. After saving, return focus to cell **[1]** and step through the cells using *`Shift + Enter`*. Jupiter will display and save all generated data as PNG files in the directory of your backtest for later reference, and print the exact results of your test. As with any portion of this code, the backtest_notes can be modified to provide additional data for the user.
___  

## Usage  

#### Environment  

Requirements:
- Python >=3.8.x
- Pip


Install the dependencies by using `pip install -r requirements.txt` from the root folder of Passiv-X.


#### Setup Exchange Connection

On the exchange of your choice, create and save a new API keypair.
You can name the API anything you like, although it is suggested to use a new account.
While the bot is running, executing manual trades may throw off the bot and cause losses or liquidation.
Add your API keys using the CLI menu:

In the directory `Passiv-X`, run the command: `python3 main.py`


        ...

        ____________________________________________________

        __________                      __       ____  __
        \______   \____    ______ ________|__  __\   \/ /
          |     ___/__  \  /  ___//  ___/  |  \/ / \    /
          |    |    / __ \_\___ \ \___ \|  |\   /  /    \
          |____|   (____  /____  \____  \__| \_/  /___/\ \
                        \/     \/     \/                \/


          ____________________________________________________

                          | Main Menu |

          [1] PassivBot Live - Binance Perpetual Futures
          [2] PassivBot Live - ByBit Inverse Perpetual Futures
          [3] Backtest
          [4] Settings
          [5] Help
          [6] Exit



          > 4

select `[4] Settings` using: `4`

          ...

          What settings would you like to adjust?
          __________________________________________________

          [1] API Keys (Users)
          [2] Live Configurations
          [3] Backtesting Configurations
          [4] <- Back


          > 1

Select `[1] API Keys (Users)` using: `1`

          ...

          [1] Add API Key
          [2] View Keys

          >

Select `[1] Add API Key` using: `1`

You will be prompted to upload or add a new API Keyfile. The default format for the API Keyfile is a `.json` file where the filename is the User's name or configuration name. If you don't know your configuration name yet, assign an arbitrary name you can copy later. No spaces are allowed.

**Format**: `["KEY", "SECRET"]`

More information is available on the [Wiki](https://github.com/JohnKearney1/Passiv-X/wiki).

#### Selecting a Configuration  

When selecting a configuration, you may either use the included backtester to generate a new config, or you can use a pre-made configuration from the 'v2.0.0' directory of the [Configuration Repo](https://github.com/JohnKearney1/PassivBot-Configurations). These configurations may be untested, unstable, unprofitable, outdated, or the inverse. They are provided with test data to provide a set of comparable data to ensure you are correctly generating configurations. If you find a configuration you'd like to share, it can be submitted for addition to the repository.

Information on usage of the backtester is detailed on the [Wiki](https://github.com/JohnKearney1/Passiv-X/wiki). As the process is relatively complex, it's recommended to run backtests from a local environment, and not on a cloud instance, VPC, VPS or otherwise.

When uploading or adding a configuration, you should name it after your API KeyFile. If you have multiple configs for one account, add multiple API KeyFiles with differing names but identical content to match the config list. For example, if you have a configuration named 'MY_BTCUSD_CONFIG', your API Key folder (`Passiv-25/api_key_secrets/{exchange}/`) should also include an API KeyFile with the name 'MY_BTCUSD_CONFIG'.


#### Running Passiv-X

You can launch Passiv-X in live mode using the CLI menu. Simply run `python3 main.py` from the root directory (Passiv-X/).  

If you wish to bypass the CLI menu, you may run the bot from the package directory (Passiv-X/Passiv-25/) using `python3 start_bot.py {exchange} {config_name}`.

To run the backtester, configure your `backtesting_settings.hjson` as defined in the wiki, then run the `python3 backtest.py {backtesting_settings_filename}`. Optionally, append `--jit` to utilize code acceleration. Note, it is not necessary to add the file extension (.hson) to the backtesting_settings_filename in executing the command.


#### Offload Live Bot to VPS/VPC

Running Passiv-X from a VPS instance is easy! When reference to the "live" bot is made, it simply refers to an instance of the bot that been cloned, and filled with the necessary configurations and API keys to run "live" on your account, using real money, without additional configuration. When reference to the "test" bot is made, it refers to a local instance used primarily for generating and analyzing new configurations. There is no difference between the code of these instances, just the configurations and KeyFiles.

Offloading your live bot to a cloud provider such as [Digital Ocean](https://www.digitalocean.com/) or [Amazon Web Services](https://aws.amazon.com/) is easy. Simply upload a zipped copy of your pre-configured instance of Passiv-X to your instance, set the region based upon the latency from the exchange's servers, unzip, and run.

More information is available on the [Wiki](https://github.com/JohnKearney1/Passiv-X/wiki).

____

### Reference "Live" Configuration: ByBit Inverse

    {

    "balance_pct": 0.5,                   # if settings["balance_pct"] = 1.0, will use 100% of balance.
                                          # if settings["balance_pct"] = 0.35, will us 35% of balance.
    "config_name": "BTCUSD_default",      # arbitrary name given to settings.
    "cross_mode": true,                   # true for cross, false for isolated.
                                          # use isolated mode with care.  depending on settings, there is high risk of accidental liquidations.

    "entry_qty_pct": 0.005,               # percentage of balance * leverage used as initial entry qty.
                                          # the bot will calculate initial entry qty using the following formula:
                                          # initial_entry_qty = round_dn(balance_in_terms_of_contracts * leverage * abs(settings["entry_qty_pct"]), qty_step)
                                          # bybit BTCUSD example:
                                          # if "entry_qty_pct"  is set to 0.0021, last price is 37000, leverage is 50 and wallet balance is 0.001 btc,
                                          # initial_entry_qty = 0.001 * 37000 * 50 * 0.0021 == 3.885.  rounded down is 3.0 usd.
                                          # binance ETHUSDT example:
                                          # if "entry_qty_pct" is set to 0.07, last price is 1100, leverage is 33 and wallet balance is 40 usdt,
                                          # initial_entry_qty = (40 / 1100) * 33 * 0.07 == 0.084.  rounded down is 0.084 eth.

    "ddown_factor": 0.02,                 # next reentry_qty is max(initial_entry_qty, abs(pos_size) * ddown_factor).
                                          # if set to 1.0, each reentry qty will be equal to 1x pos size, i.e. doubling pos size after every reentry.
                                          # if set to 1.5, each reentry qty will be equal to 1.5x pos size.
                                          # if set to 0.0, each reentry qty will be equal to initial_entry_qty.

    "indicator_settings": {
        "tick_ema": {                     # tick ema is not based on ohlcvs, but calculated based on sequence of raw trades.
            "span": 10000,                # if no pos, bid = min(ema * (1 - spread), highest_bid) and ask = max(ema * (1 + spread), lowest_ask)
            "spread": 0.001
        },                                # if ema span is set to 1.0, ema is always equal to last price, which will disable ema smoothing of initial entries

        "funding_fee_collect_mode": false,# if true, will enter long only if predicted funding fee is < 0.0, and short only if predicted funding fee is > 0.0

        "do_long": true,                  # if true, will allow long positions
        "do_shrt": true                   # if true, will allow short posisions
    },

    "grid_coefficient": 245.0,            # next entry price is pos_price * (1 +- grid_spacing * (1 + (pos_margin / balance) * grid_coefficient)).
    "grid_spacing": 0.0026,               #

    "stop_loss_liq_diff": 0.02,           # if difference between liquidation price and last price is less than 2%, ...
    "stop_loss_pos_price_diff": 0.04,     # ... or if difference between pos price and last price is greater than 4%, reduce position by 2% at a loss,

    "stop_loss_pos_reduction": 0.02,      # reduce position by 2% at a loss.

    "leverage": 100,                      # leverage (irrelevant in bybit because cross mode in is always max leverage).
    "logging_level": 0,                   # if logging_level > 0,
                                          # will log positions, open orders, order creations and order cancellations in logs/{exchange}/{config_name}.log.

    "min_markup": 0.0002,                 # when there's a position, bot makes a grid of n_close_orders whose prices are
    "max_markup": 0.0159,                 # evenly distributed between min and max markup, and whose qtys are pos_size // n_close_orders.
    "min_close_qty_multiplier": 0.5       # min_close_qty = max(min_qty, initial_entry_qty * min_close_qty_multiplier)

    "market_stop_loss": false,            # if true will soft stop with market orders, if false soft stops with limit orders at order book's higest_bid/lowest_ask

    "n_close_orders": 20,                 # max n close orders.
    "n_entry_orders": 8,                  # max n entry orders.
    "symbol": "BTCUSD"                    # only one symbol at a time.

    }
