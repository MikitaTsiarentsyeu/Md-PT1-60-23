def reverString(text, i):
  if (len(text) + i) == 0:
    return text[0]
  else:
    return text[i] + reverString(text, i-1)

text = "Теплый весенний день"
print(reverString(text, -1))