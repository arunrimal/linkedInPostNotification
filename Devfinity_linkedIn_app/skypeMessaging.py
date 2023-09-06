import json
from skpy import Skype

# dect={
#     'Post_date': '5 hrs ago',
#     'Post_URL':'https://www.linkedin.com/posts/linkedin-news-asia_the-wrap-up-monday-july-25-2022-activity-6957262149849165824-nrl3?utm_source=linkedin_share&utm_medium=member_desktop_web'
# }

login_content = open('config/skypeconfig.json')
config = json.load(login_content)
skyplogin = Skype(config['username'], config['password'])


Id_content = open('config/skypeGroupId.json')
Id_config = json.load(Id_content)


def get_post_data(data):    
    
    return data 

#contact = skyplogin.contacts [id]

def send_message(body):



    msg = f'''Devfinity last post was {body['Post_date']} \n {body['Post_URL']} '''

    # for group chat in skype as channel
    channel = skyplogin.chats.chat(Id_config['id'])      
    channel.sendMsg(msg)

    # for person chat in skype as contact
    # contact = skyplogin.contacts[Id_config['id']]
    # contact.chat.sendMsg(msg)


# data = get_post_data(dect)
# send_message(data)