/* Anagrams (strings)

        Given two strings, `a` and `b`, that may or may not be the same length,
        determine the minimum number of character deletions required to make
        `a` and `b` anagrams. Any characters can be deleted from either
        of the strings.

*/

public class Anagrams {

    private static int numberNeeded(String a, String b){
        int[] feq = new int[26];
        int ascii = (int) 'a';

        for(int i = 0; i < a.length(); i++ ){
            int asciiA = (int) a.charAt(i);
            ++feq[asciiA - ascii];
        }

        for(int j = 0; j < b.length(); j++){
            int asciiB = (int) b.charAt(j);
            --feq[asciiB - ascii];
        }

        int sum = 0;
        for(int k = 0; k < 26; k++ ){
            int temp = Math.abs(feq[k]);
            sum += temp;
        }
        //IntStream.of(feq).sum(); //this line won't get abs value

        return sum;
    }

    public static void main(String[] args){
        String a = "abdc";
        String b = "abddf";

        int res = numberNeeded(a, b);

        System.out.println("The number of characters needs to be deleted is " + res);
    }
}
