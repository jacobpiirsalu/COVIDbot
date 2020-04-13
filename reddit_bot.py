# import praw
# import prawcore

# import re
# import requests
# import time
# import traceback

# class Bot(object):
#      def __init__(self):
#           self.r = praw.Reddit('Main')
#           self.response = 'Wow, hello there!'
#           self.regex = re.compile(r'hs62hs', re.MULTILINE | re.IGNORECASE)

#       def run(self):
#           for message in self.r.inbox.unread(limit=25):
#               if self.regex.search(message.body.lower()):
#                     message.reply(self.response)
#              else:
#                  r = requests.get(
#                       'http://quotesondesign.com/wp-json/posts?filter[orderby]=rand').json()[0]
#                   quote, author = re.compile(
#                      r'<[^>]+>').sub('', r.json()[0]['content']), r.json()[0]['title']
#                  message.reply('"{0}" - {1}'.format(quote, author))

#   if __name__ == '__main__':
#        bot = Bot()

#         while 1:
#             try:
#                 bot.run()

#             except praw.exceptions.APIException:
#                 print('An API exception happened.')
#                 time.sleep(30)
#             except prawcore.exceptions.ServerError:
#                 print('503 error occurred.')
#                 time.sleep(180)
#             except prawcore.exceptions.InvalidToken:
#                 print('401 error: Token needs refreshing.')
#                 time.sleep(30)
#             except (KeyboardInterrupt, SystemExit):
#                 raise
#             except:
#                 traceback.print_exc()
#                 time.sleep(30)


import praw

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("learnpython")

for submission in subreddit.hot(limit=5):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------------\n")