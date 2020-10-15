from tg_bot.sample_config import Config


class Development(Config):
    OWNER_ID = 881769564  # my telegram ID
    OWNER_USERNAME = "Gym2105"  # my telegram username
    API_KEY = "1399883818:AAENb3BqnCTpOavg_FkKZrE3ydT3Zk7g5vw"  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgresgym:21052001@localhost:5432/database-1'  # sample db credentials
    MESSAGE_DUMP = '1001221946970' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    SUDO_USERS = [1261080659]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']
