for(int j = 0; j < p; ++j){
    std::vector <int> new_arr;
    for(int k = 0; j+k < p; ++k){
        new_arr.push_back(arr[j+k]);
        sort(new_arr.begin(), new_arr.end());
        for(int index = j, index2 = 0; index <= j+k && j + k < p; ++index, index2++){
            s += (new_arr[index2] == arr[index]);
        }
    }
}