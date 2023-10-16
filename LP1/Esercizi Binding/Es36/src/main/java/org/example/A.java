package org.example;

class A {
    public String f (Object x, A y, A z) { return "A1"; }
    private String f(A x, B y, B z) { return "A2"; }
}