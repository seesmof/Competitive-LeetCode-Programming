#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n;
    cin>>n;

    for(int i = 0; i < n; ++i){
        int p;
        cin >> p;
        std::vector <int>  arr(p);
        
        for(int j = 0; j < p; ++j){
            cin >> arr[j];
        }
        int s = 0;
        bool need_sort = 0;
        std::vector <int> vec (p);
        vec.insert(vec.begin(), arr.begin(), arr.end());
        sort(vec.begin(), vec.end());
        for(int i = 0; i < vec.size(); ++i){
            if(vec[i] != arr[i]){
                need_sort = 1;
                break;
            }
        }
        for(int j = 0; j < p; ++j){
            for(int k = 0; k <= p; ++k){
                int f = 0;
                std::vector <int> new_arr (k+1);
                for(int index = j; index <= j+k && j + k < p; ++index){

                    new_arr[f++] = arr[index];
                }
                if(k != 0 && need_sort){
                    sort(new_arr.begin(), new_arr.end());
                }

                for(int index = j, index2 = 0; index <= j+k && j + k < p; ++index, index2++){
                    if(new_arr[index2] == arr[index]){
                        ++s;
                    }
                }

            }
        }

        cout << s << "\n";
    }
}