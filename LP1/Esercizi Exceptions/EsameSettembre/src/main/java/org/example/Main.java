package org.example;

public class Main {
    public static void main(String[] args) throws Exception {
        try {
            m();
            System.out.println(1);
        } catch (MyExc3 j) {
            System.out.println(2);
            throw (new MyExc2());
        } catch (MyExc1 t) {
            System.out.println(3);
        } catch (MyExc2 t) {
            System.out.println(4);
        } finally {
            System.out.println(5);
            throw (new MyExc2());
        }
    }
    static void m() throws Exception{
        try{
            System.out.println(6);
        }catch(MyExc1 z){

        } catch(MyExc3 s){

    }
}
}