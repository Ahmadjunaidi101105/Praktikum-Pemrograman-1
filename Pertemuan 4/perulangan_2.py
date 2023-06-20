# sistem login seerhana 
login_chance = 3

while login_chance > 0:
    
    username = input("Masukan username: ")
    password = input("Masukan password: ")
    
    login_success = (username == "junaaa") and (password == "badrul")
    
    if login_success:
        print("login suceess!")
        break
    
    else:
        login_chance = login_chance - 1 
        print(f"login gagal! kesempatan mencoba: {login_chance}")
        
        


        