package org.example;

public class C extends B{
    public String f(B x, int y){ return "C1";}
    public String f(C x, long y){ return "C2";}
}
