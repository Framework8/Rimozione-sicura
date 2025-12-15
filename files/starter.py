import os
import shutil
import random
from cryptography.fernet import Fernet
from colorama import Fore, Style, init

init(autoreset=False)
print(Fore.LIGHTYELLOW_EX, end='')


def menu():
    print("\n=== MENU ===")
    print("1. Eliminare in modo sicuro un file")
    print("2. Eliminare in modo sicuro una cartella di file")
    print("3. Pulisci schermo")
    print("4. Elimina la cartella temporanea (se presente)")
    print("5. Esci")
    
    
    while True:
        scelta = input("Scegli un'opzione (1-5): ")
        if scelta in ['1', '2', '3', '4', '5']:
            return scelta
        os.system("clear")
        print("Scelta non valida. Riprova.\n")
        print("\n=== MENU ===")
        print("1. Eliminare in modo sicuro un file")
        print("2. Eliminare in modo sicuro una cartella di file")
        print("3. Pulisci schermo")
        print("4. Elimina la cartella temporanea (se presente)")
        print("5. Esci")


def chiave():
    x=Fernet.generate_key()
    return x

def critta_cartella(cartella):
    for root, dirs, files in os.walk(cartella):
        for file in files:
            filepath = os.path.join(root, file)
            critta_file(filepath)

def critta_file(filepath):
    try:
        # Leggi il contenuto originale
        with open(filepath, 'rb') as file:
            original_data = file.read()
            
        #generazione chiave diversa ogni volta
        f=Fernet(chiave())

        # Critta i dati
        encrypted_data = f.encrypt(original_data)
        
        # Sovrascrivi il file con i dati crittati
        with open(filepath, 'wb') as file:
            file.write(encrypted_data)
            
        print(f"File crittato: {filepath}")
        
    except Exception as e:
        print(f"Errore durante la crittazione di {filepath}: {str(e)}")

def new_path_file(file):
    if not os.path.exists("./temporanea"):
        os.mkdir("temporanea")
    shutil.move(file, "./temporanea/")
    documento=os.path.basename(file)
    os.rename(f"./temporanea/{documento}", "./temporanea/file.txt")

def new_path_cartella(cartella):
    if not os.path.exists("./temporanea"):
        os.mkdir("temporanea")
    for file in os.listdir(cartella):
        percorso_e_nome=os.path.join(cartella, file)
        documento=os.path.basename(file)
        shutil.move(percorso_e_nome, "./temporanea")
        numero=random.randint(1, 10000)
        os.rename(f"./temporanea/{documento}", f"./temporanea/file{numero}.txt")
    
def elimina_temporanea():
    if os.path.exists("./temporanea"):
        shutil.rmtree("./temporanea")
    else:
        print("\nLa cartella non esiste o è già stata eliminata\n")

if __name__ == "__main__":
    while True:
        scelta=menu()

        if scelta=='1':
            file=str(input("Inserisci il percorso del file:\t"))
            if not os.path.exists(file):
                print(Fore.RED + "Il percorso non esiste. Riprova" + Style.RESET_ALL)
                print(Fore.LIGHTYELLOW_EX)
            else:
                critta_file(file)
                new_path_file(file)
                os.system("./elimina_file")
                shutil.rmtree("./temporanea")

        elif scelta=='2':
            cartella=str(input("Inserisci il percorso della cartella:\t"))
            if not os.path.exists(cartella):
                print(Fore.RED + "Il percorso non esiste. Riprova" + Style.RESET_ALL)
                print(Fore.LIGHTYELLOW_EX)
            else:
                critta_cartella(cartella)
                new_path_cartella(cartella)
                os.system("./elimina_cartella")
        elif scelta=='3':
            os.system("clear")
        elif scelta=='4':
            os.system("clear")
            elimina_temporanea()
        else:
            print("Uscito")
            break
