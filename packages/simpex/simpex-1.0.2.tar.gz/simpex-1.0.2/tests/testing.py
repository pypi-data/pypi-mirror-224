# Testing program for simpex module

# ---------------------------------

# import
from simpex import simpex
import re

# ---------------------------------

# Built-in patterns

# creating object
pattern = simpex()
emails = simpex(['admin@email.com', 'test@mail.net', 'canyougetme@gmail.com'])

email_list = [
    'admin@email.com',
    'test@mail.net',
    "test@yahoo.com",
    "admin@proton.me",
    "john.doe@example.com",
    "jane.smith@test.co.uk",
    "info@company.org",
    "contact_us@business.net",
    "admin@website.org",
    "webma456ster@domain.net",
]

email = simpex(email_list)

# print(pattern.patterns('LIST'))
# print(pattern.patterns('url'))
# print(emails.regex())
print(email.regex())

# ---------------------------------

# Custom patterns

ran_num = [9854625137, 78546958862, 5462513, 98546251378, 98546142513789] # random numbers
ten_dig_num = [9854625137, 7854695886, 5462556513, 9854625137, 9854614251] # 10 digit numbers
ten_alpha_num = ['98W46251as', '78G46958fd', '54F25565fd', '985F6251hg', '98F46142ty'] # 10 digit numbers
cre_cards = ['1234-1234-1234-1234', '4564-5644-5644-5644', '7894-7894-7894-7894', '1234-1234-1234-1234']
email_list = ["tE-77st@gma7il.com", "eMai-l@fsd5Asd.co", "asD2asd@retert.sAert"]

rn = simpex(ran_num, False)
tdn = simpex(ten_dig_num)
tan = simpex(ten_alpha_num)
cc = simpex(cre_cards)
em = simpex(email_list, False)

# print(rn.regex())
# print(tdn.regex())
# print(tan.regex())
# print(cc.regex())
# print(em.regex())


# ---------------------------------

# API testing

single_email = ["test@gmail.com, email@fsdsd.co, asdasd@retert.swert"]

# obj = simpex(single_email)
# print(obj.api())
# print(obj.api(1))
