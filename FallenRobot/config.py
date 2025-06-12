class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 21705136
    API_HASH = "78730e89d196e160b0f1992018c6cb19"

    CASH_API_KEY = "J809I8KT3LJBBTZE"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = ""  # A sql database url from elephantsql.com

    EVENT_LOGS = "-1002478484121" # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://Krishna:pss968048@cluster0.4rfuzro.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://graph.org/vTelegraphBot-06-12-21"

    SUPPORT_CHAT = "QayamatBots"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "6866712276:AAH1HWzM-xRPZjCjtt22FtCmfWqGl3V-WLM"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "KI547J12APOV"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 7418323193  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
