package org.example;

public class A {
    public String f(B x, int y){ return "A1";}
    public String f(Object x, int y){ return "A2";};

    public String f(C x, long y){ return "A3";}
}
