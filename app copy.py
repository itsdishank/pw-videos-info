from flask import Flask, render_template
import re
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def homepage():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

    driver.get("https://www.youtube.com/@PW-Foundation/videos")

    yt_html = driver.page_source

    yt_soup = BeautifulSoup(yt_html,"html.parser")

    video_urls = yt_soup.find_all('a',{"class":"yt-simple-endpoint inline-block style-scope ytd-thumbnail"})

    urls_list = []

    for i in video_urls[1:6]:
        urls_list.append("https://www.youtube.com"+i['href'])

    thumbnail_url = yt_soup.find_all('img',{'class':"yt-core-image--fill-parent-height yt-core-image--fill-parent-width yt-core-image yt-core-image--content-mode-scale-aspect-fill yt-core-image--loaded"})

    image_urls_list = []

    for image_url in thumbnail_url[0:5]:
        image_urls_list.append(image_url['src'])

    video_titles = yt_soup.find_all('a',{'class':'yt-simple-endpoint focus-on-expand style-scope ytd-rich-grid-media'})

    video_title_list = []

    for video_title in (video_titles[0:5]):
        video_title_list.append(video_title.text)

    video_views = yt_soup.find_all('span',{'class':'inline-metadata-item style-scope ytd-video-meta-block'})

    count = 0
    video_views_list = []

    for views in video_views:
        if count >=5:
            break
        else:
            if re.search("^[0-9].*views$",views.text):
                video_views_list.append(views.text)
                count+=1

    uploaded_time = yt_soup.find_all('span',{'class':'inline-metadata-item style-scope ytd-video-meta-block'})

    count = 0
    uploaded_time_list = []

    for time in uploaded_time:
        if count >=5:
            break
        else:
            if re.search("[0-9].*ago$",time.text):
                uploaded_time_list.append(time.text)
                count+=1

    # sample dictionary with keys as column names and values as lists
    my_dict = {'URL': urls_list,
            'Image URL': image_urls_list,
            'Video Title': video_title_list,
            'Views': video_views_list,
            'time': uploaded_time_list
            }
    my_dict_list = []

    # open a new CSV file for writing with DictWriter
    with open('pw videos info/my_file.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=my_dict.keys())

        # write the header row with the column names
        writer.writeheader()

        # write the data rows with values from the dictionary
        for i in range(len(my_dict['URL'])):
            row_data = {key: my_dict[key][i] for key in my_dict.keys()}
            my_dict_list.append(row_data)
            writer.writerow(row_data)

    return render_template('result.html', my_dict_list=my_dict_list)

if __name__=="__main__":
    app.run(host="0.0.0.0")
