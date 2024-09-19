# Hepsiburada Laptop Bilgisayar Fiyatlarını Çekme Projesi

Bu proje, Hepsiburada sitesinde bulunan laptop (dizüstü bilgisayar) isimlerini ve fiyatlarını çekmek için Python'da requests ve BeautifulSoup kütüphanelerini kullanarak bir web scraping uygulaması gerçekleştirmektedir.

## İçindekiler

- [Proje Hakkında](#proje-hakkında)
- [Kullanılan Kütüphaneler](#kullanılan-kütüphaneler)
- [Kullanılan Değişkenler](#kullanılan-değişkenler)
- [Nasıl Çalışır](#nasıl-çalışır)
- [Nasıl Çalıştırılır](#nasıl-çalıştırılır)
- [Örnek Çıktı](#örnek-çıktı)

## Proje Hakkında

Bu proje, Hepsiburada'daki dizüstü bilgisayar ürünlerinin isimlerini ve fiyatlarını almak için Python tabanlı bir web scraping uygulamasıdır. Veriler, `requests` kütüphanesi ile çekilir ve `BeautifulSoup` kullanılarak HTML içerisinden ayrıştırılır. Ürün isimleri ve fiyatlar, bir Python sözlüğünde tutulur ve sonuçlar ekrana yazdırılır.

## Kullanılan Kütüphaneler

- **requests**: Web sayfasını indirmek için kullanılır.
- **BeautifulSoup (bs4)**: HTML yapısını ayrıştırarak gerekli verileri çekmek için kullanılır.

## Kullanılan Değişkenler

- **url**: Verilerin çekileceği web sayfasının URL'sini tutar.
- **headers**: Web isteği yaparken tarayıcı bilgilerini belirten bir başlık, web sitesine tarayıcıdan istekte bulunulduğunu simüle eder.
- **html**: Web sayfasından çekilen ham HTML içeriği.
- **soup**: `BeautifulSoup` ile ayrıştırılan HTML yapısı.
- **liste**: Ürünlerin isimlerini içeren liste.
- **priceList**: Ürünlerin fiyatlarını içeren liste.
- **comp_dict**: Bilgisayar isimleri ve fiyatlarını anahtar-değer çiftleri halinde tutan sözlük.
- **num**: Ekrana yazdırılacak her ürün için bir sayaç.
