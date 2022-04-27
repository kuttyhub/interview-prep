import java.util.Arrays;
import java.util.Scanner;

public class CheckAnagram {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the first string: ");
        String first = sc.next();
        System.out.print("Enter the second string: ");
        String second = sc.next();
        System.out.println(usingGeneric(first, second));
        System.out.println(usingMap(first, second));

        sc.close();

    }

    public static boolean usingGeneric(String s1, String s2) {
        if (s1.length() == s2.length()) {
            char[] s1Array = s1.toCharArray();
            char[] s2Array = s2.toCharArray();
            Arrays.sort(s1Array);
            Arrays.sort(s2Array);
            return Arrays.equals(s1Array, s2Array);
        }
        return false;
    }

    public static boolean usingMap(String s1, String s2) {
        if (s1.length() == s2.length()) {
            int[] letters = new int[256];
            for (int i = 0; i < s1.length(); i++) {
                letters[s1.charAt(i)]++;
            }
            for (int i = 0; i < s2.length(); i++) {
                letters[s2.charAt(i)]--;
            }
            for (int i = 0; i < letters.length; i++) {
                if (letters[i] != 0) {
                    return false;
                }
            }
            return true;
        }
        return false;
    }
}
