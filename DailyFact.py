from bs4 import BeautifulSoup
import requests
url = 'https://www.beagreatteacher.com/daily-fun-fact/'
headers = {'User-Agent': 'Mozilla/5.0'}
request = requests.get(url, headers=headers).text

formatirane = BeautifulSoup(request, 'html.parser')

joke_Izrechenie = formatirane.main.p.next_sibling.next_sibling
fact_Izrechenie = formatirane.main.p.next_sibling.next_sibling.next_sibling.next_sibling
question_Izrechenie = formatirane.main.p.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling

#joke_Bez_Tag = joke_Izrechenie.string.extract()
joke_Bez_Tag = joke_Izrechenie.string
fact_Bez_Tag = fact_Izrechenie.string
question_Bez_Tag = question_Izrechenie.string

# Testing
#print(joke_Izrechenie)
#print(fact_Izrechenie)
#print(question_Izrechenie)


#--v--Показва основната информация и опции за запазване.
print("\n|======= Joke of the day =======| \n \n", joke_Bez_Tag, "\n \n")
print("|======= Fact of the day =======| \n \n", fact_Bez_Tag, "\n \n")
print("|======= Question of the day =======| \n \n", question_Bez_Tag, "\n \n")
print("Choose to save: \n1) Joke of the day \n2) Fact of the day \n3) Both \n4) Exit")

#--v--Създава нов файл, ако липсва такъв.
def joke_File_Creation():
    with open('Favorite_Jokes.txt', 'x') as f:
        f.write(joke_Bez_Tag)
        print('The file "Favorite_Jokes" was created in the same directory.')
        
def fact_File_Creation():
    with open('Favorite_Facts.txt', 'x') as f:
        f.write(fact_Bez_Tag)
        print('The file "Favorite_Facts" was created in the same directory.')

#--v--Добавя изреченията на нов ред.
def joke_File_Appending():
    with open('Favorite_Jokes.txt', 'a') as f:
        f.write("\n<==============================================>\n")
        f.write(joke_Bez_Tag)
        print('The joke has been added to favorites.')

def fact_File_Appending():
    with open('Favorite_Facts.txt', 'a') as f:
        f.write("\n<==============================================>\n")
        f.write(fact_Bez_Tag)
        print('The fact has been added to favorites.')

izbor_Opciq = int(input('Option: '))

#--v--Изпълнява зададена опция. При липса на файл, създава нов, в противен случай добавя изречението.
if izbor_Opciq == 1:
    try: 
        joke_File_Creation()
    except:
        joke_File_Appending()        
    
elif izbor_Opciq == 2:
    try: 
        fact_File_Creation()
    except:
        fact_File_Appending()

elif izbor_Opciq == 3:
    try: 
        joke_File_Creation()
        fact_File_Creation()
    except:
        joke_File_Appending()
        fact_File_Appending()
elif izbor_Opciq == 4:
    raise SystemExit
else:
    print('Not an option!')