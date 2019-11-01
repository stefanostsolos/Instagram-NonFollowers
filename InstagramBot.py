from instapy import InstaPy
from getpass import getpass
from colored import fg, bg, attr
print("Enter your Instagram username: ")
insta_username = input()
print("Enter your Instagram password: ")
insta_password = getpass()
session = InstaPy(username=insta_username, password=insta_password, headless_browser=True)
session.login()
user_nonfollowers = session.pick_nonfollowers(username=insta_username, live_match=True, store_locally=True)
color = bg('#C13584') + fg('white')
reset = attr('reset')
print("Users you follow that don't follow you back: ")
print(color + str(user_nonfollowers) + reset)
session.end()