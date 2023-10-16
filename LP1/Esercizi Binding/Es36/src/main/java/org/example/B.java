package org.example;

class B extends A {
    public String f (Object x, A y, A z) { return "B1␣+␣" + f(null, new B(), new C()); }
    private String f(B x, B y, C z) { return "B2"; }
}
