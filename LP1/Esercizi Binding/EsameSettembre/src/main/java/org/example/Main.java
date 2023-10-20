package org.example;

public class Main {
    public static void main(String[] args) {
        B beta = new B();
        A alfa = beta;
        System.out.println(alfa.f(null, 1, 2));
        System.out.println(beta.f(alfa, 1.0, 2));
       // System.out.println(beta.f(alfa, 1,2));
        System.out.println(alfa.f(alfa, 1, 2));
    }
}