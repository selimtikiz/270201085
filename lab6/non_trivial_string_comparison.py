e_mail = input("enter an e-mail")
static_mail = "ceng113@example.com"
while True:
    e_mail_1 = e_mail.split("@")
    e_mail_1_0 = e_mail_1[0]
    e_mail_1_1 = e_mail_1[1]
    e_mail_1_0 = e_mail_1_0.replace(".","").lower()
    e_mail_1_1 = e_mail_1_1.lower()
    new_e_mail=(f"{e_mail_1_0}"+"@"+f"{e_mail_1_1}")
    if new_e_mail != static_mail:
        print(new_e_mail)
        e_mail = input("enter an e-mail again")
    else:
        print("correct")
        break