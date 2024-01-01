package org.grokking.algrotihmswithjava.chapter1.binarysearch;

import java.util.Arrays;
import java.util.List;

import org.grokking.algrotihmswithjava.chapter1.binarysearch.iteration.BinarySearchWithIteration;
import org.grokking.algrotihmswithjava.chapter1.binarysearch.recursion.BinarySearchWithRecursion;

public class Service {

    public static void main(String[] args) {
        List<String> students = Arrays.asList("Patrick", "Josephine", "Ibukun", "Tolu", "Ernest", "Precious", "Maurice", "Zachariah");
        String item = "Tolu";
        IBinarySearch binarySearchIteration = new BinarySearchWithIteration();
        IBinarySearch binarySearchRecursion = new BinarySearchWithRecursion();

        int position = binarySearchIteration.binarySearch(students, item);
        System.out.printf("using iteration: position of %s is %d%n", item, position);

        position = binarySearchRecursion.binarySearch(students, item);
        System.out.printf("using recursion: position of %s is %d%n", item, position);


    }
}
