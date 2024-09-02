class Solution:
    def isHappy(self, n: int) -> bool: 
        hset = set() #Cria um objeto hset que irá receber n
        while n != 1:
            hset.add(n) #Adiciona a variavel n no objeto hset
            n = sum([int(i) ** 2 for i in str(n)]) #Soma os quadrados dos valores de cada caractere da string (n) armazenados na variavel (i)
            if n in hset: 
                return False
        else:
            return True
    
