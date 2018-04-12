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

import java.util.*;


public class Contacts {

    static class TrieNode {
        int size = 0;
        HashMap<Character, TrieNode> children = new HashMap<>();

    }
    /*
    static class Trie {

        TrieNode root = new TrieNode();

    }
    */

    private static void add(TrieNode root, String str) {
        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);
            root.children.putIfAbsent(ch, new TrieNode());
            root = root.children.get(ch);
            root.size++;
        }
        //System.out.println(root.children); // for debug
    }

    private static int find(TrieNode root, String partial) {
        TrieNode node = root;
        for(int i = 0; i < partial.length(); i++) {
            char ch = partial.charAt(i);
            node = node.children.get(ch);
            if (node == null) {
                return 0;
            }
        }
        //System.out.println(node.size); // for debug
        return node.size;
    }

    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        TrieNode node = new TrieNode();
        for(int a0 = 0; a0 < n; a0++){
            String op = in.next();
            String contact = in.next();
            if(op.equals("add")){
                add(node, contact);
            }else if(op.equals("find")){
                System.out.println(find(node, contact));
            }
        }

    }
}

