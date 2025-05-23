/*
 * This source file was generated by the Gradle 'init' task
 */
package blatt01;

import java.util.Random;

public class App {

    public static int[] randomArray(int size, int lower, int upper) {
        Random rd = new Random();
        int[] arr = new int[size];
        for (int ii = 0; ii < size; ii++) {
            arr[ii] = rd.nextInt(upper-lower) + lower;
        }
        return arr;
    }

    public static int[] sort(int[] unsortedArray) {
        if (unsortedArray == null) {
            throw new NullPointerException("Array should not be null!");
        }
        if (unsortedArray.length == 0) {
            throw new IllegalArgumentException("Array should not be empty!");
        }

        int biggest = 0, biggestIdx = 0;
        int size = unsortedArray.length;
        int[] sortedArray = new int[size];

        for (int jj = 0; jj < size; jj++) {
            for (int ii = 0; ii < size; ii++) {
                if (unsortedArray[ii] > biggest) {
                    biggest = unsortedArray[ii];
                    biggestIdx = ii;
                }
            }
            unsortedArray[biggestIdx] = 0;
            sortedArray[size - jj - 1] = biggest;
            biggest = 0;
        }
        return sortedArray;
    }

    public static void main(String[] args) {
        int size = 1000;

        int[] arr = randomArray(size, 0, 100);
        int[] sortedArr = sort(arr);

        for (int ii = 0; ii < size; ii += 10)
            System.out.println(sortedArr[ii]);
    }
}
