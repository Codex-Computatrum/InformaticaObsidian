package org.example;

class B extends A {
    public String f (Object a, A b) { return "B1␣+␣" + f(null, new B()); }
    private String f(A a, B b) { return "B2"; }
}