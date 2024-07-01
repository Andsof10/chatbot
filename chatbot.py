anno_nascita = int(input('In che anno sei nato? '))
eta = 2024 - anno_nascita
alcolici = ['gin', 'vodka', 'mojito', 'rum']
analcolici = ['limonata', 'cocacola']
lista_drink = []
ordini = []

if eta >= 18:
  print('sei maggiorenne, ecco la lista dei drink disponbili: ')
  lista_drink = alcolici + analcolici

else:
  print('sei minorenne, ecco la lista dei drink disponbili: ')
  lista_drink = analcolici

while True:
  for drink in lista_drink:
    print(drink)

  ordine = input('Cosa desideri ordinare? ')

  if ordine in lista_drink:
    print('Hai ordinato: ' + ordine)
    ordini.append(ordine)

    risposta = input('Vuoi ordinare altro? (si/no) ')

    if risposta != 'si':
      print('Grazie e arrivederci')
      print('Ecco il resoconto del tuo ordine: ')
      for ordine in ordini:
        print(ordine)
      break

  else:
    while True:
      if eta < 18 and ordine in alcolici:
        print('Sei minorenne, puoi ordinare solo analcolici')
        break
      else:
        aggiungi_bevanda = input('Bevanda non disponibile. Vuoi aggiungerla alla lista drink? (si/no) ')

      if aggiungi_bevanda == 'si':
        tipo_bevanda = input('La bevanda è alcolica o analcolica? ')
      else:
        print('Va bene, Che altro desideri ordinare? ')
        break

      if tipo_bevanda == 'alcolica' and eta >= 18:
        alcolici.append(ordine)
        lista_drink = alcolici + analcolici
        print('La bevanda è stata aggiunta con successo!')
        break

      if tipo_bevanda == 'analcolica':
        analcolici.append(ordine)
        lista_drink = alcolici + analcolici
        print('Bevanda aggiunta con successo!')
        break

      else:
        print('Opzione invalida. bevanda non aggiunta.')
        break