package org.example;

class C extends B {
    public String f(A x, B y, B z) { return "C1␣+␣" + f(this, this, z); }
    public String f(B x, B y, B z) { return "C2"; }
}
