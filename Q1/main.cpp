#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>


// Defining the generator function
int gen()
{
    static int i = 0;
    return ++i;
}

template<typename T>
void Display(const T& vec);

int main()
{
    std::vector<int> v1(100);   // Declaring a vector of size 100
    std::vector<int> v2(10);    // Declaring a vector of size

    /* Part A */
    // using std::iota
    std::iota(v1.begin(), v1.end(), 1);
    std::iota(v2.begin(), v2.end(), 1);

    std::cout << "Part A: \nv1: ";
    Display(v1);
    std::cout << "v2: ";
    Display(v2);

    /* Part B */
    v2.insert(v2.end(), v1.begin(), v1.end());

    std::cout << "Part B: \nv2: ";
    Display(v2);

    /* Part C */
    std::vector<int> odd_vec(v1.size());
    std::copy_if(v1.begin(), v1.end(), odd_vec.begin(), [](int i){return i%2!=0;});
    auto iter = std::remove(odd_vec.begin(), odd_vec.end(), 0);
    odd_vec.erase(iter, odd_vec.end());

    std::cout << "Part C: \nodd_vec: ";
    Display(odd_vec);

    /* Part D */
    std::vector<int> reverse_v1(v1.size());
    std::copy(v1.rbegin(), v1.rend(), reverse_v1.begin());
    
    std::cout << "Part D: \nreverse_v1: ";
    Display(reverse_v1);


    return 0;
}

template<typename T>
void Display(const T& vec)
{
    for(auto iter{vec.begin()}; iter != vec.end(); ++iter)
        std::cout << *iter << " ";
    std::cout << std::endl;
}