# leniwy-ojciec
![alt tag](https://raw.githubusercontent.com/maciejszewczyk/leniwy-ojciec/master/screenshot.png)

## Przeczytaj, jeżeli ciągle uważasz, że to bez sensu

Jeżeli Twoje dziecko jest uczulone na niektóre produkty na przykład pieczarki lub grzyby to możesz dodać w kodzie ich listę:

```python
lista = [u'piecza', u'grzyb']
```

Następnie sprawdzić, czy szkodliwe produkty są w menu:

```python
menu = "Kakao, chleb staropolski i wieloziarnisty z masłem, wędlina, rzodkiewki, ser żółty, sałata, herbata owocowa, woda.
Zupa pieczarkowa, udziec indyczy duszony, kluski śląskie, surówka z kapusty pekińskiej, kompot.
Chleb słoneczko z masłem, jajko gotowane, szczypiorek, actimel naturalny."

for el in lista:
  if el in menu:
    print 'Rzyganie i gorączka"
```

Następnie wysłać ostrzegawczego maila by w odpowiednim czasie powiadomić przedszkole:

![alt tag](https://raw.githubusercontent.com/maciejszewczyk/leniwy-ojciec/master/screenshot2.png)
