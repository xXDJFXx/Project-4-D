                        #FINAL MAIN.PY CODE:
import credit

print('Enter a credit card number')
number = input()

#credit.isValid(number)

#--------------------------------------------------------
#COMMENT OUT THE CODE ABOVE AND TEST OUT YOUR INDIVIDUAL FUNCTIONS BELOW. AFTER YOU TEST THEM, COMMENT THEM OUT:
print(credit.getsize(number))
print(credit.getPrefix(number,(4)))
print(credit.prefixMatched(number,4))
print(credit.getdigit(number))
print(credit.getSumEven(number))
print(credit.getSumofOddPlace(number))
print(credit.isvalid(number))