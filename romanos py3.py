class Solution:

  def romanToInt(s: str) -> int:
    ans = 0 #variavel que acumula o resultado
    roman = { 'I': 1,
              'V': 5,
              'X': 10,
              'L': 50,
              'C': 100,
              'D': 500,
              'M': 1000} #Cria um objeto que armazena os respectivos valores de cada caractere de numero romano 

    for a, b in zip(s, s[1:]): #Separa os caracteres de S em pares
      if roman[a] < roman[b]: #Checa se o valor do primeiro caractere é menor que o do segundo
        ans -= roman[a] #Verdadeiro: subtrai o valor de a ao resultado final
      else:
        ans += roman[a] #Falso: adiciona o valor de A ao resultado final

    return ans + roman[s[-1]] #Adiciona o valor do ultimo caractere romano (s) ao resultado final (ans)
  
  print(romanToInt(input("Digite um numero romano: "))) #Input