package org.example;

public class Main {
    public static void main(String[] args) {
        B beta = new B();
        A alfa = beta;
        System.out.println( alfa . f (null, alfa ));
        System.out.println(beta. f (beta, beta));
        System.out.println(beta.getClass() == alfa.getClass());
    }
}