package org.example;

public class Main {
    public static void main(String[] args) throws Exception{
        try{
            System.out.println("Hello World!");
        }catch (MyExc1 e){
            System.out.println(e);
        }

    }
}