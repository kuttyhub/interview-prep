import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

class DistinctElement {
    public static void main(String[] args) {
        int[] array = { 1, 2, 3, 4, 5, 4, 3, 1 };
        usingSet(array);

    }

    public static void usingHash(int[] array) {
        Map<Integer, Integer> map = new HashMap<>();
        for (var i : array) {
            map.put(i, map.getOrDefault(i, 0) + 1);
        }
        for (int i = 0; i < array.length; i++) {
            if (map.get(array[i]) == 1) {
                System.out.print(String.valueOf(i) + " ");
            }
        }
    }

    public static void usingSet(int[] array) {
        Set<Integer> set = new HashSet<>();
        for (int i = 0; i < array.length; i++) {
            if (!set.contains(array[i])) {
                System.out.print(String.valueOf(array[i]) + " ");
                set.add(i);
            }

        }
    }
}