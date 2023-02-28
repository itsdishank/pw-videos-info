# from flask import Flask, render_template, request,jsonify
# from flask_cors import CORS,cross_origin
# import requests
# from bs4 import BeautifulSoup as bs
# from urllib.request import urlopen as uReq
# import logging
# import pymongo
# logging.basicConfig(filename="scrapper.log" , level=logging.INFO)

# app = Flask(__name__)

# @app.route("/", methods = ['GET'])
# def homepage():
#     return render_template("index.html")

# @app.route("/review" , methods = ['POST' , 'GET'])
# def index():
#     if request.method == 'POST':
#         try:
#             searchString = request.form['content'].replace(" ","")
#             flipkart_url = "https://www.flipkart.com/search?q=" + searchString
#             uClient = uReq(flipkart_url)
#             flipkartPage = uClient.read()
#             uClient.close()
#             flipkart_html = bs(flipkartPage, "html.parser")
#             bigboxes = flipkart_html.findAll("div", {"class": "_1AtVbE col-12-12"})
#             del bigboxes[0:3]
#             box = bigboxes[0]
#             productLink = "https://www.flipkart.com" + box.div.div.div.a['href']
#             prodRes = requests.get(productLink)
#             prodRes.encoding='utf-8'
#             prod_html = bs(prodRes.text, "html.parser")
#             print(prod_html)
#             commentboxes = prod_html.find_all('div', {'class': "_16PBlm"})

#             filename = searchString + ".csv"
#             fw = open(filename, "w")
#             headers = "Product, Customer Name, Rating, Heading, Comment \n"
#             fw.write(headers)
#             reviews = []
#             for commentbox in commentboxes:
#                 try:
#                     #name.encode(encoding='utf-8')
#                     name = commentbox.div.div.find_all('p', {'class': '_2sc7ZR _2V5EHH'})[0].text

#                 except:
#                     logging.info("name")

#                 try:
#                     #rating.encode(encoding='utf-8')
#                     rating = commentbox.div.div.div.div.text


#                 except:
#                     rating = 'No Rating'
#                     logging.info("rating")

#                 try:
#                     #commentHead.encode(encoding='utf-8')
#                     commentHead = commentbox.div.div.div.p.text

#                 except:
#                     commentHead = 'No Comment Heading'
#                     logging.info(commentHead)
#                 try:
#                     comtag = commentbox.div.div.find_all('div', {'class': ''})
#                     #custComment.encode(encoding='utf-8')
#                     custComment = comtag[0].div.text
#                 except Exception as e:
#                     logging.info(e)

#                 mydict = {"Product": searchString, "Name": name, "Rating": rating, "CommentHead": commentHead,
#                           "Comment": custComment}
#                 reviews.append(mydict)
#             logging.info("log my final result {}".format(reviews))

            
#             # client = pymongo.MongoClient("mongodb+srv://pwskills:pwskills@cluster0.ln0bt5m.mongodb.net/?retryWrites=true&w=majority")
#             # db =client['scrapper_eng_pwskills']
#             # coll_pw_eng = db['scraper_pwskills_eng']
#             # coll_pw_eng.insert_many(reviews)
#             print(reviews[0:(len(reviews)-1)])
#             print(reviews)

#             return render_template('result.html', reviews=reviews[0:(len(reviews)-1)])
#         except Exception as e:
#             logging.info(e)
#             return 'something is wrong'
#     # return render_template('results.html')

#     else:
#         return render_template('index.html')


# if __name__=="__main__":
#     app.run(host="0.0.0.0")


# import re
# import csv
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())


# driver.get("https://www.youtube.com/@PW-Foundation/videos")

# yt_html = driver.page_source

# yt_soup = BeautifulSoup(yt_html,"html.parser")

# video_urls = yt_soup.find_all('a',{"class":"yt-simple-endpoint inline-block style-scope ytd-thumbnail"})

# urls_list = []

# for i in video_url[1:6]:
#     urls_list.append("https://www.youtube.com"+i['href'])

# thumbnail_url = yt_soup.find_all('img',{'class':"yt-core-image--fill-parent-height yt-core-image--fill-parent-width yt-core-image yt-core-image--content-mode-scale-aspect-fill yt-core-image--loaded"})

# image_urls_list = []

# for image_url in thumbnail_url[0:5]:
#     image_urls_list.append(image_url['src'])

# video_titles = yt_soup.find_all('a',{'class':'yt-simple-endpoint focus-on-expand style-scope ytd-rich-grid-media'})

# video_title_list = []

# for video_title in (video_titles[0:5]):
#     video_title_list.append(video_title.text)

# video_views = yt_soup.find_all('span',{'class':'inline-metadata-item style-scope ytd-video-meta-block'})

# count = 0
# video_views_list = []

# for views in video_views:
#     if count >=5:
#         break
#     else:
#         if re.search("^[0-9].*views$",views.text):
#             video_views_list.append(views.text)
#             count+=1

# uploaded_time = yt_soup.find_all('span',{'class':'inline-metadata-item style-scope ytd-video-meta-block'})

# count = 0
# uploaded_time_list = []

# for time in uploaded_time:
#     if count >=5:
#         break
#     else:
#         if re.search("[0-9].*ago$",time.text):
#             uploaded_time_list.append(time.text)
#             count+=1