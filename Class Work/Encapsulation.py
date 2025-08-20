#ENCAPSULATION: Encapsulation means Ristrictions 

class Profile:
    def __init__(self,username,password):
        self._followers=set() #_ single underscore means protective
        self._following=set()
        self.posts=[]
        self.username=username
        self.__password=password #__ double underscore means private
        self.bio=''
        print(f'\n{self.username}, Your account is created. Have fun with Instagram')



    def getPassword(self):    # To get a Password
        return self.__password

    def setPassword(self,new_password):   # To set a password
        self.__password=new_password
        

    @property
    def NRfollowers(self):     # To get Followers
        return self._followers

    @NRfollowers.setter        # To set Followers
    def NRfollowers(self,req_uname):
        self._followers.add(req_uname)
        

    @property                      # To get Following
    def NRfollowing(self):
        return self._following

    @NRfollowing.setter             # To set Following
    def NRfollowing(self,rai_uname):
        self._following.add(rai_uname)
        


kusuma= Profile('kusuma','kus123')

print('kusuma Details'.center(40,'-'))

print('\nBefore Changing')
print(f'Before Username: {kusuma.username}')
print(f'Before Password: {kusuma.getPassword}')
print(f'Before Bio: {kusuma.bio}')
print(f'Before Posts: {kusuma.posts}')
print(f'Before Followers: {kusuma.NRfollowers}')
print(f'Before Following: {kusuma.NRfollowing}')


print('\nAfter Changing')
kusuma.username='skusumalatha'
print(f'After Username: {kusuma.username}')

kusuma.setPassword('kusuma@123')
print(f'After Password: {kusuma.getPassword()}')


kusuma.bio='Blogger'
print(f'After Bio: {kusuma.bio}')

kusuma.posts.extend(['Graduation.png','Fest.png','Travelling.mp4'])
print(f'After Posts: {kusuma.posts}')

kusuma.NRfollowers='prathyusha'
kusuma.NRfollowers='kavitha'
kusuma.NRfollowers='madhavi'
print(f'After Followers: {kusuma.NRfollowers}')


kusuma.NRfollowing='megana'
kusuma.NRfollowing='swathi'
kusuma.NRfollowing='maheswari'
kusuma.NRfollowing='sowmya'
kusuma.NRfollowing='bharathi'
kusuma.NRfollowing='deepthi'
print(f'After Following: {kusuma.NRfollowing}')

sowmya= Profile('sowmya','sow978')
print('sowmya Details'.center(40,'-'))

print('\nBefore Cnanging')
print(f'Before Username: {sowmya.username}')
print(f'Before Password: {sowmya.getPassword}')
print(f'Before Bio: {sowmya.bio}')
print(f'Before Posts: {sowmya.posts}')
print(f'BeforeFollowers: {sowmya.NRfollowers}')
print(f'Before Following: {sowmya.NRfollowing}')


print('\nAfter Changing')
sowmya.username='bsowmya'
print(f'After Username: {sowmya.username}')

sowmya.setPassword('sowmya@978')
print(f'After Password: {sowmya.getPassword()}')


sowmya.bio='Learner'
print(f'After Bio: {sowmya.bio}')

sowmya.posts.extend(['songs.mp4','Photos.jpg'])
print(f'After Posts: {sowmya.posts}')

sowmya.NRfollowers='jyoshna'
sowmya.NRfollowers='bharani'
sowmya.NRfollowers='yaswanthi'
print(f'After Followers: {sowmya.NRfollowers}')


sowmya.NRfollowing='akhila'
sowmya.NRfollowing='akshaya'
sowmya.NRfollowing='maheswari'
sowmya.NRfollowing='kusuma'
sowmya.NRfollowing='harika'
sowmya.NRfollowing='lakshmi'
print(f'After Following: {sowmya.NRfollowing}')


#OUTPUT:
'''
kusuma, Your account is created. Have fun with Instagram
-------------kusuma Details-------------

Before Changing
Before Username: kusuma
Before Password: <bound method Profile.getPassword of <__main__.Profile object at 0x000002808196B770>>
Before Bio: 
Before Posts: []
Before Followers: set()
Before Following: set()

After Changing
After Username: skusumalatha
After Password: kusuma@123
After Bio: Blogger
After Posts: ['Graduation.png', 'Fest.png', 'Travelling.mp4']
After Followers: {'prathyusha', 'kavitha', 'madhavi'}
After Following: {'swathi', 'sowmya', 'bharathi', 'maheswari', 'deepthi', 'megana'}

sowmya, Your account is created. Have fun with Instagram
-------------sowmya Details-------------

Before Cnanging
Before Username: sowmya
Before Password: <bound method Profile.getPassword of <__main__.Profile object at 0x00000280826D3250>>        
Before Bio:
Before Posts: []
BeforeFollowers: set()
Before Following: set()

After Changing
After Username: bsowmya
After Password: sowmya@978
After Bio: Learner
After Posts: ['songs.mp4', 'Photos.jpg']
After Followers: {'bharani', 'yaswanthi', 'jyoshna'}
After Following: {'akshaya', 'harika', 'maheswari', 'akhila', 'kusuma', 'lakshmi'}'''