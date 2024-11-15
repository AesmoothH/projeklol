# class - > OBJECT
class player:
    tempCount = 0
    def __init__(self, nama, alat, danlainlain): # ini contractor
        self.nama = nama
        self.alat = alat
        self.danlain = danlainlain
    def display( self ):
        print(f"Nama Player : {self.nama}")
        print(f"Nama Alat : {self.alat}")
        print(f"Nama Danlain : {self.danlain}")
    def gantiNama( self, newNama ):
        self.nama = newNama
        
        player.tempCount += 1
        pass

class alat:
    def __init__(self, na_alat):
        self.na_alat = na_alat
    def PenggunaAlat( self ):
        return self.na_alat
class nama:
    def __init__(self, na_nama):
        self.na_nama = na_nama
    def PenggunaAlat( self ):
        return self.na_nama

        
alatKuli = alat("palu")
Kuli = alat("semen")
Kuli = alat("gerobak")

alatlayer = alat("alat 1")
alatlayer = alat("alat 2")

def main():
    newPlayer1 = player( "kiki", "palu", "gergaji" ) # yes
    print(f"Nama Player 1 : {newPlayer1.nama}")
    newPlayer1.display()
    newPlayer1.gantiNama( "kata" )
    newPlayer2 = player("kuku", "yes", "and")
    newPlayer2.display()
    
    print(f"JUmlah Objek : {player.tempCount}")

if __name__ == "__main__":
    main()