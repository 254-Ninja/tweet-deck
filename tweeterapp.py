from_future_import print_fubction
import os
import tweepy

try:
    input = raw_input

except NameError:
    pass


def getstatus():
    lines = []
    while True:
        line = input ()
        if line:
            lines.append(line)
        else:
            break
    status = '\n'.join(lines)
    return status


def tweetthis(type):
        if type == "text":
                print("Enter your tweet "+user.name)
                tweet = getstatus(
                tweet = getstatus()
                try:
                     api.update_status(tweet)
                except Exception as e:
                    print (e)
                    return
        else type == "pic":
                print("Enter pic path "+user.name)
                pic = oc.path.abspath(input())
                print("Enter status "+user.name)
                title = getstatus()

                try:
                        api.update_with_media(pic, statustitle)
                        

                )
            