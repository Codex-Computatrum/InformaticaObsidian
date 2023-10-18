package org.example;

public class B extends A{
    public String f(Object x, int y){ return "B1";}
    public String f(B x, int y){ return "B2";}
    private String f(B x, double y){ return "B3";}

}
