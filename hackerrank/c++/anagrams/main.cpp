#include <iostream>
#include <map>
#include <numeric>

using namespace std;

/* Anagrams (strings)
 * Given two strings, `a` and `b`, that may or may not be the same length,
 * determine the minimum number of character deletions required to make
 * `a` and `b` anagrams. Any characters can be deleted from either of the strings.
 */

// count the occurrence of char in a string, using map
map<char, int > counter(string a){

    map<char , int > countChar;

    for ( int i=0; i< a.size(); ++i )
    {
        ++countChar[a[i]] ;
    }
    return countChar;
}

// find the intersection of two maps
template <typename Key, typename Value>
std::map<Key,std::pair<Value,Value> >
merge_maps( std::map<Key,Value> const & lhs, std::map<Key,Value> const & rhs )
{
    //typedef typename std::map<Key,Value>::const_iterator input_iterator;
    std::map<Key, std::pair<Value,Value> > result;
    for (auto it1 = lhs.begin(), it2 = rhs.begin(),
                  end1 = lhs.end(), end2 = rhs.end();
          it1 != end1 && it2 != end2; )
    {
        if ( it1->first == it2->first )
        {
            result[it1->first] = std::make_pair( it1->second, it2->second );
            ++it1; ++it2;
        }
        else
        {
            if ( it1->first < it2->first )
                ++it1;
            else
                ++it2;
        }
    }
    return result;
}

// find differences of two maps, return all elements of `a` that are not in `b`
map<char, int> FindDiff(map<char, int> a, map<char, int> b){
    map<char, int> c;

    /*
    std::set_difference(
            a.begin(), a.end(),
            b.begin(), b.end(),
            std::inserter(c, c.begin()) );
    //std::back_inserter needs container to support `push_back` function
    //map container does not support `push_back`
     */

    for(auto it : a){
        if(b.find(it.first) == b.end()) c.insert(it);
    }

    return c;
}

int anagrams(string a, string b) {
    int result = 0;
    map<char, int> countA;
    map<char, int> countB;
    map<char, pair<int, int> > common;
    map<char, int> uncommonA;
    map<char, int> uncommonB;

    countA = counter(a);
    countB = counter(b);
    common = merge_maps(countA, countB);
    uncommonA = FindDiff(countA, countB);
    uncommonB = FindDiff(countB, countA);

    // add all values in uncommonA
    result = std::accumulate(std::begin(uncommonA), std::end(uncommonA), 0,
                                 [](const int previous,
                                    const std::pair<char, int> &p) { return previous + p.second; });

    // add all values in uncommonB
    result += std::accumulate(std::begin(uncommonB), std::end(uncommonB), 0,
                                 [](const int previous,
                                    const std::pair<char, int> &p) { return previous + p.second; });

    int num = 0;
    for (auto it : common) {

        pair<int, int> temp = it.second;
        num += abs(temp.first - temp.second);
    }
    result += num;

    return result;
}

int main(){
    string a = "fcrxzwscanmligyxyvym";
    string b = "jxwtrhvujlmrpdoqbisbwhmgpmeoke"; // right answer: 30

    cout << "The number of characters needs to be deleted is " << anagrams(a, b) << endl;

    /*
    // debug section
    map<char, int> temp = counter(a);
    map<char, int> temp2 = counter(b);
    map<char, pair<int, int> > common = merge_maps(temp, temp2);
    map<char, int> temp3 = FindDiff(temp, temp2);
    map<char, int> temp4 = FindDiff(temp2, temp);
    for(auto it = common.cbegin(); it != common.cend(); ++it)
    {
        std::cout << it->first << " " << it->second.first << " " << it->second.second<< "\n";
        //std::cout << it->first << " " << it->second<< "\n";
    }
     */


}


/*
 * A nice answer:
 *
 int number_needed(string a, string b) {
    auto count = 0;
    vector<int> freq(26, 0);
    for (auto c : a) { ++freq[c - 'a']; }
    for (auto c : b) { --freq[c - 'a']; }
    for (auto val : freq) { count += abs(val); }
    return count;
 }
 */