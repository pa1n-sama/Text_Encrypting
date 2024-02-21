import os 
import random
import json

def key_genetration():
    Key = {}
    ordered_character_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9',"'",'.',',',' ']
    copy_ordered_character_list = ordered_character_list.copy()
    for i in ordered_character_list:
        var = random.choice(copy_ordered_character_list)
        copy_ordered_character_list.remove(var)
        Key.setdefault(i,var)
    check = input('You wanna save the Key file?(Y/N): ')
    if check.lower() in 'yes':
        with open('Key.json','w') as file:
            json.dump(Key,file)
    return Key