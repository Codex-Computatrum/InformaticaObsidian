package org.example;

class A {
    public String f(Object x, A y, B z) { return "A1"; }
    public String f(A x, C y, C z) { return "A2"; }
}

