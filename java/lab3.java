package java;

import java.util.ArrayList;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class lab3 {

    public static void main(String[] args) {

        int in, inputs;
        ArrayList<String> regX = new ArrayList<>();
        ArrayList<String> testers = new ArrayList<>();
        ArrayList<Boolean> results = new ArrayList<>();
        ArrayList<Integer> resultsCode = new ArrayList<>();
        Scanner sc = new Scanner(System.in);
        in = sc.nextInt();

        for (int i = 0; i < in; i++) {
            Scanner sca = new Scanner(System.in);
            String x = sca.nextLine();
            regX.add(x);
        }
        inputs = sc.nextInt();
        for (int i = 0; i < inputs; i++) {
            Scanner sca = new Scanner(System.in);
            String x = sca.nextLine();
            testers.add(x);
            results.add(Boolean.FALSE);
        }

        for (int i = 0; i < inputs; i++) {
            String x = testers.get(i);
            for (int j = 0; j < regX.size(); j++) {
                String patternStr = regX.get(j);
                Pattern pattern = Pattern.compile(patternStr);

                String input = x;

                // create a matcher that will match the given input against this pattern
                Matcher matcher = pattern.matcher(input);

                boolean matchFound = matcher.matches();
                results.set(i, matchFound);
                if (matchFound == true) {
                    break;
                }

            }
        }

        for (int i = 0; i < results.size(); i++) {
            if (results.get(i).equals(true)) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }

        }

    }

}