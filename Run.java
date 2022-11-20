/*
 * RUN THIS FILE OR RUN.PY TO USE THIS PROGRAM
 * 
 * DO NOT LOG INTO CODINGBAT WHILE IT IS RUNNING!!
 * ANYTHING BEFORE OR AFTER IS FINE THO
 */

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class Run {
    public static void main(String[] args) {
        CodingbatClient client = new CodingbatClient();

        // gets user input
        Scanner scanner = new Scanner(System.in);
        System.out.print("Email Address: ");
        String emailAddress = scanner.nextLine();
        System.out.print("Password: ");
        String password = scanner.nextLine();

        // clears the screen
        System.out.print("\033[H\033[2J");
        System.out.flush();

        scanner.close();

        client.doLogin(emailAddress, password);

        List<Answer> answers = readAnswersFromFile();
        for (Answer answer : answers) {
            client.submitAnswer(answer);
            System.out.println("Completed " + answer.name);
        }
    }

    private static List<Answer> readAnswersFromFile() {
        String text;
        try {
            byte[] encodedText = Files.readAllBytes(Paths.get("./answers.json"));
            text = new String(encodedText, StandardCharsets.UTF_8);
        } catch (IOException e) {
            e.printStackTrace();
            return null;
        }
        ArrayList<Answer> answers = new ArrayList<>();
        String name = "";
        String id = "";
        String code = "";
        int quotesCounter = 0;
        for (int i = 0; i < text.length(); i++) {
            char c = text.charAt(i);
            if (c == '"' && text.charAt(i - 1) != '\\') { // 2nd condition removes quotes in code
                quotesCounter++;
                if (quotesCounter == 6 && text.charAt(i + 1) == '}') { // resets if code is missing
                    quotesCounter = 0;
                } else {
                    continue;
                }
            }
            switch (quotesCounter) {
                case 1:
                    name += c;
                    break;
                case 5:
                    id += c;
                    break;
                case 9:
                    code += c;
                    break;
                case 10:
                    answers.add(new Answer(name, id, code));
                    quotesCounter = 0;
                    name = "";
                    id = "";
                    code = "";
                    break;
            }
        }
        return answers;
    }
}