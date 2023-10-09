package org.example;

class A {
    public String f(A x, A y, B z) { return "A1"; }
    public String f(A x, Object y, A z) { return "A2"; }
    private String f(B x, Object y, B z) { return "A3"; }
}
