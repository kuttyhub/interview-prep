import java.util.Scanner;

public class FindPrimeSum {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = sc.nextInt();
        findPrimeSum(n);
        sc.close();
    }

    public static void findPrimeSum(int n) {
        for (int first = 2; first <= n; first++) {
            if (isPrime(first)) {
                int second = n - first;
                if (isPrime(second)) {
                    System.out.println(first + " " + second);
                }

            }
        }
    }

    public static boolean isPrime(int n) {
        if (n > 1) {
            for (int i = 2; i < n / 2; i++) {
                if (n % i == 0) {
                    return false;
                }
            }
            return true;
        }

        return false;
    }
}
