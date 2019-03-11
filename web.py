from IPython.display import Image as IPythonImage
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import requests


def display_cover(top,bottom ):
    
    name='album_art_raw.png'
  
    album_art_raw = requests.get('https://picsum.photos/500/500/?random')

    with open(name,'wb') as album_art_raw_file:
       album_art_raw_file.write(album_art_raw.content)

    img = Image.open("album_art_raw.png")
    draw = ImageDraw.Draw(img)


    fnt = ImageFont.truetype("arial.ttf", 28)
    band_x, band_y = 50, 50
    album_x, album_y = 50, 400

    outline_color ="black"
    

    draw.text((band_x-1, band_y-1), top,font=fnt, fill=outline_color)
    draw.text((band_x+1, band_y-1), top,font=fnt, fill=outline_color)
    draw.text((band_x-1, band_y+1), top,font=fnt, fill=outline_color)
    draw.text((band_x+1, band_y+1), top,font=fnt, fill=outline_color)
    
    draw.text((album_x-1, album_y-1), bottom, font=fnt, fill=outline_color)
    draw.text((album_x+1, album_y-1), bottom, font=fnt, fill=outline_color)
    draw.text((album_x-1, album_y+1), bottom, font=fnt, fill=outline_color)
    draw.text((album_x+1, album_y+1), bottom, font=fnt, fill=outline_color)

    draw.text((band_x,band_y),top,(255,255,255))
    draw.text((album_x, album_y),bottom,(255,255,255))

    return img
# ADD Python and Data Science to image at top and bottom
img = display_cover("Python", "Data Science")
img.save('python+datascience.png')
IPythonImage('python+datascience.png')

# Using Requests to get random wikipedia page and taking out title out of it
# for title given to album and band name

wikipedia_link='https://en.wikipedia.org/wiki/Special:Random'
raw_random_wikipedia_page = requests.get(wikipedia_link)
page = raw_random_wikipedia_page.text

# extracting title of the page for band_title
start = page.find('<title>')
end = page.find('</title>')
wiki_title = page[start+7:end]
band_title = wiki_title.strip('- Wikipedia')

# extracting title of the new page for album_title
raw_random_wikipedia_page = requests.get(wikipedia_link)
page = raw_random_wikipedia_page.text
start = page.find('<title>')
end = page.find('</title>')
wiki_title = page[start+7:end]
album_title = wiki_title.strip('- Wikipedia')

# print them out:-
print("Your band: ", band_title)
print("Your album: ", album_title)

# set them on the image by using display_cover function
album_cover = display_cover(band_title,album_title)
album_cover.save(band_title+ "and" + album_title +'.png')
IPythonImage(band_title+ "and" + album_title +'.png')
album_cover.show()