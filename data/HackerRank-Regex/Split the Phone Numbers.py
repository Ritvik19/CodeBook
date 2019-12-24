import re

PHN = re.compile(r"(\d{1,3})(-| )(\d{1,3})(-| )(\d{4,10})")

for n in range(int(input())):
    phnnum = PHN.findall(input())[0]
    print(
        f"CountryCode={phnnum[0]},LocalAreaCode={phnnum[2]},Number={phnnum[4]}")
