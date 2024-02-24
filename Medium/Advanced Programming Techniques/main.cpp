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

int main() {

  // vector<int> myarray = read_from_file();
  
  // for (auto item : myarray) {
  //   string Fizz_buzz = "";
  //   if (item % 3 == 0) {
  //     Fizz_buzz += "Fizz";
  //     cout << item << Fizz_buzz << endl;
  //   }
  //   if (item % 5 == 0) {
  //     Fizz_buzz += "Buzz";
  //     cout << item << Fizz_buzz << endl;
  //   }
  //   if (item % 3 != 0 && item % 5 != 0){
  //       cout << item << item << endl;
  //   }
  // }
  return 0;
}

string output(){
   vector<int> myarray = read_from_file();
}