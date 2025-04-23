with open('titanic.txt', 'r') as file:
    file=file.read()
    print(file)
with open('titanic.txt', 'a') as file:
    file.write("titanic tragically sunk after striking an iceberg on its maiden voyage,taking the lives of over 1500 people.Titanic was the largest ship afloat upon entering service and the second of three Olympic-class ocean liners built for White Star Line. The ship was built by the Harland and Wolff shipbuilding company in Belfast. Thomas Andrews Jr., the chief naval architect of the shipyard, died in the disaster. Titanic was under the command of Captain Edward John Smith, who went down with the ship. J. Bruce Ismay, White Star Line's chairman, managed to get in a lifeboat and survived.")
file.close()
try:
    with open('titanic.txt', 'r') as file:
        file=file.read()
        print(file)
except FileNotFoundError:
        print(input('Enter the file name your are looking for:' ));

