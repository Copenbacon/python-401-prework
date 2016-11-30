def cat_dog(str):
  countdog = 0
  countcat = 0
  for i in range(len(str)):
    if str[i:i+3] == 'cat':
        countcat +=1
        print countcat
    elif str[i:i+3] == 'dog':
        countdog +=1
        print countdog
  return countcat == countdog

cat_dog('catdog')
