import java.util.ArrayList;
import java.util.Collections;
import java.util.List;


class Result {

    /*
     * Complete the 'findBeforeMatrix' function below.
     *
     * The function is expected to return a 2D_INTEGER_ARRAY.
     * The function accepts 2D_INTEGER_ARRAY after as parameter.
     */

    public static List<List<Integer>> findBeforeMatrix(List<List<Integer>> after) {
        List<List<Integer>> before = new ArrayList<>(after.size());
        for (int i = 0; i < after.size(); i++) {
          before.add(new ArrayList<>(Collections.nCopies(after.get(0).size(), 0)));
        }

        for (int i = 0; i < after.size(); i++) {
            for (int j = 0; j < after.get(0).size(); j++) {
                int top = i > 0 ? after.get(i-1).get(j) : 0;
                int left = j > 0 ? after.get(i).get(j - 1) : 0;
                int topLeft = i > 0 && j > 0 ? after.get(i-1).get(j-1) : 0;
                int current = after.get(i).get(j);
                before.get(i).set(j, current - top - left + topLeft);
            }
        }
        return before;
    }
}
