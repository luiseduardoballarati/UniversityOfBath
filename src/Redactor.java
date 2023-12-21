public class Redactor {

    public static void main(String[] args) {
        String content = "The quick brown eFOXe 123 jumps over the lazy dog! Fox % lalala $";
        String[] redactList = {"fox", "jumps", "%", "$"};

        System.out.println(redact(content, redactList));
    }

    public static String redact(String content, String[] redactWords) {
        for (String word : redactWords) {
            String escapedWord = word.replaceAll("[.*+?^${}()|\\[\\]\\\\]", "\\\\$0");

            int numLetters = LetterCounter(word);

            String pattern = "(?i)\\b" + escapedWord + "\\b";

            String replacement = "*".repeat(numLetters);
            content = content.replaceAll(pattern, replacement);
        }

        return content;
    }

    private static int LetterCounter(String word) {
        int count = 0;
        for (char c : word.toCharArray()) {
            if (Character.isLetter(c)) {
                count++;
            }
        }
        return count;
    }
}