# Ransom Note
ransomNote = "a"
magazine = "b"

st = ransomNote
ransomNote = Counter (ransomNote)
magazine = Counter(magazine)
for ch in st:
    if ransomNote[ch]>magazine[ch]:
        return False
return True
