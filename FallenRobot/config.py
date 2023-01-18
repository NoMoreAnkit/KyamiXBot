class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = "20047951"
    API_HASH = "28383d04008e2c078fb35f55f8783339"

    CASH_API_KEY = "1T4JPU6WMF1DG7EI"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://nljwycjt:7B43ya5gucYPy6Za6BElKm2bVtuB5ZAP@snuffleupagus.db.elephantsql.com/nljwycjt"  # A sql database url from elephantsql.com

    EVENT_LOGS = "-1001686049931"  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://<KyamiX:x@cluster0.5piuasa.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://te.legra.ph/file/d11f39494a3eb8a6cb49a.jpg"

    SUPPORT_CHAT = "DevilsHeavenMF"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "5844122667:AAEw_I6RykGhdX2yno9_qTLd-8pZdFyUMzs"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "EK8JNZ13XPB8"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 5672027235  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = "5672027235"  # User id of sudo users
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