from Types.Result import ResultDef

listProlog = []
listForCompare = []

class PrologDef():
    def __init__(self, nomecorso, docente, numstudenti, seguitoda, numore, lab, numslot, slotdur, type, mysql, fullname, link):
        self.nomecorso = nomecorso  #nome simbolico del corso
        self.docente = docente  #cognome del docente
        self.numstudenti = numstudenti  #intero che indica la stima degli studenti che seguiranno il corso
        self.seguitoda = seguitoda  #lista dei corsi che seguono il corso
        self.numore = numore  #numero di ore settimanali di corso, se ha .5 ha una mezz'ora in più
        self.lab = lab  #aula in cui si svolge il corso
        self.numslot = numslot  #numero di lezioni che vengono tenute in una settimana
        self.slotdur = slotdur  #durata delle singole lezioni
        self.type = type  #può assumere i valori [year1, year2, fixed, lunch, turni, noturni, exceptional]
        self.mysql = mysql  #campo che serve per l'esportazione in Google Calendar
        self.fullname = fullname  #nome di output del corso
        self.link = link  #link al sito web del corso


def addToList(corsoString):
    temp0 = str(corsoString).split(",")
    temp1 = None
    temp2 = None
    lastParenthesis = 0
    secondParenthesis = 0
    if str(temp0[3]).startswith("[["):
        temp1 = str(temp0[3])
        for i in range(4,20):  #messo un range di sicurezza provvisorio. Si può sostituire con un ciclo while
            if str(temp0[i]).endswith("]]"):
                temp1 = temp1 + str(temp0[i])
                lastParenthesis = i
                break
            else:
                temp1 = temp1 + str(temp0[i])
    if str(temp0[lastParenthesis+4]).startswith("["):
        temp2 = str(temp0[lastParenthesis+4])
        if temp2.endswith("]"):
            secondParenthesis = lastParenthesis + 4
        else:
            for j in range(lastParenthesis + 5, lastParenthesis + 8):
                if str(temp0[j]).endswith("]"):
                    temp2 = temp2 + "/" + str(temp0[j])
                    secondParenthesis = j
                    break
                else:
                    temp2 = temp2 + "/" + str(temp0[j])

    nomecorso = temp0[0]
    docente = temp0[1]
    numstudenti = temp0[2]
    seguitoda = temp1
    numore = temp0[lastParenthesis + 1]
    lab = temp0[lastParenthesis + 2]
    numslot = temp0[lastParenthesis + 3]
    slotdur = temp2
    type = temp0[secondParenthesis + 1]
    mysql = temp0[secondParenthesis + 2]
    fullname = temp0[secondParenthesis + 3].replace('"', '')
    link = temp0[secondParenthesis + 4].replace('"','').split(").", 1)[0]


    listProlog.append(PrologDef(nomecorso, docente, numstudenti, seguitoda, numore, lab, numslot, slotdur, type, mysql, fullname, link))

    listForCompare.append(ResultDef(str(nomecorso), str(docente).lower(), "", "", "", "", ""))

def getPrologList():
    listProlog.sort(key=lambda x: x.fullname, reverse=False)
    return listProlog

def getListforCompare():
    return listForCompare