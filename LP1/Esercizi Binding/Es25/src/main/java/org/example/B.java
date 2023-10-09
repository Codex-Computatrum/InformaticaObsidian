package org.example;

class B extends A {
    public String f (B x, B y) { return "B1␣+␣" + f(null, (A)y); }
    private String f(A x, B y) { return "B2␣+␣" + f(y, y); }
}