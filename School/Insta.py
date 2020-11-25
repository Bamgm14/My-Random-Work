from instagram_web_api import Client, ClientCompatPatch
from PIL import Image
 
#filePath = "sample_image_file.jpg"
#img = Image.open(filePath)
#width, height = img.size
user_name = 'bamgm14'
password = 'bamgm146'

api = Client(username=user_name, password=password)
api.login()
#api.post_photo(open('Icon_GearChronicle.png','rb').read(),caption='API Test')
