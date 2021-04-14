import pandas as pd
import requests
from time import sleep




import os
from requests import get
from bs4 import BeautifulSoup
import json
from random import randint
import requests
import time, sys
from queue import Queue
from threading import Thread
import timeit

print ('''
                                                
   (                                  )  
 ( )\         )        (           ( /(  
 )((_)  (    (     ___ )\  (    (  )\()) 
((_)_   )\   )\  '|___((_) )\ ) )\(_))/  
 | _ ) ((_)_((_))      (_)_(_/(((_) |_   
 | _ \/ _ \ '  \()     | | ' \)|_-<  _|  
 |___/\___/_|_|_|      |_|_||_|/__/\__|  
                                         
>---------------------------------------->
snapchat: flaah999 
''')




class Instagram:
    def __init__(self, username):
        self.username = str (username)


def clear():
    if os.name == 'nt':
        os.system ('cls')
    else:
        os.system ('clear')


clear ()


print ('============= new privacy ============')

THREADCOUNT = 100
queue = Queue ()
notTaken = []


def Read(filename):
    return [line.strip () for line in open (filename)]


def DoWork(line):
    Sesson = requests.Session ()

    req = Sesson.get ('http://www.instagram.com/%s' % line)
    print ('جيد يوجد الحساب {0}'.format (line))


    if req.status_code == 404:
        notTaken.append (line)


def Worker(q):
    while True:
        line = q.get ()
        DoWork (line)
        time.sleep (1)
        q.task_done ()


for i in range (THREADCOUNT):
    worker = Thread (target=Worker, args=(queue,))
    worker.setDaemon (True)
    worker.start ()


def main():
    tic = timeit.default_timer ()
    if len (sys.argv) < 2:
        try:
            Accounts = Read ('accounts.txt')
        except IOError:
            print ('الرجاء إنشاء ملف يسمى accounts.txt مع اضافة اسماء المستخدمين داخله')
            input ()
            sys.exit ()
    else:
        Accounts = Read (sys.argv[1])

    for Account in Accounts:
        queue.put (Account)

    queue.join ()

    for a in notTaken:
        print ('الحساب %s غير موجود !' % a)
        with open ('الحسابات_غير_مودجودة.txt', 'w+') as File:
            for i in notTaken:
                File.write (i + '\n')




if __name__ == '__main__':
    main ()

    print ('============= new data ============')


class Instagram:
    def __init__(self, username):
        self.username = str (username)

    def get_request(self):
        """
        Returns page contents
        :return str:
        """
        request = requests.get ('https://www.instagram.com/' + self.username)
        if request.status_code == 200:
            return request.content
        else:
            raise Exception (" This username is not used: {}".format (self.username))

    def content_parser(self):
        """
        Returns parsed page contents
        :return str:
        """
        content = self.get_request ()
        source = BeautifulSoup (content, 'html.parser')
        return source

    def get_info(self):
        """
        Returns instagram infos
        :return dict:
        """
        source = self.content_parser ()
        description = source.find ("meta", {"property": "og:description"}).get ("content")
        info_list = description.split ("-")[0]
        followers = info_list[0:info_list.index ("Followers")]
        info_list = info_list.replace (followers + "Followers, ", "")
        following = info_list[0:info_list.index ("Following")]
        info_list = info_list.replace (following + "Following, ", "")
        posts = info_list[0:info_list.index ("Posts")]
        results = {"followers": followers, "following": following, "posts": posts}
        return results

    def print_info(self):
        """
        Prints all informations
        """
        url = "https://www.instagram.com/" + self.username + "/?__a=1"
        r = requests.get (url)
        email = str (r.json ()["graphql"]["user"]["business_email"])
        photo = str (r.json ()["graphql"]["user"]["profile_pic_url_hd"])
        id = str (r.json ()["graphql"]["user"]["id"])
        info = self.get_info ()
        #______________________________________
        s = '35a2d547d3b6ff400f713948cdffe0b789a903f86117eb6e2f3e573079b2f038.{"q":\"' + self.username + '\","guid":"b449de3c-1663-47bc-8cca-e83b570b60d1","device_id":"615d8b7997acf12b"}'
        userAAgent = "Instagram 99.4.0"
        url = 'https://i.instagram.com/api/v1/users/lookup/'
        myobj = {'signed_body': s, "ig_sig_key_version": "9"}

        x = requests.post (url, headers={'User-Agent': userAAgent}, data=myobj)
        flo = str (x.json ()["obfuscated_email"])
        print ("")
        print (" اسم المستخدم: {}".format (self.username))
        print (" المتابعون: {}".format (info["followers"]))
        print (" يتابع: {}".format (info["following"]))
        print (" المنشورات: {}".format (info["posts"]))
        print ("الاميل التواصل:", email)
        print ("اي دي الحساب: ", id)
        print ("صورة العرض:", photo)
        print ("الاميل الموثق في الحساب:", flo)


        print ("")
        print (" -" * 15)


class Helper:
    @staticmethod
    def read_file(filename):
        """
        Returns account lists
        :param filename:
        :return list:
        """
        accounts = [line.rstrip ('\n') for line in open (filename, encoding="utf8")]
        return accounts

    @staticmethod
    def retry():
        """
        Decides wanna try again
        :return boolean:
        """
    


if __name__ == "__main__":
    while True:
        accounts = Helper.read_file ("accounts.txt")
        for account in accounts:
            info = Instagram (account)
            try:
                info.print_info ()
            except Exception as e:
                print (e)
                
                

        retry = Helper.retry ()
        if not retry:
            break
            


def data_posts_count(searched_tag):
    'to get primary dataframe for the seareched tag and its total posts count'
    url = 'https://www.instagram.com/explore/tags/' + searched_tag + '/?__a=1'
    response = requests.get (url)
    data = response.json ()
    total_posts_count = data['graphql']['hashtag']['edge_hashtag_to_media']['count']
    return data, total_posts_count


def extract_tags(x):
    'to extract hashtags/keywords from a text x if any'
    if x is pd.np.nan:
        return ''
    return ','.join (''.join ([i for i in x.split () if i.startswith ('#')]).split ('#')[1:])


def get_temp_df(data):
    'to get temporary dataframe'
    # top_posts and other posts
    top_posts = data['graphql']['hashtag']['edge_hashtag_to_top_posts']['edges']
    posts = data['graphql']['hashtag']['edge_hashtag_to_media']['edges']
    # get the node where data located
    clean_top_posts = [i['node'] for i in top_posts]
    clean_posts = [i['node'] for i in posts]
    # select the interested columns
    columns = ['owner', 'shortcode', 'taken_at_timestamp', 'edge_media_to_caption', 'edge_media_to_comment', \
               'edge_liked_by', 'is_video', 'video_view_count']
    # set up the dataframe
    top_posts_df = pd.DataFrame (clean_top_posts, columns=columns)
    top_posts_df['is_top'] = True
    posts_df = pd.DataFrame (clean_posts, columns=columns)
    posts_df['is_top'] = False
    temp_df = top_posts_df.append (posts_df, sort=False)
    return temp_df


def insta_scraper(searched_tag):
    """
    colllect the needed data for the interested hashtag
    ===================================================
    INPUT:
    searched_tag : str
    ---------------------------------------------------
    OUTPUT:
    {searched_tag}_data.csv file
    data_df  : Pandas DataFrame with
             -'user_id': user id number, str
             -'url':post link, str
             -'date': date of post , datetime64[ns]
             -'text': post text , str
             -'num_comments': number of comments , int64
             -'num_likes': number of likes , int64
             -'is_video':is vedio post or not , bool
             -'video_view_count':number of vedio views if is_vedio: True , float64
             -'is_top': if the post is top post , bool
             -'other_tags' related hashtags/key words
    """
    # url
    url = 'https://www.instagram.com/explore/tags/' + searched_tag + '/?__a=1'
    # get the previous data and total posts count
    data, total_posts_count = data_posts_count (searched_tag)
    print (f'There is {total_posts_count:,} posts for #{searched_tag}')
    # set up the dataframe
    data_df = get_temp_df (data)
    # has next page (True or False)
    has_next_page = data['graphql']['hashtag']['edge_hashtag_to_media']['page_info']['has_next_page']
    # get how many posts to scrape
    deep = int (input ('أدخل عدد المشاركات التي تريد استخزاج:'))
    # get all data
    while has_next_page:
        if len (data_df) >= deep:
            break
        else:
            # end cursor to be put after (max_id = ) to go to next page
            next_page = data['graphql']['hashtag']['edge_hashtag_to_media']['page_info']['end_cursor']
            new_url = url + '&max_id=' + next_page
            # parse the interested url
            sleep (2)
            response = requests.get (new_url)
            # data from json file
            data = response.json ()
            has_next_page = data['graphql']['hashtag']['edge_hashtag_to_media']['page_info']['has_next_page']
            temp_df = get_temp_df (data)
            data_df = temp_df.append (data_df, sort=False)
    data_df.reset_index (drop=True, inplace=True)

    # rename columns
    data_df.rename (columns={"edge_media_to_caption": "text", "edge_media_to_comment": "num_comments", \
                             "taken_at_timestamp": "date", "edge_liked_by": "num_likes", \
                             "owner": "user_id", "is_video": "is_video", \
                             "video_view_count": "video_view_count", 'shortcode': 'url'}, inplace=True)

    # fix the columns
    data_df.user_id = data_df.user_id.apply (lambda x: x['id'])
    data_df.url = data_df.url.apply (lambda x: 'https://www.instagram.com/p/' + x + '/')
    data_df.date = pd.to_datetime (data_df.date, unit='s')
    data_df.text = data_df.text.apply (lambda x: x['edges'][0]['node']['text'] if len (x['edges']) == 1 else pd.np.nan)
    data_df.num_comments = data_df.num_comments.apply (lambda x: x['count'])
    data_df.num_likes = data_df.num_likes.apply (lambda x: x['count'])
    # get other tags
    data_df['other_tags'] = data_df.text.apply (lambda x: extract_tags (x))

    # save to csv file to the working directory
    path_to_data = f'{searched_tag}_data.csv'
    # save data
    data_df.to_csv (path_to_data, encoding='utf-8-sig', index=False)
    return data_df


if __name__ == "__main__":
    tag = str (input ('ادخل عنوان الهشتاق:'))
    print ('Collecting data....')
    data = insta_scraper (tag)
    print ('Data collection has been completed.')