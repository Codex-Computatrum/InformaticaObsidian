package org.example;

public class Main {
    public static void main(String[] args) {
        C gamma = new C();
        B beta = gamma;
        A alfa = gamma;
        System.out.println( alfa . f (gamma, 3));
        System.out.println(gamma.f(null, 4));
        //System.out.println(gamma.f(beta, 3));
        System.out.println("1" + 1);
    }
}