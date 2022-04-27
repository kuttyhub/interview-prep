import java.util.Scanner;

public class CheckPalindrome {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        String test = sc.next();
        System.out.println(isPalindrome(test));

        // for preventing memory leaks
        sc.close();
    }

    public static boolean isPalindrome(String s) {
        String revesedString = usingRecursion(s);
        if (s.equals(revesedString)) {
            return true;
        }
        return false;
    }

    public static String usingGenericMethod(String s) {
        String rev = "";
        for (int i = s.length() - 1; i >= 0; i--) {
            rev += s.charAt(i);
        }
        return rev;
    }

    public static String usingStringBuilder(String s) {
        StringBuilder sb = new StringBuilder(s);
        sb.reverse();
        return sb.toString();
    }

    public static String usingRecursion(String word) {
        if (word == null || word.isEmpty()) {
            return word;
        }
        return word.substring(word.length() - 1) + usingRecursion(word.substring(0, word.length() - 1));
    }
}
