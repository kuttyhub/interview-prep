public class RotateArray {
    public static void main(String[] args) {
        int[][] array = { { 1, 2, 3 }, { 4, 5, 6 }, { 7, 8, 9 } };
        printArray(array, 3);
        array = rotate(array, 3);
        printArray(array, 3);
    }

    public static int[][] rotate(int[][] array, int n) {

        int[][] newArray = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                newArray[j][n - i - 1] = array[i][j];
            }
        }
        return newArray;
    }

    public static void printArray(int[][] array, int n) {
        System.out.println();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(array[i][j] + " ");
            }
            System.out.println();
        }
    }
}
