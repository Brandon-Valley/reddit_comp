import json
 

def print_str_wo_error(str):
    output = ''
    
    for char in str:
        try:
            print(char, end = '')
        except:
            print('[' + format(ord(char), "x") + ']', end = '')
            
    print('')
 
 
 
with open("C:/Users/Brandon/Documents/Personal_Projects/reddit_comp/vids_to_compile/LOG_FILES/01-06-2019_11-02-26/POSTS.json") as json_file:  
    data = json.load(json_file)
    
    
    print(data["1"])
    
    
#     for p in data['people']:
#         print('Name: ' + p['name'])
#         print('Website: ' + p['website'])
#         print('From: ' + p['from'])
#         print('')
         
        
        
        
# import json
# 
# data = {}  
# data['people'] = []  
# data['people'].append({  
#     'name': 'Scott',
#     'website': 'stackabuse.com',
#     'from': 'Nebraska'
# })
# data['people'].append({  
#     'name': 'Larry',
#     'website': 'google.com',
#     'from': 'Michigan'
# })
# data['people'].append({  
#     'name': 'Tim',
#     'website': 'apple.com',
#     'from': 'Alabama'
# })
# 
# with open('data.json', 'w') as outfile:  
#     json.dump(data, outfile)