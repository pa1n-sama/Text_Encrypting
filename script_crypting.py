import json
from random_key_generation import key_genetration

def crypting(script):
    encrypting_dic = key_genetration()
    crypted_script = ''
    for i in script:
        crypted_script = crypted_script + encrypting_dic[i]
    return crypted_script
def decrypting(script):
    with open('Key.json','r') as file:
        json_Key=json.loads(file.read())
    decrypting_dic = {value:keys for keys,value in json_Key.items()}
    decrypted_script=''
    for i in script:
        decrypted_script = decrypted_script + decrypting_dic[i]
    return decrypted_script