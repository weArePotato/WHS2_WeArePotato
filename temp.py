import os

temp = []

for root, dirs, files in os.walk("./data/pypi/malicious/Backstabbers-Knife-Collection-master/pypi"):
  temp = dirs
  break
print(temp)

for root, dirs, files in os.walk("./data/pypi/malicious/pypi_malregistry-main"):
  for dir in dirs:
    if dir not in temp:
      print(dir)
  break