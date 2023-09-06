

# dect={
#     'Post_date': '15 hours ago',
#     'Post_URL':'https//...'
# }
# print(dect.get('Post_date'))
# print(dect)

def condition_all(post_details):

    number = int(post_details['Post_date'][0:2].replace(' ',''))
    time_unit =str(post_details['Post_date'][2:-4].replace(' ',''))
    #print(time_unit)
    #print(number)
    
    global diction,status
    status=0
    diction={}
    if (time_unit=='minutes' or time_unit=='minute'):
        status =1
        print('this is in minutes: ',number)
        diction['Post_date'] = post_details.get('Post_date')
        diction['Post_URL'] = post_details.get('Post_URL')
    
    elif (time_unit=='hour' or time_unit=='hours'):
        
        print('this is in hours: ',number)
        if number <= 12:
            status =1
            print('this is in hours below 12: ', number)
            #diction['Post_date']=str(number)+ ' hours ago'
            diction['Post_date']=post_details.get('Post_date')
            diction['Post_URL'] = post_details.get('Post_URL')
          
    else:
        status =0
        # diction['Post_date']= post_details.get('Post_date')
        # diction['Post_URL'] = post_details.get('Post_URL')
    #print(status, diction)     
    return status,diction
     

   
#condition_all(dect)



