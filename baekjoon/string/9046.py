num = int(input())

for i in range(num): 
  string = input().replace(" ", "")
  alphabet = {}
  for j in string:
    if j in alphabet:
      alphabet[j] += 1
    else:
      alphabet[j] = 1

  max_val = max(alphabet.values())
  max_char = [key for key, value in alphabet.items() if value == max_val]

  if len(max_char) > 1:
    print("?")
  else:
    print(max_char[0])
