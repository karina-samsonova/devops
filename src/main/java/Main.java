import java.util.HashMap;

import static java.lang.Thread.sleep;

public class Main {

    public static void main(String[] args) throws InterruptedException {
        // write your code here
        HashMap<Integer, String> alphabet = new HashMap<>();
        alphabet.put(1,"Aa");
        alphabet.put(2,"Bb");
        alphabet.put(3,"Cc");
        alphabet.put(4,"Dd");
        alphabet.put(5,"Ee");

        MapIterator<Integer, String> it = new MapIterator<>(alphabet);
        it.next();
        it.remove();    //удалили первый элемент из словаря
        while(it.hasNext()){
            System.out.println(it.next());
            sleep(1000);
        }
    }
}

