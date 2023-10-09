package org.example;

public class Main {
    public static void main(String[] args) {
        C gamma = new C();
        B beta = gamma;
        B[] array = new B[10];
        System.out.println(beta. f (gamma, array));
        System.out.println(gamma.f(beta, null));
        System.out.println(beta. f (array [0], null));
    }
}