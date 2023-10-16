package org.example;

public class Main {
    public static void main(String[] args) {
        C gamma = new C();
        B beta = gamma;
        A alfa = new A();
        System.out.println(beta.f(beta, beta, gamma));
        System.out.println(gamma.f(beta, null, beta));
        System.out.println(gamma.f(alfa, beta, gamma));
        System.out.println(((Object) gamma).equals((Object) alfa));
    }
}