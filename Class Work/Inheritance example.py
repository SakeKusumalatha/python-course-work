#INHERITANCE : REAL EXAMPLE

class Youtube:
    def playvideo(self):
        print("Video is running with....")
        print("Ads will run")
        print("No background play")
        print("Low quality available")
        print("Play back speed (upto 2x)")

    def youtubeMusic(self):
        print("No access to YouTube Music in free version")

    def likes(self):
        print("You can like videos")

    def share(self):
        print("You can share videos with others")

    def comments(self):
        print("You can comment on videos")

    def subscribe(self):
        print("You can subscribe to channels")

    def upload(self):
        print("You can upload your own videos")

    def watchhistory(self):
        print("You can view your watch history")

    def downloads(self):
        print("No access to Downloads in free version")


# Premium version using inheritance
class YoutubePremium(Youtube):
    def playvideo(self):
        print("Video is running with....")
        print("No ads 🎉")
        print("Background play available")
        print("High quality available (up to 4K/8K)")
        print("Play back speed (upto 2x)")

    def youtubeMusic(self):
        print("Access granted to YouTube Music 🎶")

    def downloads(self):
        print("Videos can be downloaded and watched offline")

ram=YoutubePremium()
print("\n ram -YoutubePremium")
ram.playvideo()
ram.youtubeMusic()
ram.downloads()
ram.likes()
ram.comments()
ram.subscribe()
ram.upload()
ram.watchhistory()

sita=Youtube()
print("\n sita -Youtube")
sita.playvideo()
sita.youtubeMusic()
sita.downloads()
sita.likes()
sita.comments()
sita.subscribe()
sita.upload()
sita.watchhistory()

'''#OUTPUT :
ram -YoutubePremium
Video is running with....
No ads 🎉
Background play available
High quality available (up to 4K/8K)
Play back speed (upto 2x)
Access granted to YouTube Music 🎶
Videos can be downloaded and watched offline
You can like videos
You can comment on videos
You can subscribe to channels
You can upload your own videos
You can view your watch history

 sita -Youtube
Video is running with....
Ads will run
No background play
Low quality available
Play back speed (upto 2x)
No access to YouTube Music in free version
No access to Downloads in free version
You can like videos
You can comment on videos
You can subscribe to channels
You can upload your own videos
You can view your watch history'''
