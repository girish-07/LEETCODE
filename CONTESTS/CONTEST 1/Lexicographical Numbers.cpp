class Solution {
public:
    vector<int> lexicalOrder(int n) {
        vector<int> arr;
        for(int i=1; i<10; i++) {
            dfs(i, n, arr);
        }
        return arr;
    }
    void dfs(int cur, int n, vector<int>& arr) {
        if(cur>n) {
            return;
        }
        else {
            arr.push_back(cur);
            for(int i=0; i<10; i++) {
                dfs(cur*10+i, n, arr);
            }
        }
    }
};
