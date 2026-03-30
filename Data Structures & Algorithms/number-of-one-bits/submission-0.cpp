class Solution {
public:
    int hammingWeight(uint32_t n) {
        int hamming_distance = 0;
        while (n) {
            hamming_distance += n%2;
            n /= 2;
        }
        return hamming_distance;
    }
};
