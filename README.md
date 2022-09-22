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


data_anormality.py file


Local databaseden angular_velocity tablosunu kullanarak açısal hızın x koordinatı ile y-koordinatı arasında fark %30 dan fazla olan değerleri '1', diğerler de '0'     olarak işaretlendi.Bu değerlerde 'type' colununa yazıldı. 

Veriler işaretlenirken x ve y koordinatlari yönüdeki bileşenler vektorel fark alınarak işlem yapılmıştır. 
  
  fark = sqrt(x^2 + y^2 -2*x*y*cos(alpha)) alpha : iki vektor arasındaki açı, burada alpha = 0 olduğundan cos(alpha) = 0 : fark = sqrt(x^2 + y^2) şeklinde kullanıldı. 



DecisionTree.py

  1) database ile bağlantı kurularak velocity tablosu okundu.
  2) Databaseden okunan time colonundaki veriler object type dan datetime cevrildi.
     *(Zaman Serileri kullanmayı düşünüyordum)
  3) Makine öğrenmesi methodlarından DecisionTree algoritması kullanıldı.
  4) DecisionTreeClassifier fonksiyonunda criterion 'entropy' ve 'gini' olarak ayrı ayrı denendi
     Fakat entropy değerinde daha iyi sonuçlar alınmıştır 
  5) Dashboard içinde python streamlit kütüphanesi kullanılmıştır.
  6) İki farklı flight id olduğu için iki farklı zaman tür grafiği çizilmiştir.
