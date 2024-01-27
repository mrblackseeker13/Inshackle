
```python
import time
import instaloader

# Set the sleep time between follow and unfollow actions
sleep_time = 10

def follow_user(username):
    try:
        L = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(L.context, username)
        profile.follow()
        print(f"Followed {username} successfully")
    except Exception as e:
        print(f"Error occurred while following {username}: {str(e)}")

def unfollow_user(username):
    try:
        L = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(L.context, username)
        profile.unfollow()
        print(f"Unfollowed {username} successfully")
    except Exception as e:
        print(f"Error occurred while unfollowing {username}: {str(e)}")

# List of celebrity IDs 
celeb_ids = ["celeb_id1", "celeb_id2", "celeb_id3"]

# Follow each celebrity
for celeb_id in celeb_ids:
    follow_user(celeb_id)
    time.sleep(sleep_time)

# Unfollow each celebrity
for celeb_id in celeb_ids:
    unfollow_user(celeb_id)
    time.sleep(sleep_time)
```
