package org.example;

public class Main {
        public static void main(String[] args) {
            B beta = new B();
            A alfa = (A) beta;
            System.out.println( alfa . f ( alfa , beta, beta));
            System.out.println( alfa . f (beta, alfa , null));
            System.out.println(beta. f (beta, beta, beta));
            System.out.println( alfa instanceof B);
        }
    }