#include <iostream>
using namespace std;
int xoroperright(int arr[], int n, int beg, int end) {
  int xorsum = 0;
  for (int i = beg; i < end; i++) {
    xorsum ^= arr[i];
  }
  return xorsum;
}
int andoperleft(int arr[], int n, int beg, int end) {
  int andsum = arr[beg];
  for (int i = beg; i > end; i--) {
    andsum &= arr[i];
  }
  return andsum;
}
int xoroperleft(int arr[], int n, int beg, int end) {
  int xorsum = 0;
  for (int i = end; i > beg + 1; i--) {
    xorsum ^= arr[i];
  }
  return xorsum;
}
int andoperright(int arr[], int n, int beg, int end) {
  int andsum = arr[beg];
  for (int i = beg; i < end - 1; i++) {
    andsum &= arr[i];
  }
  return andsum;
}
int main() {
  int t;
  cin >> t;
  int ans[128];
  for (int index = 0; index < t; index++) {
    int lenarr, xorop, andop;
    int* a;
    cin >> lenarr;
    a = new int[lenarr];
    for (int i = 0; i < lenarr; i++) {
      cin >> a[i];
    }  
    int xend = lenarr - 1;
    int apointer = lenarr - 1;
    for (int xpointer = 0, xend; xend != 1; xend--) {
      cout << xoroperleft(a, lenarr, 0, xend) << andoperright(a, lenarr, lenarr - 1, xend) << endl;
    }

  }
}