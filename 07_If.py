is_man = True

if is_man:
  print("je bent een man")
else:
    print("je bent geen man")

is_man = True
is_lang = True

if is_man or is_lang:
  print("je bent een man of lang of beide")
else:
    print("je bent geen man en je bent niet lang")

if is_man and is_lang:
  print("je bent een lange man")
else:
    print("je bent geen man en je bent niet lang of beide")



if is_man and is_lang:
  print("je bent een lange man")
elif is_man and not(is_lang):
    print("je bent een korte man")
elif not(is_man) and is_lang:
    print("je bent geen man, maar lang")
else:
    print("je bent geen man en je bent niet lang of beide")
