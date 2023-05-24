package interview.mntn;

import java.io.FileInputStream;
import java.io.IOException;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;

/**
 * There is a CSV file in the data directory.
 *
 * Each row in the file is comma separated:
 * - the first item is a C or an I
 * - the second item is a matching ID
 * - the third item is a score (only for lines starting with I)
 *
 * 1. Compute the sum of all scores for records starting with I
 * 2. Compute the sum of records starting with a C by using the scores from the I records with a matching ID
 **/

class Main {

    private static String DIR_NAME = "data";

    private static void handleFile(String fname) throws IOException {
        try (final Scanner scanner = new Scanner(new FileInputStream(fname))) {
            Map<String, Integer> keyToScore = new HashMap<>();
            Set<String> cSet = new HashSet<>();

            int sumI = 0;
            int sumC = 0;
            while (scanner.hasNextLine()) {
                final String line = scanner.nextLine();
                final String[] values = line.split(",");
                final String key = values[1];

                if (values[0].equals("I")) {
                    final int score = Integer.valueOf(values[2]);
                    keyToScore.putIfAbsent(key, score);
                    sumI += score;

                    if (cSet.remove(key)) {
                        sumC += score;
                    }
                } else if (values[0].equals("C")) {
                    if (keyToScore.containsKey(key)) {
                        sumC += keyToScore.get(key);
                    } else {
                        cSet.add(key);
                    }
                }
            }

            System.out.println(sumI);
            System.out.println(sumC);
            assert sumI == 60;
            assert sumC == 60;
        } catch (IOException e) {
            System.out.println(e);
        }
    }

    public static void main(String[] args) throws Exception {
        System.out.println(String.format("Working in %s", System.getProperty("user.dir")));
        handleFile(String.format("%s/%s", DIR_NAME, "input.csv"));
    }
}
