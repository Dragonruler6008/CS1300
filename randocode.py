"""
_summary_
"""
string = "11122333444555"
result = []
prev_char = None
for char in string:
  if char.isdigit():
    if prev_char != char:
      result.append(char)
      prev_char = char
  else:
    result.append(char)
    prev_char = None
print(''.join(result)) # Output: 12345
