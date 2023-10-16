package org.example;

class C extends B {
    public String f(A x, int n) { return "C1:" + n; }
    public String f(C x, double n) { return "C2:" + f(x, x); }
}

