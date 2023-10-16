package org.example;

class C extends B {
    public String f(Object a, B b) { return "C1"; }
    public String f(A a, B b) { return "C2"; }
}
