package org.grokking.algrotihmswithjava.chapter1.binarysearch.recursion;

import java.util.Collections;
import java.util.List;

import org.grokking.algrotihmswithjava.chapter1.binarysearch.IBinarySearch;

public class BinarySearchWithRecursion implements IBinarySearch {


    @Override
    public int binarySearch(List<String> arr, String item) {
        Collections.sort(arr);
        System.out.println("sorted array: "+arr);
        int low = 0; int high = arr.size()-1;
        return binarySearchHelper(arr, item, low, high);
    }

    private static int binarySearchHelper(List<String> arr, String item, int low, int high) {
        int mid = (low + high)/2;
        System.out.println("guessed position: "+mid);

        if (low > high) return -1;

        if (item.compareTo(arr.get(mid)) > 0) {
            low = mid+1;
            return binarySearchHelper(arr, item, low, high);
        } else if (item.compareTo(arr.get(mid)) < 0) {
            high = mid-1;
            return binarySearchHelper(arr, item, low, high);
        } else return mid;
    }
}
