package org.example;


class B extends A {
    public String f(A x, A y, B z) { return "B1" + f(x, this, z); }
    private String f(A x, B y, B z) { return "B2"; }
    public String f(B x, Object y, B z) { return "B3"; }
}
