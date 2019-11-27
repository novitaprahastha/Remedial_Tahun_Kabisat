kabisatInput = int(input('Masukan tahun: '))

def thKabisat(x): 
    if kabisatInput % 400 == 0:
        return True
    elif kabisatInput % 100 == 0:
        return False
    elif kabisatInput % 4 == 0: 
        return True

if thKabisat(kabisatInput):
    print(f'input tahun: {kabisatInput} \nHasil: TAHUN KABISAT')
else:
    print(f'input tahun: {kabisatInput} \nHasil: BUKAN TAHUN KABISAT')