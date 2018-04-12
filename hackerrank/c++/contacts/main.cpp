/* Contacts (Tries)

Tries: a tree data structure that stores characters as nodes, and
check weather the path forms a word.

The contacts application must perform two types of operations:

1. add name, where `name` is a string denoting a contact name.
This must store `name` as a new contact in the application.
2. find partial, where `partial` is a string denoting a partial name
        to search the application for. It must count the number of contacts
        starting with `partial` and print the count on a new line.

*/

#include <iostream>
#include <map>
#include <fstream>
#include <vector>

using namespace std;

struct TrieNode {
    int size = 0;
    map<char, TrieNode*> children;
} node;

void add(TrieNode* root, string name){
    // check if a char is already added in the trie
    for(auto ch : name){
        if( root->children.find(ch) != root->children.end()){
            root = root->children.at(ch);
            root->size++;
        }
    }

    // append new nodes for the remaining char, if any
    for(auto ch : name) {
        //cout << ch << endl;
        root->children[ch] = new TrieNode;
        root = root->children.at(ch);
        root->size++;
    }
}

int find(TrieNode* root, string partial) {
    TrieNode* node = root;
    for(auto ch : partial){
        if(node->children.find(ch) == node->children.end()){
            //cout << "inside if" << endl;
            return 0;
        }
        else{
            node = node->children.at(ch);
        }
    }
    return node->size;
}

int main() {

    // Current version did not pass all tests
    // TODO: try to read in input3.txt and check the output
    string Filename = "input3.txt";
    ifstream input(Filename);         // Open the file
    if(!input){
        cerr <<"File loading error";
        exit(1);
    }
    string line;                      // Temp variable
    vector<string> lines;             // Vector for holding all lines in the file
    while (getline(input, line))      // Read lines as long as the file is
    {
        lines.push_back(line);        // Save the line in the vector
    }
    input.close();
    cout << lines[0] << endl;
    /*
    int n;
    n = stoi(lines[0]);
    cout << n << endl;
    */

    //cout << lines[0:10] << endl; // the python-style slice does not work, try programming iterator
    // see this website: http://www.cplusplus.com/forum/general/135833/
    /*
    for(int a0 = 0; a0 < n; a0++){
        string op;
        string contact;
        op =

        if (op == "add") {
            add(&node, contact);
        }
        if (op == "find") {
            cout << find(&node, contact) << endl;
        }

    }
    */



    return 0;
}