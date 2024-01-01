package org.grokking.algrotihmswithjava.chapter1.binarysearch.iteration;

import java.util.Collections;
import java.util.List;

import org.grokking.algrotihmswithjava.chapter1.binarysearch.IBinarySearch;

public class BinarySearchWithIteration implements IBinarySearch {

    @Override
    public int binarySearch(List<String> arr, String item) {
        Collections.sort(arr);
        System.out.println("sorted array: "+arr);
        int low = 0; int high = arr.size() - 1;

        while (low <= high) {
            int mid = (low + high)/2;
            System.out.println("guessed position: "+mid);
            if (item.compareTo(arr.get(mid)) > 0) {
                low = mid +1;
            } else if (item.compareTo(arr.get(mid)) < 0) {
                high = mid - 1;
            } else return mid;
        }
        return -1;
    }

}

