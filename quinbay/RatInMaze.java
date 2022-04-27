public class RatInMaze {
    public static void main(String[] args) {
        int[][] maze = { { 1, 0, 0, 0 }, { 1, 1, 0, 1 }, { 0, 1, 0, 0 }, { 1, 0, 1, 1 } };
        int[] start = { 0, 0 };
        int[] end = { 3, 3 };
        System.out.println(canReach(maze, start, end));
    }

    private static boolean canReach(int[][] maze, int[] possition, int[] end) {
        if (possition[0] == end[0] && possition[1] == end[1]) {
            return true;
        }
        if (possition[0] > end[0] || possition[1] > end[1] || maze[possition[0]][possition[1]] == 0) {
            return false;
        }
        return canReach(maze, new int[] { possition[0] + 1, possition[1] }, end)
                || canReach(maze, new int[] { possition[0], possition[1] + 1 }, end);
    }
}
