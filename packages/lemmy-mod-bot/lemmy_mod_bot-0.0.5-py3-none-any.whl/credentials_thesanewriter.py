# Rename this file to credentials.py and update the values below.
username = "Mod_bot"
password = '*Y9"qi$L.6rJzCU'
instance = "https://lemmy.thesanewriter.com"
communities = ["firefighting@lemmy.world", "nsw@lemmy.world", "hmres@lemmy.world", "asklemmy@lemmy.world", "bot_testing@lemm.ee"]
alt_username = 'Bluetreefrog@lemmy.world'
user_watch_list = ["https://fedia.io/u/AllahFucksKids", "https://kbin.social/u/AngrilyEatingMuffins", "https://lemmy.world/u/UmbrellAssassin", "https://sh.itjust.works/u/Captainvaqina"]
question_communities = ["asklemmy@lemmy.world"]
debug_mode = False  # Setting this value to true will mean that the bot will not actually submit reports.

# The bot basically works on a balance of probabilities approach when deciding whether to report
# content as toxic.  The following parameter increases the threshold of certainty that
# the bot requires before reporting content.  0 = balance of probabilities.  1.0 = never report.
uncertainty_allowance = 0.2

# Matrix login details for the bot to communicate with a Matrix room
"""    
    server : string - The name of the server.  e.g. "https://matrix.example.org"
    account : string - The name of the account e.g. "@alice:example.org"
    password : string - The password for the account e.g. "my-secret-password"
    room_id : string - The id of the room e.g. "!my-fave-room:example.org"
    content : string - The content of the message e.g. "Hello World!"
"""
matrix_server="https://matrix.org"
matrix_account="@bluetreefrog:matrix.org"
matrix_password="W1c(8aL?Gm_}"
matrix_room_id="!GuwQcFdSsZvfbQITgS:matrix.org"

