print("Hello")
def reizinajums_summa_(skaitlis1,skaitlis2): #1.uzd
    if skaitlis1 * skaitlis2 <= 1000:
        rezultats = skaitlis1 * skaitlis2
        return "reizinajums ir: " + str(rezultats)
    else:
        rezultats = skaitlis1 + skaitlis2
        return "summa ir: " + str(rezultats)
print(reizinajums_summa_(20,30))
print(reizinajums_summa_(40,30))

def drukat_summas(skaits): #2.uzd
    ieprieksejais = 0
    for esosais in range(skaits):
        summa = esosais + ieprieksejais
        print("esosais skaitlis: " + str(esosais) + "ieprieksejais:" +str(ieprieksejais) + "summa: " +str(summa))
        ieprieksejais = esosais
    return

drukat_summas(10)

def drukat_burtus(teksts): #3.uzd
    rezultats = ""
    for indekss in range(0,len(teksts),2):
        rezultats += teksts[indekss]
    return rezultats

print(drukat_burtus("Agnese"))


def nonemtBurtus(teksts, cikBurti):  #4.uzd
    jaunaisTeksts = teksts[cikBurti:]
    return jaunaisTeksts

print(nonemtBurtus("mani sauc elīna",1))

def

