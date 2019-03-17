website_list = ("www.zframez.com", "www.wikipedia.org", "www.asp.net", "www.abcd.in")

suffix_list = []

for website in website_list:
    suffix_list.append(website.split(".")[2])

print(*suffix_list, sep=", ")