package org.example;


class C extends B {
    public String f(B x, float y) { return "C1"; }
    public String f(Object x, double y) { return "C2"; }
    public String f(C x, int y) { return "C3:" + f(x, y * 2.0); }
}

