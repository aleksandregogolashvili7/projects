# import re
# import sys


# def main():
#     print(parse(input("HTML: ")))


# def parse(s):
#     matches=re.search(r"embed/",s)
#     if matches:
#         s=s.split('"')

#         new=s[1]

#         new=new.replace("www.","")
#         new=re.sub(r"embed/","",new)
#         new=new.replace("be","")
#         new=new.replace("com","be")
#         return new
#     else:
#         return None




# if __name__ == "__main__":
#     main()
import re


def parse(s):
    pattern = r'src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)"'
    match = re.search(pattern, s)
    if match:
        video_id = match.group(1)
        return f"https://youtu.be/{video_id}"
    else:
        return None
