def computegrade(score):
    if(score >= 0.9 and score <= 1.0):
     grade ="Sobresaliente"
    elif (score>= 0.8 and score <= 0.9):
     grade = "Notable"
    elif(score >= 0.7 and score <= 0.8):
      grade = "Ben"
    elif(score >= 0.6 and score <= 0.7):
      grade = "Suficiente"
    elif(score >= 0 and score <= 0.6):
      grade = "Insuficiente"
    else:
      grade="Calificacion no valida"
    return grade

try:
    score=float(input("Ingrese la calificacion (0.01-1.00):"))
    grade=computegrade(score)
    print("El grado de su calificación es:", grade)
except:
    print("Error, debe ingresar un valor númerico")