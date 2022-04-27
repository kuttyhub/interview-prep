public class RepetedNumber {
    public static void main(String[] args) {
        int[] array = { 1, 2, 3, 2, 5 };
        findRepetedNumber(array);
    }

    public static void findRepetedNumber(int[] array) {
        for (int i : array) {
            int idx = Math.abs(i) - 1;
            if (array[idx] > 0) {
                array[idx] = -array[idx];
            } else {
                System.out.println(Math.abs(i));
            }
        }
        System.out.println();
        for (int i : array) {
            System.out.print(String.valueOf(i) + " ");
        }
    }
}
