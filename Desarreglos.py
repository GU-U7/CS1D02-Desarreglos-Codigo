from itertools import permutations as pt

def Desarreglos(n):

  pers = [i for i in range(65, 65+n)]
  for j in range(len(pers)):
    pers[j]=chr(pers[j])


  todas = list(pt(range(1,n+1)))

  sel=[todas[0]]

  for i in range(n):
    mans = 0
    
    """
    for j in pers:
      print(j, end='\t')
    print()"""

    if i ==0:
      for j in todas:
        mans+=1
        """
        for k in j:
          print(k, end='\t')
        print()
        """

    else: 
        
      temp=None
      for j in todas:
        sep=True
        
        for k in sel:
          for p in range(n):
            if k[p]==j[p]:
              sep=False
              break        
        
        if sep:
          mans+=1
          temp=j
          """
          for k in j:
            print(k, end='\t')
          print()
          """
          
      sel.append(temp)
    print("Mes: ",i+1,"Seleccion: ", sel[i], "Formas: ", mans, end='\n\n')

