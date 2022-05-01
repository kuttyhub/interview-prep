public class mergeIsland {
    public static void main(String[] args) {
        char[][] grid = {
                { '1', '1', '1', '0', '0' },
                { '1', '1', '0', '0', '0' },
                { '0', '0', '1', '0', '1' },
                { '0', '0', '0', '1', '1' }
        };
        System.out.println(numberOfIslands(grid));

    }

    public static int numberOfIslands(char[][] grid) {
        if (grid == null || grid.length == 0 || grid[0].length == 0)
            return 0;

        int m = grid.length;
        int n = grid[0].length;

        int count = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1') {
                    count++;
                    mergeIslands(grid, i, j);
                }
            }
        }
        return count;
    }

    public static void printArray(char[][] grid) {
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                System.out.print(grid[i][j] + " ");
            }
            System.out.println();
        }
    }

    public static void mergeIslands(char[][] grid, int i, int j) {
        int m = grid.length;
        int n = grid[0].length;

        if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] != '1')
            return;

        grid[i][j] = 'X';

        mergeIslands(grid, i - 1, j);
        mergeIslands(grid, i + 1, j);
        mergeIslands(grid, i, j - 1);
        mergeIslands(grid, i, j + 1);
    }
}
