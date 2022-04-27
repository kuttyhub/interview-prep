import java.time.Duration;
import java.time.Instant;
import java.util.Scanner;

public class FibonacciSeries {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of terms: ");
        int n = sc.nextInt();
        System.out.println(fibonacciGeneric(n));

        Instant start = Instant.now();

        System.out.println(fibonacciRecursion(n));

        Instant end = Instant.now();
        Duration timeElapsed = Duration.between(start, end);
        System.out.println("Recurssion -> Time elapsed: " + timeElapsed.toNanos() + " ns");

        start = Instant.now();
        printFibonacci(0, 1, n + 1);
        end = Instant.now();
        timeElapsed = Duration.between(start, end);
        System.out.println("Iteration -> Time elapsed: " + timeElapsed.toNanos() + " ns");
        sc.close();
    }

    public static int fibonacciGeneric(int n) {
        Instant start = Instant.now();
        // time passes
        int first = 0, second = 1;
        for (int i = 2; i < n; i++) {
            int sum = first + second;
            first = second;
            second = sum;
        }
        Instant end = Instant.now();
        Duration timeElapsed = Duration.between(start, end);
        System.out.println("Generic -> Time elapsed: " + timeElapsed.toNanos() + " ns");
        return second;

    }

    public static int fibonacciRecursion(int n) {

        if (n == 0) {
            return 0;
        }
        if (n == 1) {
            return 1;
        }
        return fibonacciRecursion(n - 1) + fibonacciRecursion(n - 2);
    }

    public static void printFibonacci(int first, int second, int size) {
        if (size == 0) {
            return;
        }
        System.out.print(first + " ");
        printFibonacci(second, first + second, size - 1);
    }
}
