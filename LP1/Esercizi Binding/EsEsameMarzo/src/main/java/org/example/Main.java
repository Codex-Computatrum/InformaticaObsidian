package org.example;

public class Main {
    public static void main(String[] args){
        C gamma = new C();
        B beta = gamma;
        A alfa = gamma;
        //System.out.println(alfa.f(null, 10));
        System.out.println(gamma.f(alfa, 0));
        System.out.println(alfa.f(beta, 10));
        //System.out.println(gamma.f(gamma, -5));

    }
}