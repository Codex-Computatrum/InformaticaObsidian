package org.example;

class B extends A {
    private String f(B x, B y) { return "B1␣:␣" + f(null, (A)y); }
    public String f(Object x, B y) { return "B2␣:␣" + f(x, (A)y); }
    public String f(A x, B y) { return "B3␣:␣" + f(y, y); }
}
