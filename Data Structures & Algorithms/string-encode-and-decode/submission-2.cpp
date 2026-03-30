class Solution {
public:
    // 4#neet4#code4#love3#you
    string encode(vector<string>& strs) {
        string result = "";
        for (auto& str: strs) {
            result += to_string(str.size());
            result += "#";
            result += str;
        }
        return result;
    }

    vector<string> decode(string s) {
        vector<string> result;
        if (s.size() == 0) {
            return result;
        }
        int i = 0;
        while(i < s.size()) {
            int len = 0;
            while (s[i] != '#') {
                len = len * 10 + (s[i] - '0');
                i++;
            }
            if (s[i] == '#') {
                i++;
            }
            string str = "";
            for (int j = 0; j < len; j++) {
                str += s[i];
                i++;

            }
            result.push_back(str);
        }
        return result;
    }
};
