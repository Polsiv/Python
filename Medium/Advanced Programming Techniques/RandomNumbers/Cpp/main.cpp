#include <random>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <chrono>

using namespace std;
using namespace std::chrono;

vector<int> rng(int low_limit, int high_limit, int max_numbers){
    vector<int> num_list;
    random_device dev;
    uniform_int_distribution<mt19937::result_type> dist(low_limit, high_limit);
    mt19937 rng(dev());
    for (int i = 0; i < max_numbers; i++)
        num_list.push_back(dist(rng));
    return num_list;
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

void write_data(string filename, vector<int> numbers){

    fstream file (filename, ios::out);

    if (file.is_open()){
        for (int number: numbers){

            file << number << endl;
        }
    } else {
        cout << "couldnt open file." << endl;
    }
}

vector<int> read_data(string file_name){

    vector<int> numbers;
    fstream file (file_name, ios::in);
    
    if (file.is_open()){
        int number;
        while(file >> number){
            numbers.push_back(number);
        }
    } else {
        cout << "Couldn't open file.";
    }
    
    return numbers;
}

void write_sorted_data(string filename, vector<int> numbers){
    fstream file (filename,  ios::out);
    if (file.is_open()){
        for (int i: numbers){
            file << i << endl;
        }
    } else {
        cout << "couldnt open file." << endl;
    }
}

int main(){
    int min_limit = 0;
    int sup_limit = 256; 
    int max_numbers = 1048576;
    vector<int> numbers = rng(min_limit, sup_limit, max_numbers);
    write_data("input.txt", numbers);
    vector<int> numbers_from_file = read_data("input.txt");

    auto start = high_resolution_clock::now();
    std::vector<int> sorted = countsort(numbers_from_file, *std::max_element(numbers_from_file.begin(), numbers_from_file.end()));
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<milliseconds>(stop - start);

    write_sorted_data("sortednumbers.txt", sorted);
    cout << "time elapsed: " << duration.count() << " milliseconds" << endl;
    return 0;
  
}





