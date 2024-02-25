#include <fstream>
#include <iostream>
#include <vector>
using namespace std;

std::vector<int> read_from_file(){
  vector<int> myarray;
  int x;
  ifstream read;

  read.open("input.txt");
  while (read >> x) {
    myarray.push_back(x);
  }

  myarray.erase(myarray.begin());

  return myarray;
}

string check_number(int the_number){
  
    string Fizz_buzz = "";
    if (the_number % 3 == 0){
      Fizz_buzz += "Fizz";
      }
    if(the_number % 5 == 0){
      Fizz_buzz += "Buzz";
      }
    if (the_number % 3 != 0 && the_number % 5 != 0){
      Fizz_buzz += to_string(the_number);
      }
      return Fizz_buzz;
    }


void print_result(){
  vector<int> number_list = read_from_file();
  for (auto number: number_list){
    cout << number << " " << check_number(number) << endl;
  }
} 

int main() {
  print_result();
  return 0;
}