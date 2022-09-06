import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String input = br.readLine();
        int[] alphabet = new int[26];
        for(int i = 0; i < input.length(); i++){
            int index = input.charAt(i);
            if(index >= (int)'a') index -= (int)'a';
            else index -= (int)'A';
            alphabet[index]++;
        }
        char ch = '?';
        int max = -1;
        for(int i=0; i < alphabet.length; i++){
            if(alphabet[i]>max){
                max = alphabet[i];
                ch = (char) (i+65);
            }
            else if (alphabet[i] == max) ch = '?';
        }
        bw.write(ch);
        bw.flush();
        bw.close();
    }
}
