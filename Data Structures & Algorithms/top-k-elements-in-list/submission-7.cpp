class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, int> freq;
        for (auto& num: nums) {
            freq[num]++;
        }
        vector<int> result;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> h;
        for (auto& item: freq) {
            h.push({item.second, item.first});
            if (h.size() > k) {
                h.pop();
            }
        }
        while(!h.empty()) {
            result.push_back(h.top().second);
            h.pop();
        }
        return result;
    }
};
