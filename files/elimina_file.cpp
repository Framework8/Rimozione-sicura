#include <iostream>
#include <fstream>
#include <filesystem>
#include <random>
#include <string>  // Aggiunto per std::getline

namespace fs = std::filesystem;

void sovrascriviFileConDatiCasuali(const std::string& percorso, int passaggi = 3) {
    std::ifstream fileInput(percorso, std::ios::binary | std::ios::ate);
    if (!fileInput) {
        throw std::runtime_error("Errore nell'apertura del file per la lettura.");
    }

    std::streamsize dimensione = fileInput.tellg();
    fileInput.close();

    std::random_device rd;
    std::mt19937 generatore(rd());
    std::uniform_int_distribution<int> distribuzione(0, 255);

    std::vector<char> buffer(4096);

    for (int pass = 0; pass < passaggi; ++pass) {
        std::ofstream fileOutput(percorso, std::ios::binary | std::ios::out | std::ios::trunc);
        if (!fileOutput) {
            throw std::runtime_error("Errore nell'apertura del file per la scrittura.");
        }

        std::streamsize scritto = 0;
        while (scritto < dimensione) {
            for (auto& c : buffer) {
                c = static_cast<char>(distribuzione(generatore));
            }
            std::streamsize daScrivere = std::min<std::streamsize>(dimensione - scritto, buffer.size());
            fileOutput.write(buffer.data(), daScrivere);
            scritto += daScrivere;
        }
        fileOutput.close();
    }
}

int main(){

    std::string percorsoFile = "./temporanea/file.txt";
        //std::cout << "Inserisci il percorso del file da eliminare in modo sicuro: ";
        //std::getline(std::cin, percorsoFile);

        if (!fs::exists(percorsoFile)) {
            std::cerr << "Il file specificato non esiste.\n";
            return 1;
        }

        try {
            sovrascriviFileConDatiCasuali(percorsoFile);
            fs::remove(percorsoFile);
            std::cout << "File sovrascritto e eliminato con successo.\n";
        } catch (const std::exception& e) {
            std::cerr << "Errore: " << e.what() << "\n";
            return 1;
        }




    return 0;
}

