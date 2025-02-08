s=input()
upper_count=0
lower_count=0
for char in s:
    if char.isupper():
        upper_count=upper_count+1
    else:
         lower_count=lower_count+1
if upper_count>lower_count:
    s=s.upper()
else:
    s=s.lower()
print(s)
