#1. Pengalaman saya menggunakan python adalah ketika saya mengikuti kelas python beginner dari sanberlearn
#2. Ada kelas lanjutan lagi tentang python for data science untuk bidang image recognition atau video analytics
#3. Kodingannya dibawah ini

class manipulasi:
  def __init__(self):
    self.kalimat = input("data = ")
  
  def kapital(self):
    print(self.kalimat.capitalize())
  
  def kecil(self):
    print(self.kalimat.lower())
  
  def besar(self):
    print(self.kalimat.upper())

  def pisah(self):
    print(self.kalimat.split())

tes = manipulasi()
tes.kapital()
tes.kecil()
tes.besar()
tes.pisah()
