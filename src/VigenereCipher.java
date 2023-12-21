import java.util.ArrayList;
import java.util.List;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
public class VigenereCipher implements Cipher {

    public static List<List<String>> generateVigenereSquare() {
        String alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        List<List<String>> vigenereSquare = new ArrayList<>();

        for (int i = 0; i < 26; i++) {
            List<String> row = new ArrayList<>();
            for (int j = 0; j < 26; j++) {
                row.add(String.valueOf(alphabet.charAt((i + j) % 26)));
            }
            vigenereSquare.add(row);
        }
        return vigenereSquare;
    }
    public static List<String> keyCreator(List<String> messageFinal, List<String> keywordFinal) {
        List<String> key = new ArrayList<>();
        int k = 0;
        for (String i : messageFinal) {
            key.add(keywordFinal.get(k));
            k++;
            if (k == keywordFinal.size()) {
                k = 0;
            }
        }
        return key;
    }

    @Override
    public String encrypt(String message_filename, String key_filename) {
        List<String> keywordFinal = readFromFile(key_filename);
        List<String> messageFinal = readFromFile(message_filename);
        List<String> key = keyCreator(messageFinal, keywordFinal);

        for (int letter = 0; letter < messageFinal.size(); letter++) {
            messageFinal.set(letter, messageFinal.get(letter).toUpperCase());
        }

        for (int letter = 0; letter < key.size(); letter++) {
            key.set(letter, key.get(letter).toUpperCase());
        }

        List<Integer> messageNumbers = new ArrayList<>();
        List<Integer> keyNumbers = new ArrayList<>();

        for (String letter : messageFinal) {
            messageNumbers.add((int) letter.charAt(0) - 'A' + 1);
        }

        for (String letter : key) {
            keyNumbers.add((int) letter.charAt(0) - 'A' + 1);
        }
        int p = 0;
        int q = 0;
        List<String> crip = new ArrayList<>();
        for (String letter : messageFinal) {
            if (letter.matches("[a-zA-Z]")) {
                crip.add(generateVigenereSquare().get(keyNumbers.get(p) - 1).get(messageNumbers.get(q) - 1));
                p++;
                q++;
            } else {
                crip.add(letter);
                p++;
                q++;
            }
        }

        for (int letter = 0; letter < crip.size(); letter++) {
            if (crip.get(letter).equals("|")) {
                crip.set(letter, crip.get(letter).replace("|", " "));
            }
        }
        return String.join("", crip);
    }


    @Override
    public String decrypt(String message_filename, String key_filename) {
        List<String> keywordFinal = readFromFile(key_filename);
        List<String> encryptedMessageFinal = readFromFile(message_filename);
        List<String> key = keyCreator(encryptedMessageFinal, keywordFinal);

        for (int letter = 0; letter < encryptedMessageFinal.size(); letter++) {
            encryptedMessageFinal.set(letter, encryptedMessageFinal.get(letter).toUpperCase());
        }

        for (int letter = 0; letter < key.size(); letter++) {
            key.set(letter, key.get(letter).toUpperCase());
        }
        List<Integer> messageNumbers = new ArrayList<>();
        List<Integer> keyNumbers = new ArrayList<>();
        for (String letter : encryptedMessageFinal) {
            //messageNumbers.add((int) letter.charAt(0) - 'A' + 1);
            messageNumbers.add(getNumericalEquivalent(letter));
        }

        for (String letter : key) {
            //keyNumbers.add((int) letter.charAt(0) - 'A' + 1);
            keyNumbers.add(getNumericalEquivalent(letter));
        }

        List<Integer> res = new ArrayList<>();
        List<String> finalList = new ArrayList<>();

        for (int number = 0; number < messageNumbers.size(); number++) {
            res.add((messageNumbers.get(number) - keyNumbers.get(number)) + 1);
            if (res.get(number) < 0) {
                res.set(number, res.get(number) + 26);
            }
            finalList.add(String.valueOf((char) (res.get(number) + 64)));
        }

        List<String> decrip = new ArrayList<>();
        int p = 0;

        for (String letter : encryptedMessageFinal) {
            if (letter.matches("[a-zA-Z]")) {
                decrip.add(finalList.get(p));
                p++;
            } else {
                decrip.add(letter);
                p++;
            }
        }

        for (int letter = 0; letter < decrip.size(); letter++) {
            if (decrip.get(letter).equals("|")) {
                decrip.set(letter, decrip.get(letter).replace("|", " "));
            }
        }

        return String.join("", decrip);
    }
    private int getNumericalEquivalent(String letter) {
        if (letter.matches("[a-zA-Z]")) {
            char uppercaseChar = Character.toUpperCase(letter.charAt(0));
            return uppercaseChar - 'A' + 1;
        } else {
            return -1;
        }
    }
    private List<String> readFromFile(String filename) {
        List<String> characters = new ArrayList<>();

        try (BufferedReader br = new BufferedReader(new FileReader(filename))) {
            String line;
            while ((line = br.readLine()) != null) {
                for (char c : line.toCharArray()) {
                    characters.add(String.valueOf(c));
                }
                characters.add("\n");
            }
            characters.remove(characters.size() - 1);
        } catch (IOException e) {
            e.printStackTrace();
        }

        return characters;
    }

    public static void main(String[] args) {
        VigenereCipher vigenereCipher = new VigenereCipher();

        System.out.println(vigenereCipher.encrypt("encrypt_check.txt", "key_check.txt"));

        System.out.println(vigenereCipher.decrypt("decrypt_check.txt", "key_check.txt"));

        System.out.println("attack on dawn");

    }
}
