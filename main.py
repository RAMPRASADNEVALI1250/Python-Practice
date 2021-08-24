email = input("Enter email id :").strip()
user = email[:email.index("@")]
domain = email[email.index("@")+1:email.index(".")]
print(f"user name is {user} and domain name is {domain}")
