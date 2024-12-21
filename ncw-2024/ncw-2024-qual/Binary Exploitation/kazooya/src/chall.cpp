#include <iostream>
#include <string>
#include <vector>
#include <string.h>
#include <cstdint>
#include <cstdio>

#define STR_SZ 0x50

using namespace std;

class Animal{
	public:
		Animal():name(NULL), weight(0){}

		Animal(string name, uint64_t weight, string msg){
			this->name = new char[STR_SZ];
			strcpy(this->name, name.c_str());
			this->weight = weight;
			this->sound = msg;
		}

		virtual uint64_t getId(){
			return id;
		}

		string getType(){
			return type;
		}

		char* getName(){
			return name;
		}

		virtual void showInfo(){
			cout << "Name: " << name << endl;
			cout << "Weight: " << weight << endl;
		}
		
		virtual void makeSound(){
			cout << type << "makes a sound << " << sound << " >>" << endl;
		}

		virtual ~Animal(){
			type.clear();
			sound.clear();
			delete[] name;
		}

	protected:
		uint64_t id;
		char *name;
		uint64_t weight;
		string type;
		string sound;
};

class Monke :public Animal{
	public:
		Monke():age(0){}
		Monke(string name, uint64_t weight, string msg, uint64_t age){
			this->type = "Monke";
			this->name = new char[STR_SZ];
			strcpy(this->name, name.c_str());
			this->weight = weight;
			this->sound = msg;
			this->age = age;
			this->id = (classId)++;
		}

		void showInfo(){
			cout << "Monke ID: " << id << endl;
			cout << "Monke name: " << name << endl;
			cout << "Monke age: " << age << endl;
			cout << "Monke weight: " << weight << endl;
		}

		~Monke(){
			id--;
			age = 0;
		}

	private:
		static uint64_t classId;
		uint64_t age;
};

class Cat :public Animal{
	public:
		Cat():furs(0){}

		Cat(string name, uint64_t weight, string msg, uint64_t furs){
			this->type = "Cat";
			this->name = new char[STR_SZ];
			strcpy(this->name, name.c_str());
			this->weight = weight;
			this->sound = msg;
			this->furs = furs;
			this->id = (classId)++;
		}
		
		~Cat(){
			id--;
			furs = 0;
		}

		void showInfo(){
			cout << "Cat ID: " << id <<endl;
			cout << "Cat name: " << name <<endl;
			cout << "Cat weight: " << weight <<endl;
			cout << "Cat furcount: " << furs <<endl;
		}

	private:
		static uint64_t classId;
		uint64_t furs;
};

vector<Animal*> animalList;
uint64_t Monke::classId = 0;
uint64_t Cat::classId = 0;

void animaltypes(){
	cout << "We currently only have 2 animal types" << endl;
	cout << "1. Monke" << endl;
	cout << "2. Cat" << endl;
}

void addMenu(){
	unsigned int choice, weight;
	string name, sound;
	animaltypes();
	cout << ">> ";
	cin >> choice;
	cin.ignore();

	cout << "Name: ";
	getline(cin, name);
	cout << "Sound: ";
	cin >> sound;
	cout << "Weight: ";
	cin >> weight;

	switch(choice){
		case 1:
			uint64_t age;
			cout << "Age: ";
			cin >> age;
			animalList.push_back(new Monke(name, weight, sound, age));
			break;
		case 2:
			uint64_t furs;
			cout << "How many furs(num): ";
			cin >> furs;
			animalList.push_back(new Cat(name, weight, sound, furs));
			break;
		default: cout << "No such animal"; break;
	}
}


void listAnimal(){
	cout << "=========== Monke =============" << endl;
    for (auto animal : animalList) {
		if(animal->getType() == "Monke"){
			animal->showInfo();
			cout << "===============================" << endl;
		}
    }
	cout << ">>>=========================<<<" << endl;

	cout << "===========  Cat  =============" << endl;
    for (auto animal : animalList) {
		if(animal->getType() == "Cat"){
			animal->showInfo();
			cout << "===============================" << endl;
		}
	}
}

void hearSound(){
	uint64_t choice;
	string type;
	uint64_t id;
	listAnimal();
	cout << "What kind of animal would you like to hear?" <<endl;
	cout << "1. Monke" <<endl;
	cout << "2. Cat" <<endl;
	cout << ">> ";
	cin >> choice;
	cout << "Which id?" <<endl;
	cout << ">> ";
	cin >> id;
	switch(choice){
		case 1:
			for(auto animal: animalList){
				if(animal->getType() == "Monke" && animal->getId() == id){
					animal->makeSound();
				}
			}
			break;
		case 2:
			for(auto animal: animalList){
				if(animal->getType() == "Cat" && animal->getId() == id){
					animal->makeSound();
				}
			}
			break;
		default: cout << "No such animal" << endl;
	}
}

void printMenu(){
	cout << "Welcome to KaZooYa" << endl;
	cout << "The Online Zoo Management Tool" << endl;
	cout << "You, as the managing director of KaZooya are tasked to oversee the Animals in the Zoo" << endl;
	cout << "Now, what would you like to do?" << endl;
	cout << "1. Add new animal" << endl;
	cout << "2. Show animal list" << endl;
	cout << "3. Hear animal sound" << endl;
	cout << "4. Done for the day" << endl;
}

void init(){
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

int main(void){
	init();
	unsigned int choice = 0;
	cout << "[LEAK]: " << (void*)puts << endl;
	cout << "[LEAK]: " << (void*)malloc(0x10) << endl;
	for(;;){
		printMenu();
		cout << ">> ";
		cin >> choice;
		switch(choice){
			case 1: addMenu(); break;
			case 2:
				if(animalList.empty()){
					cout << "... The zoo is empty" << endl;
				}else{
					listAnimal();
				}
				break;
			case 3:
				if(animalList.empty()){
					cout << "... The zoo is empty" << endl;
				}else{
					hearSound();
				}
				break;
			case 4: exit(1); break;
			default: cout << "Did you mash your keyboard?" << endl;
		}
	}
	return 0;
}