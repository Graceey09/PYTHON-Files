import re


def mail_validator(emails: list):
    valid_mail_list = []
    invalid_mail_list = []
    for mails in emails:
        re.search(r'\d + \w', mails)
        if re.search(r'@', mails):
            if re.search(r'\d', mails):
                if re.search(r'.', mails):
                    if re.search(r'@', mails):
                        valid_mail_list.append(mails)
                else:
                    print('A valid mail must contain an @')
                    invalid_mail_list.append(mails)
            else:
                print('Missing . after email')
                invalid_mail_list.append(mails)
        else:
            print('Your email cannot start with an @')
            invalid_mail_list.append(mails)
    return valid_mail_list


if __name__ == '__main__':
    print(
        mail_validator(["wechat.com", "grace95@gmail.com", "@precious.com", "Prisca8@yahomail.com", "yuo@gmail@..com"]))
