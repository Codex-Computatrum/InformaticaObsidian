package org.example;

class B extends A {
    public String f (Object x, A y, A z) { return "B1␣+␣" + f(null, new B(), y); }
    private String f(A x, B y, B z) { return "B2"; }
}
