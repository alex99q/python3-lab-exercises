import re

ip_regex = "^(((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.)){3})(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
web_info_regex = "\"(GET|POST) .+\""

ip_count_dict = {}
web_info_count_dict = {}

with open("access_log.txt", "r") as file:
    current_line = ' '
    while current_line != '':
        current_line = file.readline()
        match_ip = re.match(ip_regex, current_line)
        match_web_info = re.search(web_info_regex, current_line)

        if match_ip:
            matched_str = match_ip.group()

            if matched_str in ip_count_dict:
                ip_count_dict[matched_str] += 1
            else:
                ip_count_dict[matched_str] = 1

        if match_web_info:
            matched_str = match_web_info.group().split()[1]

            if matched_str in web_info_count_dict:
                web_info_count_dict[matched_str] += 1
            else:
                web_info_count_dict[matched_str] = 1

top5_ip_dict = {}
top5_web_info_dict = {}

for n in range(0, 5):
    top_ip = ""
    top_ip_count = 0

    top_web_info = ""
    top_web_info_count = 0

    for current_ip, current_ip_count in ip_count_dict.items():
        if current_ip_count > top_ip_count and current_ip not in top5_ip_dict:
            top_ip_count = current_ip_count
            top_ip = current_ip

    for current_web_info, current_web_info_count in web_info_count_dict.items():
        if current_web_info_count > top_web_info_count and current_web_info not in top5_web_info_dict:
            top_web_info_count = current_web_info_count
            top_web_info = current_web_info

    top5_ip_dict[top_ip] = top_ip_count
    top5_web_info_dict[top_web_info] = top_web_info_count

print(top5_ip_dict)
print(top5_web_info_dict)