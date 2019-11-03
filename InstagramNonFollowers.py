from instapy import InstaPy
from getpass import getpass
from colored import fg, bg, attr

# Get account's username
print("Enter your Instagram username: ")
insta_username = input()

# Get account's password
print("Enter your Instagram password: ")
insta_password = getpass()

# Launch session and login
session = InstaPy(username=insta_username, password=insta_password, headless_browser=True)
session.login()

# Grab Non-Followers list
user_nonfollowers = session.pick_nonfollowers(username=insta_username, live_match=True, store_locally=True)

# Pick color for output 
color = bg('#C13584') + fg('white')
reset = attr('reset')

#Print Non-Followers list
print("Users you follow that don't follow you back: ")
print(color + str(user_nonfollowers) + reset)
session.end()
