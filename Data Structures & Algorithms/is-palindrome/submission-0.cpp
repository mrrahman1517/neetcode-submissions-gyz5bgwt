#include <iostream>
#include <string>
#include <algorithm>
#include <cctype>

class Solution {
public:
    bool isPalindrome(string s) {
        if (s.length() == 0) {
            return true;
        }
        // Remove non-alphanumeric characters
        s.erase(std::remove_if(s.begin(), s.end(), [](char c) {
            return !std::isalnum(c);
        }), s.end());

        // Convert to lowercase
        std::transform(s.begin(), s.end(), s.begin(), ::tolower);
        cout << s << endl;
        int i = 0;
        int j = s.length() - 1;
        while (i <= j) {
            if (s[i] != s[j]) {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
};
