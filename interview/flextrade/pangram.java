import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;


class Result {

    /*
     * Complete the 'isPangram' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts STRING_ARRAY pangram as parameter.
     */

    public static String isPangram(List<String> pangram) {
        return pangram.stream().map((sentence) -> {
            Set<Character> letters = new HashSet<>();
            for (Character letter : sentence.toCharArray()) {
                if (letter == ' ') {
                    continue;
                }
                if (letters.size() == 26) {
                    return "1";
                }
                letters.add(letter);
            }
            if (letters.size() == 26) {
                return "1";
            } else {
                return "0";
            }
        }).collect(Collectors.joining());
    }
}
