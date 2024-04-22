#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <set>

using namespace std;

int main() {
    int n;
    int answer = 0;
    set<int> user_set;  
    unordered_map<int,int> user_map;    

    cin >> n;

    vector<int> arr(n + 2); 
    vector<vector<int>> index_arr(n + 2);
    vector<bool> visited(n + 2, false);


    for(int i=1; i <= n; i++){
        cin >> arr[i];
        user_set.insert(arr[i]);
    }

    int idx = 0;
    for(auto elem : user_set){
        user_map.insert({elem, idx++});
    }

    
    for(int i=1; i <= n; i++){
        index_arr[user_map[arr[i]]].push_back(i);
    }

    int result = 0;
    int user_set_size = user_set.size();


    for(int i= user_set_size - 1; i >= 0; i--){ 

        for(int j= 0; j < index_arr[i].size(); j++){
            
            int cur_idx = index_arr[i][j];
            if(!visited[cur_idx -1] && !visited[cur_idx + 1]){ 
                result++;
            }
            else if(!visited[cur_idx - 1]){
            }
            else if(!visited[cur_idx  + 1]){   
            }
            else{ 
                result--;
            }
            visited[cur_idx] = true;
        }
        
       
        answer= max(answer, result);
    }

    cout << answer << '\n';
    return 0;
}