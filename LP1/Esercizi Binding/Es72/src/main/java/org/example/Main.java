package org.example;

public class Main {
    public static void main(String[] args) {
        C gamma = new C();
        B beta = gamma;
        A alfa = new B();
        System.out.println(beta. f (null, 7));
        System.out.println( alfa . f (gamma, 5));
        System.out.println(gamma.f(beta, 3.0));
        System.out.println((1 << 1) > 1);
    }
}