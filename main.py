from bouderrie.helpers import HelperMethods
from bouderrie.bouderrie import Boudrerrie


boudrerrie = Boudrerrie()

discord_token = HelperMethods.get_token()

if discord_token:
    boudrerrie.run(discord_token)
else:
    print("No discord token found, exiting.")

