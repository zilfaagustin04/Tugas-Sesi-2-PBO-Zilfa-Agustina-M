#membuat class
class AC: 
  #fungsi construktor
  def __init__(self, nama_brand, ukuran_suhu, tingkat_suhu): 
     self.nama_brand = nama_brand
     self.ukuran_suhu = ukuran_suhu
     self.tingkat_suhu = tingkat_suhu

  #membuat fungsi dari AC
  def nyalakanAC(self):
      print('Ac menyala ', self.nama_brand)

  def matikanAC(self):
      print('Ac dimatikan ', self.nama_brand)

  def gantiUkuranSuhu(self):
      print('Ac gantishu ', self.nama_brand)


#membuatobjek
ac_ruang_tamu = AC('LG', '16', 20)
ac_ruang_kamar = AC('SAMSUNG', '17', 25)
#memanggil fungsi daro obyek
ac_ruang_tamu.nyalakanAC()
ac_ruang_kamar

#memasukkan attribut ke objek
ac_ruang_tamu.nama_brand = 'LG'
ac_ruang_kamar.nama_brand = 'SAMSUNG'

#print
print(ac_ruang_kamar.nama_brand)
print(ac_ruang_tamu.nama_brand)