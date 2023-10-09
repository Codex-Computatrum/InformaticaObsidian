package org.example;

class A {
    public String f(Object a, B b) { return "A1"; }
    public String f(A a, A b) { return "A2"; }
    public String f(B a, C b) { return "A3"; }
}