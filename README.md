# DemoProject
Veri Bilimci Case Study

scv_to_db.py file
  1) csv uzantılı dosyalar csv_list listesine atildı.
  2) Her bir scv dosyalarını pandas yapısna çevril.
  3) pandas veri yapısındandan sql verisına haritalandı
  4) for döngüsü ile her bir pandas dataframe ler postgresql database çevirild.
  5) for döngüsü içinde oncelikle tablo adı ve colun adaları düzeltildi.
      xyz[0] -> xyz_0_ şeklinde
  6) Database baglanıp pandas dataframe deki veriler tablolaştırıldı.
