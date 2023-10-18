package org.example;

public class Main {
    public static void main(String[] args) {
        A[] arr = new B[10];
        C gamma = new C();
        B beta = gamma;
        A alfa = gamma;
        //System.out.println(beta. f (null, arr));
        System.out.println(gamma.f(arr, alfa));
        System.out.println(gamma.f(alfa, arr));
        System.out.println(1 << 1);
    }
}
