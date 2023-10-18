package org.example;

public class Main {
    public static void main(String[] args) throws Exception{
        try{
            System.out.println(1);
            m();
            System.out.println(2);
        }
        }
        static void m() throws Exception{
        try{
            throw (new MyExc1());
        } catch(MyExc2 z){
        }
        catch(Exception c){
            throw (new MyExc1());
        }
        catch(MyExc3 k){
            System.out.println(3);
        }
        finally{
            System.out.println(4);
        }
}