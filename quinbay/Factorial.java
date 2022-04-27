import java.util.Scanner;

public class Factorial {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int n = sc.nextInt();

        System.out.println(usingGeneric(n));
        System.out.println(usingRecursion(n));

        sc.close();
    }

    public static int usingRecursion(int n) {
        if (n == 1) {
            return 1;
        }
        return n * usingRecursion(n - 1);
    }

    public static int usingGeneric(int n) {
        int fact = 1;
        for (int i = 1; i <= n; i++) {
            fact *= i;
        }
        return fact;
    }
}
