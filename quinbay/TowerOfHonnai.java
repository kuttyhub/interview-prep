// Write a Java program for solving the Tower of Hanoi Problem.

public class TowerOfHonnai {
    public static void main(String[] args) {
        TOH('A', 'B', 'C', 3);
    }

    private static void TOH(char source, char auxiliary, char destination, int numOfDisk) {
        if (numOfDisk > 0) {
            TOH(source, destination, auxiliary, numOfDisk - 1);
            System.out.println(
                    "Move " + numOfDisk + " disk from " + source + " to " + destination + " using " + auxiliary + ".");
            TOH(auxiliary, source, destination, numOfDisk - 1);
        }
    }
}
