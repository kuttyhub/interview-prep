import java.util.Scanner;

/*
    Write a Java Program to check if any number is a magic number or not.
    A number is said to be a magic number if after doing sum of digits in each step 
    and inturn doing sum of digits of that sum, 
    the ultimate result (when there is only one digit left) is 1.
        
        Step 1: 163 => 1+6+3 = 10
        Step 2: 10 => 1+0 = 1 => Hence 163 is a magic number
*/

public class MagicNumber {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = sc.nextInt();
        System.out.println(isMagicNumberGeneric(n));
        System.out.println(isMagicNumberRecursion(n));
        sc.close();

    }

    public static boolean isMagicNumberGeneric(int n) {
        int sum = 0;
        while (n > 0 || sum > 9) {
            if (n == 0) {
                n = sum;
                sum = 0;
            }
            sum += n % 10;
            n /= 10;
        }
        return sum == 1 ? true : false;
    }

    public static int getDigitSum(int n) {
        int sum = 0;
        int temp = n;
        while (temp != 0) {
            sum += temp % 10;
            temp /= 10;
        }
        return sum;
    }

    public static boolean isMagicNumberRecursion(int n) {
        if (n / 10 == 0) {
            return false;
        }
        int sum = getDigitSum(n);
        if (sum == 1) {
            return true;
        }
        return isMagicNumberRecursion(sum);
    }
}
