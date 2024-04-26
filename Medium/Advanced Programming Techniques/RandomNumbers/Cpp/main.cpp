#include <random>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <chrono>

using namespace std;
using namespace std::chrono;

int generate_random(){

    random_device dev;
    mt19937 rng(dev());
    uniform_int_distribution<mt19937::result_type> dist(0, 16383);
    return dist(rng);
};

vector<int> countsort(vector<int>& list, int max) {
    
    std::vector<int> list_count(max + 1, 0);
    std::vector<int> list_sorted(list.size());

    for (int i : list) {
        list_count[i]++;
    }

    int total = 0;
    for (int i = 0; i < list_count.size(); ++i) {
        int count = list_count[i];
        list_count[i] = total;
        total += count;  
    }

    for (int index : list) {
        list_sorted[list_count[index]] = index;
        list_count[index]++;
    }

    return list_sorted;
}

vector<int> write_data(string filename){

    vector<int> numbers;
    fstream file (filename,  fstream::app);

    if (file.is_open()){
        for (int i = 0; i < 1048576; i++){

            int rd = generate_random();
            file << rd << endl;
            numbers.push_back(rd);
        }
    } else {
        cout << "couldnt open file." << endl;
    }
    return numbers;
}

void write_sorted_data(string filename, vector<int> numbers){

    fstream file (filename,  fstream::app);

    if (file.is_open()){

        for (int i: numbers){

            file << i << endl;
        }
    } else {
        cout << "couldnt open file." << endl;
    }
}

int main(){
    
    vector<int> numbers = write_data("unsortednumbers.txt");

    auto start = high_resolution_clock::now();
    std::vector<int> sorted = countsort(numbers, *std::max_element(numbers.begin(), numbers.end()));
    auto stop = high_resolution_clock::now();

    auto duration = duration_cast<milliseconds>(stop - start);
    write_sorted_data("sortednumbers.txt", sorted);

    cout << "time elapsed: " << duration.count() << " milliseconds" << endl;
    return 0;
  
}





