def invalid_mail(mail):
    letter_list = []
    for i in mail:
        letter_list.append(i)

    if letter_list.count("@") == 1 and letter_list.count(".") >= 1:
        print("Valid mail")
        return True
    else:
        print("Invalid mail")
        return False


mail_str = str(input("Mail:"))

print(invalid_mail(mail_str))