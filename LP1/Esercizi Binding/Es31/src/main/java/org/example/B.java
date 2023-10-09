package org.example;

class B extends A {
    public String f(B a, B b) { return "B1␣+␣" + f(a, (A)b); }
    public String f(A a, B b) { return "B2"; }
}
