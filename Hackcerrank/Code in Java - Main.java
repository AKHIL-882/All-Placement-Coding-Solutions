import java.util.HashMap;
import java.util.Map;

class Result {
    public static int getDistance(String word) {
        String[][] keyword = {
            {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"},
            {"Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"},
            {"A", "S", "D", "F", "G", "*", "H", "J", "K", "L"},
            {" ", "Z", "X", "C", "V", "B", "N", "M", " ", " "}
        };

        Map<String, int[]> set_ = new HashMap<>();
        for (int i = 0; i < keyword.length; i++) {
            for (int j = 0; j < keyword[i].length; j++) {
                set_.put(keyword[i][j], new int[]{i, j});
            }
        }

        int[] ini = set_.get("*");
        int result = 0;

        for (char i : word.toCharArray()) {
            String s = String.valueOf(i);
            int[] j = set_.get(s);
            result += Math.abs(ini[0] - j[0]) + Math.abs(ini[1] - j[1]);
            ini = j;
        }

        return result;
    }
    
    
    // Dont write this below lines
    public static void main(String[] args) {
        System.out.println(getDistance("QZ"));
        System.out.println(getDistance("QA"));
        System.out.println(getDistance("HELLO123"));
    }
}
