package org.example;

class B extends A {
    public String f(Object x, A y, B z) { return "B1␣+␣" + f(null, z, new B()); }
    private String f(B x, B y, B z) { return "B2"; }
}
