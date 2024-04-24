#include <random>
#include <iostream>

using namespace std;

int generate_random(){

    static default_random_engine rng;
    uniform_int_distribution<int> dist(0, 16383);
    return dist(rng);

};
 
int main(){
    for (int i = 0; i < 1000; i++){
        cout << generate_random() << endl;
    }
}