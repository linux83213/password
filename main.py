import string
import hashlib
import json 
import os 

stockpassword = "mdp_stocker.json"

def mdp_valid_json():
    if not os.path.exists(stockpassword):
        return {}
    with open(stockpassword, 'r') as fichier:
        return json.load(fichier)

def add_mdp_json(mot_pass):
    with open(stockpassword, 'a') as fichier:
        pass
        json.dump (mot_pass, fichier, indent=4)


def mot_pass_valid(mot_pass): 
    mot_pass_ok = True 

    if len (mot_pass) >=8 : 
        pass
    else : 
        mot_pass_ok = False
        print ("le mot de passe doit contenir au moins 8 caractère")
    if any (caractère.isupper() for caractère in mot_pass) : 
        pass 
    else : 
        mot_pass_ok : False  
        print ("le mot de passe doit contenir au moins une majuscule")
    if any (caractère.islower ()for caractère in mot_pass) : 
        pass
    else :
        mot_pass_ok = False 
        print ("le mot de passe doit contenir au moins une minuscule")
    if any (caractère.isdigit()for caractère in mot_pass) :
        pass 
    else :
        mot_pass_ok = False 
        print ("le mot de passe doit contenir au moins un chiffre")
    if any (caractere in string.punctuation for caractere in mot_pass) : 
        pass
    else :
        mot_pass_ok = False 
        print ("le mot de passe doit contenir au moins un caractère spécial")

    return mot_pass_ok
mdp = mdp_valid_json()
while True :
    
    mot_pass = input ("Veuillez choisir un mot de passe :")
    

    if mot_pass_valid (mot_pass): 
        print ("le mot de passe est correct")
        break
    else : 
        print ("le mot de passe est incorrecte")


def hash_password():
    return hashlib.sha256 (mot_pass.encode()).hexdigest()

hash_mdp = hash_password()


list_mdp_valid = mdp_valid_json()

if mot_pass in list_mdp_valid: 
    print ("ce mot de passe existe déjà")

else:
    mdp = {"mot de passe : " : mot_pass, "hash" : hash_mdp}
    add_mdp_json(mot_pass)
    print("mot de passe garde")









