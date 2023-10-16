package org.example;

class A {
    public String f(Object a, A b) { return "A1"; }
    public String f(A a, C b) { return "A2"; }
}