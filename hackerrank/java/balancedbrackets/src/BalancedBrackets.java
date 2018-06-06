import java.util.Scanner;
import java.util.Stack;

public class BalancedBrackets {
    private static boolean isBalanced(String expression) {
        Stack<Character> s = new Stack<>();
        for (int i = 0; i < expression.length(); i++) {
            char ch = expression.charAt(i);
            switch (ch) {
                case '{':
                    s.push(ch);
                    break;
                case '[':
                    s.push(ch);
                    break;
                case '(':
                    s.push(ch);
                    break;
                default:
                    if (s.empty() || !isPair(ch, s.pop())) return false;
            }
        }
        return s.empty();
    }

    private static boolean isPair(char a, char b){
        int asciiA = (int) a;
        //System.out.println(asciiA);
        int asciiB = (int) b;
        //System.out.println(asciiB);
        if((asciiA == 123 && asciiB == 125) || (asciiA == 125 && asciiB == 123))
            return true;
        else if((asciiA == 91 && asciiB == 93) || (asciiA == 93 && asciiB == 91))
            return true;
        else
            return (asciiA == 41 && asciiB == 40) || (asciiA == 40 && asciiB == 41);
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for (int a0 = 0; a0 < t; a0++) {
            String expression = in.next();
            System.out.println( (isBalanced(expression)) ? "YES" : "NO" );
        }
    }
}
