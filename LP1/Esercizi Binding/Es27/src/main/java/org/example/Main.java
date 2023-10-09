package org.example;

public class Main {
    public static void main(String[] args) {
        B[] arrayB = new B[10];
        A[] arrayA = arrayB;
        arrayB[0] = new B();
        System.out.println(arrayB[0]. f (null, arrayB));
        System.out.println(arrayA[0]. f (null, arrayA));
        System.out.println(arrayA[0]. f (arrayA[0], null));
    }
}